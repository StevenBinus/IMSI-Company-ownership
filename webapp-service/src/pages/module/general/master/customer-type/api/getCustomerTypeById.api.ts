import { sleep } from '@utils/test.util'

export async function getCustomerTypeById(customer_type: string) {
	await sleep(1e3)
	if (customer_type === 'string') {
		return {
			customer_type_id: 1,
			customer_type: 'string',
			customer_type_description: 'string',
			customer_type_flag: 'string',
			customer_type_group: 'string',
			bbn: true,
			police_invoice: true,
			spm: true,
			tax_free: true,
			is_active: true,
		}
	}

	return null
}
