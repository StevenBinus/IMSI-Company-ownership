import { sleep } from '@utils/test.util'

export interface CashFlowCodeProps {
	cash_flow_code_id: number
	cash_flow_code: string
	cash_flow_code_description: string
	cash_flow_type_id: number
	cash_flow_group_id: number
	cash_flow_group_detail_id: number
	sequence_number: number
	is_active: boolean
}

export async function getCashFlowCodeById(cash_flow_code: string) {
	await sleep(1e3)
	if (cash_flow_code === 'string') {
		return {
			cash_flow_code_id: 1,
			cash_flow_code: 'string',
			cash_flow_code_description: 'string',
			cash_flow_type_id: 1,
			cash_flow_group_id: 1,
			cash_flow_group_detail_id: 1,
			sequence_number: 0,
			is_active: true,
		}
	}

	return null
}
