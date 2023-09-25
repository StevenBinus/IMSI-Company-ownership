import { ResponseProps, getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface AreaProps {
	area_id: number
	area_code: string
	description: string
	region_id: number
	region_code: string
	region_name: string
	is_active: boolean
}

// export async function getAreaById(area_id: number) {
// 	await sleep(1e3)
// 	if (area_id === 1) {
// 		return {
// 			area_id: 1,
// 			sales_area_code: '001',
// 			area_description: 'Bali',
// 			region_id: 3,
// 			region_code: 'R03',
// 			region_name: 'SULAWESI',
// 			is_active: true,
// 		}
// 	}
// 	if (area_id === 2) {
// 		return {
// 			area_id: 2,
// 			sales_area_code: '002',
// 			area_description: 'Banten',
// 			region_id: 2,
// 			region_code: 'R02',
// 			region_name: 'JAWA, BALI, NTB, SULAWESI & KUPANG',
// 			is_active: true,
// 		}
// 	}

// 	return null
// }

export async function getAreaById(
	area_id: number
): Promise<ResponseProps<AreaProps>> {
	return (
		await getApiInstance().get(`/general-service/api/general/area/${area_id}`)
	).data
}
