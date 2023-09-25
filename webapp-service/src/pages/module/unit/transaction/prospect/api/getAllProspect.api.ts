import { sleep } from '@utils/test.util'

export interface ProspectListProps {
	sales_name: number
	prospect_no: string
	prospect_date: string
	last_stage: string
	age: number
	prospect_name: string
	variant: string
	qty: number
	status: boolean
}

export async function getAllProspect() {
	await sleep(1e3)
	return [
		{
			sales_name: 1,
			prospect_no: 'string',
			prospect_date: 'string',
			last_stage: 'string',
			age: 1,
			prospect_name: 'string',
			variant: 'string',
			qty: 1,
			status: true,
		},
		{
			sales_name: 2,
			prospect_no: 'strong',
			prospect_date: 'strong',
			last_stage: 'strong',
			age: 2,
			prospect_name: 'strong',
			variant: 'strong',
			qty: 2,
			status: true,
		},
		{
			sales_name: 3,
			prospect_no: 'streng',
			prospect_date: 'streng',
			last_stage: 'streng',
			age: 3,
			prospect_name: 'streng',
			variant: 'streng',
			qty: 3,
			status: true,
		},
		{
			sales_name: 4,
			prospect_no: 'strung',
			prospect_date: 'strung',
			last_stage: 'strung',
			age: 4,
			prospect_name: 'strung',
			variant: 'strung',
			qty: 4,
			status: true,
		},
		{
			sales_name: 5,
			prospect_no: 'strang',
			prospect_date: 'strang',
			last_stage: 'strang',
			age: 5,
			prospect_name: 'strang',
			variant: 'strang',
			qty: 5,
			status: true,
		},
	]
}
