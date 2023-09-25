import { sleep } from '@utils/test.util'

export interface CashFlowCodeListProps {
	cash_flow_code_id: number
	cash_flow_code: string
	cash_flow_type: string
	cash_flow_group: string
	cash_flow_group_detail: string
}

export async function getAllCashFlowCode() {
	await sleep(1e3)
	return [
		{
			cash_flow_code_id: 1,
			cash_flow_code: 'string',
			cash_flow_type: 'string',
			cash_flow_group: 'string',
			cash_flow_group_detail: 'string',
		},
		{
			cash_flow_code_id: 2,
			cash_flow_code: 'strong',
			cash_flow_type: 'strong',
			cash_flow_group: 'strong',
			cash_flow_group_detail: 'strong',
		},
		{
			cash_flow_code_id: 3,
			cash_flow_code: 'string',
			cash_flow_type: 'string',
			cash_flow_group: 'string',
			cash_flow_group_detail: 'string',
		},
		{
			cash_flow_code_id: 4,
			cash_flow_code: 'strong',
			cash_flow_type: 'strong',
			cash_flow_group: 'strong',
			cash_flow_group_detail: 'strong',
		},
		{
			cash_flow_code_id: 5,
			cash_flow_code: 'string',
			cash_flow_type: 'string',
			cash_flow_group: 'string',
			cash_flow_group_detail: 'string',
		},
		{
			cash_flow_code_id: 6,
			cash_flow_code: 'strong',
			cash_flow_type: 'strong',
			cash_flow_group: 'strong',
			cash_flow_group_detail: 'strong',
		},
	]
}
