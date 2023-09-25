import { ResponseProps, getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface DashboardProps {
	document_id: number
	document_number: string
	document_date: string
	document_user: string
	tax_invoice_number: string
}

export async function getDashboardSearch(
	page: number,
	limit: number,
	unit_module?: boolean,
	after_sales_module?: boolean,
	finance_module?: boolean,
	form_name?: string,
	document_date_from?: string,
	document_date_to?: string,
	document_number?: string,
	document_user?: string,
	brand_id?: number,
	profit_center_id?: number
) {
	await sleep(1e3)
	return {
		status_code: 200,
		message: 'success',
		page_limit: 1,
		page: 0,
		total_rows: 1,
		total_pages: 1,
		data: [
			{
				document_id: 1,
				document_number: 'string',
				document_date: 'string',
				document_user: 'string',
				tax_invoice_number: 'string',
			},
			{
				document_id: 2,
				document_number: 'strong',
				document_date: 'strong',
				document_user: 'strong',
				tax_invoice_number: 'strong',
			},
		],
	}
}

// export async function getDashboardSearch(
// 	page: number,
// 	limit: number,
// 	unit_module?: boolean,
// 	after_sales_module?: boolean,
// 	finance_module?: boolean,
// 	form_name?: string,
// 	document_date_from?: string,
// 	document_date_to?: string,
// 	document_number?: string,
// 	document_user?: string,
// 	brand?: number,
// 	profit_center?: number
// ): Promise<ResponseProps<DashboardProps[]>> {
// 	return (
// 		await getApiInstance().get(
// 			`sales-service/api/sales/preprinted-spm-register-search?page=${page}&limit=${limit}`
// 		)
// 	).data
// }
