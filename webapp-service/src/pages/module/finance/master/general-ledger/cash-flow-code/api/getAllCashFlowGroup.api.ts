import { sleep } from '@utils/test.util'
import useSWR from 'swr'

export interface CashFlowGroupProps {
	cash_flow_group_id: number
	cash_flow_group: string
}

export const CashFlowGroupKey = 'CashFlowGroup'

async function getAllCashFlowGroup(): Promise<CashFlowGroupProps[]> {
	await sleep(1e3)
	return [
		{
			cash_flow_group_id: 1,
			cash_flow_group: 'tempe - duer',
		},
		{
			cash_flow_group_id: 2,
			cash_flow_group: 'tempo - duar',
		},
	]
}

export function useGetAllCashFlowGroup() {
	const { data, error, isLoading } = useSWR(
		CashFlowGroupKey,
		getAllCashFlowGroup
	)
	return {
		dataCashFlowGroup: data,
		isLoadingCashFlowGroup: isLoading,
		isErrorCashFlowGroup: error,
	}
}
