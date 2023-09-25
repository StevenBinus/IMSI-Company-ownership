import { ResponseProps, getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface SPMRegisterProps {
	spm_register_no: number
	register_system_number: number
	batch_no: string
	spm_received_by: string
	spm_number_format: string
	spm_received_date: string
	spm_form_format: string
	spm_number_from: number
	start_sequence_no: string
}

export async function getSPMRegisterSearch(
	page: number,
	limit: number,
	register_batch_no?: string,
	received_by?: string,
	received_date_from?: string,
	received_date_to?: string,
	spm_form_format?: string,
	start_spm_seq?: number,
	total_spm_form?: number
): Promise<ResponseProps<SPMRegisterProps[]>> {
	return (
		await getApiInstance().get(
			`sales-service/api/sales/preprinted-spm-register-search?page=${page}&limit=${limit}${
				register_batch_no ? `&register_batch_no=${register_batch_no}` : ''
			}${received_by ? `&received_by=${received_by}` : ''}${
				received_date_from ? `&received_date_from=${received_date_from}` : ''
			}${received_date_to ? `&received_date_to=${received_date_to}` : ''}${
				spm_form_format ? `&spm_form_format=${spm_form_format}` : ''
			}${start_spm_seq ? `&start_spm_seq=${start_spm_seq}` : ''}${
				total_spm_form ? `&total_spm_form=${total_spm_form}` : ''
			}`
		)
	).data
}
