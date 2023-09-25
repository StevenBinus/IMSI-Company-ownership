import { sleep } from '@utils/test.util'

export async function getUserByNIK(NIK: string) {
	await sleep(1e3)
	if (NIK === '50088') {
		return {
			user_id: 1,
			NIK: '50088',
			user_name: 'Ariestiana',
			position: '	Corporate Legal Div Head',
			is_active: true,
		}
	}
	if (NIK === '50141') {
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
