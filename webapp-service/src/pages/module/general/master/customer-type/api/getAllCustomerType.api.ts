import { sleep } from '@utils/test.util'

export interface CustomerTypeProps {
	customer_type_id: number
	customer_type: string
	customer_type_description: string
	customer_type_flag: string
	customer_type_group: string
	bbn: boolean
	police_invoice: boolean
	spm: boolean
	tax_free: boolean
	is_active: boolean
}

export async function getAllCustomerType() {
	await sleep(1e3)
	return [
		{
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
		},
		{
			customer_type_id: 2,
			customer_type: 'strong',
			customer_type_description: 'strong',
			customer_type_flag: 'strong',
			customer_type_group: 'strong',
			bbn: false,
			police_invoice: false,
			spm: false,
			tax_free: false,
			is_active: false,
		},
	]
}
