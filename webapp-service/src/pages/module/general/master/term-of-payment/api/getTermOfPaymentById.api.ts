import { sleep } from '@utils/test.util'

export async function getTermOfPaymentById(term_of_payment_code: string) {
	await sleep(1e3)
	if (term_of_payment_code === 'string') {
		return {
			term_of_payment_id: 1,
			term_of_payment_code: 'string',
			term_of_payment_name: 'string',
			term_of_payment_installment: 1,
			term_of_payment_interval: 1,
			term_of_payment_policy: 'string',
			is_active: true,
		}
	}

	return null
}
