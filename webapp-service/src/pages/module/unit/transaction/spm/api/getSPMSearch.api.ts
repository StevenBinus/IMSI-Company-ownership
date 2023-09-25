import { ResponseProps, getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface SPMProps {
	spm_number: number
	sales_rep: string
	spm_date: string
	order_name: string
	variant: string
	qty: number
	approval_status: string
	allocated_by: string
	approval_remark: string
}

export async function getSPMSearch(
	page: number,
	limit: number,
	sales_rep?: string,
	spm_date?: string,
	brand?: string,
	model?: string,
	variant?: string,
	spm_doc_no?: string,
	keyword?: string
): Promise<ResponseProps<SPMProps[]>> {
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
				sales_rep: '1',
				spm_date: '1',
				order_name: '1',
				variant: '1',
				qty: 1,
				approval_status: '1',
				allocated_by: '1',
				approval_remark: '1',
			},
			{
				spm_number: 2,
				sales_rep: '2',
				spm_date: '2',
				order_name: '2',
				variant: '2',
				qty: 2,
				approval_status: '2',
				allocated_by: '2',
				approval_remark: '2',
			},
		],
	}
}

// export async function getSPMSearch(
// 	page: number,
// 	limit: number,
// 	register_batch_no?: string,
// 	received_by?: string,
// 	received_date_from?: string,
// 	received_date_to?: string,
// 	spm_form_format?: string,
// 	start_spm_seq?: number,
// 	total_spm_form?: number
// ): Promise<ResponseProps<SPMProps[]>> {
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
