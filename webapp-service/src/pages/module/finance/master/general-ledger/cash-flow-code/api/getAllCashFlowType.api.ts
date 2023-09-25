import { sleep } from '@utils/test.util'
import useSWR from 'swr'

export interface CashFlowTypeProps {
	cash_flow_type_id: number
	cash_flow_type: string
}

export const CashFlowTypeKey = 'CashFlowType'

async function getAllCashFlowType(): Promise<CashFlowTypeProps[]> {
	await sleep(1e3)
	return [
		{
			cash_flow_type_id: 1,
			cash_flow_type: 'tempe - duer',
		},
		{
			cash_flow_type_id: 2,
			cash_flow_type: 'tempo - duar',
		},
	]
}

export function useGetAllCashFlowType() {
	const { data, error, isLoading } = useSWR(CashFlowTypeKey, getAllCashFlowType)
	return {
		dataCashFlowType: data,
		isLoadingCashFlowType: isLoading,
		isErrorCashFlowType: error,
	}
}
