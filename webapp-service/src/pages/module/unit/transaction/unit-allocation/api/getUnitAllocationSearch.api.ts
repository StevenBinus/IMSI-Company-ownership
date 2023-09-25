import { ResponseProps, getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface UnitAllocationProps {
	spm_number: number
	spm_date: string
	corporate_purchase_order_no: string
	order_by: string
	spm_received_date: string
	allocated_chassis_no: string
	allocated_date: string
	allocated_by: string
	action: string
	vehicle_desc: string
	engine_no: string
	customer_purchase_order: string
}

export async function getUnitAllocationSearch(
	page: number,
	limit: number,
	register_batch_no?: string,
	received_by?: string,
	received_date_from?: string,
	received_date_to?: string,
	spm_form_format?: string,
	start_spm_seq?: number,
	total_spm_form?: number
): Promise<ResponseProps<UnitAllocationProps[]>> {
	return {
		status_code: 200,
		message: 'success',
		page_limit: 10,
		page: 0,
		total_rows: 15,
		total_pages: 1,
		data: [
			{
				spm_number: 1,
				spm_date: '1',
				corporate_purchase_order_no: '1',
				order_by: '1',
				spm_received_date: '1',
				allocated_chassis_no: '1',
				allocated_date: '1',
				allocated_by: '1',
				action: 'Allocate',
				vehicle_desc: '1',
				engine_no: '1',
				customer_purchase_order: '1',
			},
			{
				spm_number: 2,
				spm_date: '2',
				corporate_purchase_order_no: '2',
				order_by: '2',
				spm_received_date: '2',
				allocated_chassis_no: '2',
				allocated_date: '2',
				allocated_by: '2',
				action: 'Deallocate',
				vehicle_desc: '2',
				engine_no: '2',
				customer_purchase_order: '2',
			},
		],
	}
}

// export async function getUnitAllocationSearch(
// 	page: number,
// 	limit: number,
// 	register_batch_no?: string,
// 	received_by?: string,
// 	received_date_from?: string,
// 	received_date_to?: string,
// 	spm_form_format?: string,
// 	start_spm_seq?: number,
// 	total_spm_form?: number
// ): Promise<ResponseProps<UnitAllocationProps[]>> {
// 	return (
// 		await getApiInstance().get(
// 			`sales-service/api/sales/preprinted-spm-register-search?page=${page}&limit=${limit}${
// 				register_batch_no ? `&register_batch_no=${register_batch_no}` : ''
// 			}${received_by ? `&received_by=${received_by}` : ''}${
// 				received_date_from ? `&received_date_from=${received_date_from}` : ''
// 			}${received_date_to ? `&received_date_to=${received_date_to}` : ''}${
// 				spm_form_format ? `&spm_form_format=${spm_form_format}` : ''
// 			}${start_spm_seq ? `&start_spm_seq=${start_spm_seq}` : ''}${
// 				total_spm_form ? `&total_spm_form=${total_spm_form}` : ''
// 			}`
// 		)
// 	).data
// }
