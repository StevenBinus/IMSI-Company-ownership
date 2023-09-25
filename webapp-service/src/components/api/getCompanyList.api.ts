import { sleep } from '@utils/test.util'
import useSWR from 'swr'

export interface Usercompany {
	company_id: number
	company_name: string
}

export const CompanyListKey = 'CompanyList'

async function getCompanyList(): Promise<Usercompany[]> {
	await sleep(1e3)
	return [
		{
			company_name: 'Indomobil Trada Nasional - Halim',
			company_id: 1,
		},
		{
			company_name: 'Indomobil Trada Nasional - Bogor',
			company_id: 2,
		},
		{
			company_name: 'Indomobil Trada Nasional - Cikarang',
			company_id: 3,
		},
		{ company_name: 'Indomobil Sompo Japan', company_id: 4 },
		{
			company_name: 'Indomobil Trada Nasional - Pluit',
			company_id: 5,
		},
		{ company_name: 'Wangsa Indra Permana - BSD', company_id: 6 },
		{
			company_name: 'Indomobil Trada Nasional - Bekasi',
			company_id: 7,
		},
		{
			company_name: 'Wahana Trans Lestari Medan - Adam Malik Datsun',
			company_id: 8,
		},
	]
}

export function useGetCompanyList() {
	const { data, error, isLoading } = useSWR(CompanyListKey, getCompanyList)
	return {
		dataCompanyList: data,
		isLoadingCompanyListData: isLoading,
		isErrorCompanyListData: error,
	}
}
