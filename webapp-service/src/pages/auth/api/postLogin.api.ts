import { SHA256 } from 'crypto-js/sha256'
import FingerprintJS from '@fingerprintjs/fingerprintjs'
import {
	MenuRequestProps,
	menu_list_data_dummy,
} from '@components/api/getMenu.api'
import { getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface LoginResponseProps {
	token: string
	refreshToken?: string
	menu_list: MenuRequestProps[]
	company: {
		company_name: string
		company_code: number
	}
}

export interface LoginRequestProps {
	password: string
	username: string
}

const createFingerprint = async () => {
	const fingerprintJS = await FingerprintJS.load()
	const { visitorId } = await fingerprintJS.get()
	return visitorId
}

// export async function postLogin(
// 	data: LoginRequestProps
// ): Promise<LoginResponseProps> {
// 	const hashedFingerprint = await createFingerprint()
// 	return await getApiInstance().post(`/api/auth/login`, {
// 		client: hashedFingerprint,
// 		username: data.username,
// 		password: data.password,
// 	})
// }

export async function postLogin(
	data: LoginRequestProps
): Promise<LoginResponseProps> {
	await sleep(1e3)
	return {
		token: 'string',
		refreshToken: 'string',
		menu_list: menu_list_data_dummy,
		company: {
			company_name: 'Indomobil Trada Nasional - Bekasi',
			company_code: 120000,
		},
	}
}
