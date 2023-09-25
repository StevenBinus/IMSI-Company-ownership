import { sleep } from '@utils/test.util'

export interface RegionProps {
	region_id: number
	region_code: string
	region_name: string
	user_id: number
	NIK: string
	user_name: string
	is_active: boolean
}

export async function getRegionById(region_id: number) {
	await sleep(1e3)
	if (region_id === 1) {
		return {
			region_id: 1,
			region_code: 'A01',
			region_name: 'Jabodetabek',
			user_id: 1,
			NIK: '90464',
			user_name: 'Andrew Nasuri',
			is_active: true,
		}
	}

	return null
}
