import { ResponseProps, getApiInstance } from '@utils/api.util'

export interface SPMRegisterRequestProps {
	company_id: number
	spm_received_by: string
	spm_received_date: string
	spm_number_format: string
	spm_number_from: number
	total_spm: number
	reference_document_number: string
}

export interface SPMRegisterResponseProps {
	register_system_number: number
}

export async function postSPMRegister(
	data: SPMRegisterRequestProps
): Promise<ResponseProps<SPMRegisterResponseProps>> {
	return (
		await getApiInstance().post(
			`sales-service/api/sales/preprinted-spm-register`,
			{
				company_id: data.company_id,
				spm_received_by: data.spm_received_by,
				spm_received_date: data.spm_received_date,
				spm_number_format: data.spm_number_format,
				spm_number_from: data.spm_number_from,
				total_spm: data.total_spm,
				reference_document_number: data.reference_document_number,
			}
		)
	).data
}
