import { sleep } from '@utils/test.util'

export async function getRegionByCode(region_code: string) {
	await sleep(1e3)
	if (region_code === 'A01') {
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
