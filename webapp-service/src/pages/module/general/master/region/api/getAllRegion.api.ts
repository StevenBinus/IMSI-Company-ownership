import { ResponseProps, getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface RegionListProps {
	region_id: number
	region_code: string
	region_name: string
	is_active: boolean
}

export async function getAllRegion(
	page: number,
	limit: number,
	query_of?: string[],
	query_by?: string[]
): Promise<ResponseProps<RegionListProps[]>> {
	return (
		await getApiInstance().get(
			`/general-service/api/general/region?page=${page}&limit=${limit}${
				query_by ? `&query_by=${query_by}` : ''
			}${query_of ? `&query_of=${query_of}` : ''}`
		)
	).data

	// await sleep(1e3)
	// return [
	// 	{
	// 		region_id: 1,
	// 		region_code: 'A01',
	// 		region_name: 'Jabodetabek',
	// 		is_active: true,
	// 	},
	// 	{
	// 		region_id: 2,
	// 		region_code: 'H01',
	// 		region_name: 'HINO JAKARTA',
	// 		is_active: true,
	// 	},
	// ]
}
