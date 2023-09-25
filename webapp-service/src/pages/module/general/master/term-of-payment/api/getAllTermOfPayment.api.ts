import { sleep } from '@utils/test.util'

export interface TermOfPaymentProps {
	term_of_payment_id: number
	term_of_payment_code: string
	term_of_payment_name: string
	term_of_payment_installment: number
	term_of_payment_interval: number
	term_of_payment_policy: string
	is_active: boolean
}

export async function getAllTermOfPayment() {
	await sleep(1e3)
	return [
		{
			term_of_payment_id: 1,
			term_of_payment_code: 'string',
			term_of_payment_name: 'string',
			term_of_payment_installment: 1,
			term_of_payment_interval: 1,
			term_of_payment_policy: 'string',
			is_active: true,
		},
		{
			term_of_payment_id: 2,
			term_of_payment_code: 'strong',
			term_of_payment_name: 'strong',
			term_of_payment_installment: 1,
			term_of_payment_interval: 1,
			term_of_payment_policy: 'strong',
			is_active: true,
		},
	]
}
