import { sleep } from '@utils/test.util'

export interface CompanyOwnershipProps {
	company_ownership_id: number
	company_ownership_type: string
	company_ownership_name: string
	is_active: boolean
}

export async function getAllCompanyOwnership() {
	await sleep(1e3)
	return [
		{
			company_ownership_id: 1,
			company_ownership_type: 'string',
			company_ownership_name: 'string',
			is_active: true,
		},
		{
			company_ownership_id: 2,
			company_ownership_type: 'strong',
			company_ownership_name: 'strong',
			is_active: false,
		},
	]
}
