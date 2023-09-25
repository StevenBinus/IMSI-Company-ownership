import { sleep } from '@utils/test.util'

export async function getAreaByCode(sales_area_code: string) {
	await sleep(1e3)
	if (sales_area_code === '001') {
		return {
			area_id: 1,
			sales_area_code: '001',
			area_description: 'Bali',
			region_id: 3,
			region_code: 'R03',
			region_name: 'SULAWESI',
			is_active: true,
		}
	}
	if (sales_area_code === '002') {
		return {
			area_id: 2,
			sales_area_code: '002',
			area_description: 'Banten',
			region_id: 2,
			region_code: 'R02',
			region_name: 'JAWA, BALI, NTB, SULAWESI & KUPANG',
			is_active: true,
		}
	}

	return null
}
