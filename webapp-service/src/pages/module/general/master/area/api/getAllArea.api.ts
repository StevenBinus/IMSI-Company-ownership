import { ResponseProps, getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface AreaListProps {
	area_id: number
	area_code: string
	description: string
	is_active: boolean
}

// export async function getAllArea() {
// 	await sleep(1e3)
// 	return [
// 		{
// 			area_id: 1,
// 			sales_area_code: '001',
// 			area_description: 'Bali',
// 			is_active: true,
// 		},
// 		{
// 			area_id: 2,
// 			sales_area_code: '002',
// 			area_description: 'Banten',
// 			is_active: true,
// 		},
// 	]
// }

export async function getAllArea(
	page: number,
	limit: number,
	query_of?: string,
	query_by?: string
): Promise<ResponseProps<AreaListProps[]>> {
	return (
		await getApiInstance().get(
			`/general-service/api/general/areas?page=${page}&limit=${limit}${
				query_by ? `&query_by=${query_by}` : ''
			}${query_of ? `&query_of=${query_of}` : ''}`
		)
	).data
}
