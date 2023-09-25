import { sleep } from '@utils/test.util'

export async function getCompanyOwnershipById(company_ownership_type: string) {
	await sleep(1e3)
	if (company_ownership_type === 'string') {
		return {
			company_ownership_id: 1,
			company_ownership_type: 'string',
			company_ownership_name: 'string',
			is_active: true,
		}
	}

	return null
}
