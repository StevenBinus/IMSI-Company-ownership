import { sleep } from '@utils/test.util'
import useSWR from 'swr'

export interface CashFlowGroupDetailProps {
	cash_flow_group_detail_id: number
	cash_flow_group_detail: string
}

export const CashFlowGroupDetailKey = 'CashFlowGroupDetail'

async function getAllCashFlowGroupDetail(): Promise<
	CashFlowGroupDetailProps[]
> {
	await sleep(1e3)
	return [
		{
			cash_flow_group_detail_id: 1,
			cash_flow_group_detail: 'tempe - duer',
		},
		{
			cash_flow_group_detail_id: 2,
			cash_flow_group_detail: 'tempo - duar',
		},
	]
}

export function useGetAllCashFlowGroupDetail() {
	const { data, error, isLoading } = useSWR(
		CashFlowGroupDetailKey,
		getAllCashFlowGroupDetail
	)
	return {
		dataCashFlowGroupDetail: data,
		isLoadingCashFlowGroupDetail: isLoading,
		isErrorCashFlowGroupDetail: error,
	}
}
