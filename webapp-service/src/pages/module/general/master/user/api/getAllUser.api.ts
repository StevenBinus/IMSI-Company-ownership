import { sleep } from '@utils/test.util'

export interface UserListProps {
	user_id: number
	NIK: string
	user_name: string
	user_position: string
	is_active: boolean
}

export async function getAllUser() {
	await sleep(1e3)
	return [
		{
			user_id: 1,
			NIK: '50088',
			user_name: 'Ariestiana',
			user_position: '	Corporate Legal Div Head',
			is_active: true,
		},
		{
			user_id: 2,
			NIK: '50141',
			user_name: 'Ngatino',
			user_position: 'HRGA Officer',
			is_active: true,
		},
	]
}
