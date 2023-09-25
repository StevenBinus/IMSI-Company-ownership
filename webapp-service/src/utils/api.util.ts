import axios, { AxiosInstance } from 'axios'

import { getCookie, setCookie } from './cookies.util'

export interface ResponseProps<T> {
	status_code: number
	message: string
	page_limit?: number
	page?: number
	total_rows?: number
	total_pages?: number
	data: T // If Extended also has T in the interface
}

// export const BACKEND_URL = 'http://172.16.5.40:8087/api'
export const BACKEND_URL = 'http://10.1.32.26:8000'

let instance: null | (() => AxiosInstance) = null

export function getApiInstance(): AxiosInstance {
	const token = getCookie('token')
	if (!instance) {
		return axios.create({
			baseURL: `${BACKEND_URL}`,
			headers: {
				Authorization: `Bearer ${token}`,
			},
		})
	}
	return instance && instance()
}

// custom Axios only used in refresh token
const customAxios = axios.create({
	baseURL: `${BACKEND_URL}`,
})

// export function getApiInstance(): AxiosInstance {
// 	const token = getCookie('token')
// 	if (!instance) {
// 		customAxios.defaults.headers.common['Authorization'] = `Bearer ${token}`
// 		return customAxios
// 	}
// 	return instance && instance()
// }

let isAlreadyFetchingAccessToken = false

// This is the list of waiting requests that will retry after the JWT refresh complete
let subscribers = []

function onAccessTokenFetched(access_token) {
	// When the refresh is successful, we start retrying the requests one by one and empty the queue
	subscribers.forEach((callback) => callback(access_token))
	subscribers = []
}

function addSubscriber(callback) {
	subscribers.push(callback)
}

async function refreshTokenAndReattemptRequest(error) {
	try {
		const { response: errorResponse } = error

		const refreshToken = getCookie('refreshToken') // Your own mechanism to get the refresh token to refresh the JWT token
		if (!refreshToken) {
			// We can't refresh, throw the error anyway
			// will add remove cookie and local storage
			alert('Session Expired')
			return Promise.reject(error)
		}
		/* Proceed to the token refresh procedure
    We create a new Promise that will retry the request,
    clone all the request configuration from the failed
    request in the error object. */
		const retryOriginalRequest = new Promise((resolve) => {
			/* We need to add the request retry to the queue
    since there another request that already attempt to
    refresh the token */
			addSubscriber((access_token) => {
				errorResponse.config.headers.Authorization = 'Bearer ' + access_token
				resolve(axios(errorResponse.config))
			})
		})
		if (!isAlreadyFetchingAccessToken) {
			isAlreadyFetchingAccessToken = true
			const response = await axios({
				method: 'post',
				url: `${BACKEND_URL}/getAccessToken`,
				data: {
					token: refreshToken, // Just an example, your case may vary
				},
			})
			if (!response.data) {
				// will add remove cookie and local storage
				alert('Session Expired')
				return Promise.reject(error)
			}
			const newToken = response.data.token
			setCookie('token', newToken, 1) // save the newly refreshed token for other requests to use
			isAlreadyFetchingAccessToken = false
			onAccessTokenFetched(newToken)
		}
		return retryOriginalRequest
	} catch (err) {
		return Promise.reject(err)
	}
}

function isTokenExpiredError(errorResponse) {
	// Your own logic to determine if the error is due to JWT token expired returns a boolean value
	return true
}

customAxios.interceptors.response.use(
	function (response) {
		// If the request succeeds, we don't have to do anything and just return the response
		return response
	},
	function (error) {
		const errorResponse = error.response
		if (isTokenExpiredError(errorResponse)) {
			return refreshTokenAndReattemptRequest(error)
		}
		// If the error is due to other reasons, we just throw it back to axios
		return Promise.reject(error)
	}
)
