import { ResponseProps, getApiInstance } from '@utils/api.util'
import { sleep } from '@utils/test.util'

export interface SPMRegisterDetailListProps {
	spm_form_registration_detail_id: number
	spm_document_number: string
}

export interface SPMRegisterDetailProps {
	company_id: number
	register_document_number: string
	spm_received_date: string
	spm_received_by: string
	spm_number_format: string
	spm_number_from: number
	total_spm: number
	list_spm: SPMRegisterDetailListProps[]
}

export async function getSPMRegisterDetail(
	spm_register_id: number
): Promise<ResponseProps<SPMRegisterDetailProps>> {
	return (
		await getApiInstance().get(
			`sales-service/api/sales/preprinted-spm-register/${spm_register_id}`
		)
	).data
}
