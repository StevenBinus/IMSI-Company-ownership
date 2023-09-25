import { sleep } from '@utils/test.util'

export interface UserProps {
	user_id: number
	NIK: string
	user_name: string
	position: string
	is_active: boolean
}

export async function getUserById(user_id: number) {
	await sleep(1e3)
	if (user_id === 1) {
		return {
			user_id: 1,
			NIK: '50088',
			user_name: 'Ariestiana',
			position: '	Corporate Legal Div Head',
			is_active: true,
		}
	}
	if (user_id === 2) {
		return {
			user_id: 2,
			NIK: '50141',
			user_name: 'Ngatino',
			user_position: 'HRGA Officer',
			is_active: true,
		}
	}

	return null
}
