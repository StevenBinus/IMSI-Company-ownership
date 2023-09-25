import { sleep } from '@utils/test.util'

export interface MenuRequestProps {
	title: string
	url?: string
	children?: MenuRequestProps[]
}

export const menu_list_data_dummy = [
	{
		title: 'Master',
		children: [
			{
				title: 'General',
				children: [
					{ title: 'Region', url: '/module/general/master/region' },
					{ title: 'Area', url: '/module/general/master/area' },
					{ title: 'Province', url: '/module/general/master/province' },
					{ title: 'Storage Type', url: '/module/general/master/storage-type' },
					{
						title: 'Term Of Payment',
						url: '/module/general/master/term-of-payment',
					},
					{
						title: 'Company Ownership',
						url: '/module/general/master/company-ownership',
					},
				],
			},
			{
				title: 'Unit',
				children: [
					{ title: 'TPT Master', url: '/module/unit/master/tpt-master' },
				],
			},
			{
				title: 'After Sales',
				children: [
					{
						title: 'Item',
						children: [
							{
								title: 'Item Class',
								url: '/module/after-sales/master/item/item-class',
							},
							{
								title: 'Unit of Measurement',
								url: '/module/after-sales/master/item/unit-of-measurement',
							},
						],
					},
				],
			},

			{
				title: 'Finance',
				children: [
					{
						title: 'Currency Code',
						url: '/module/finance/master/currency-code',
					},
					{
						title: 'Exchange Rate Type',
						url: '/module/finance/master/exchange-rate-type',
					},
					{
						title: 'Exchange Rate',
						url: '/module/finance/master/exchange-rate',
					},
					{
						title: 'General Ledger',
						children: [
							{
								title: 'Cash Flow Code',
								url: '/module/finance/master/general-ledger/cash-flow-code',
							},
						],
					},
				],
			},
		],
	},
	{
		title: 'Transaction',
		children: [
			{
				title: 'Unit',
				children: [
					{
						title: 'Preprinted SPM Register',
						url: '/module/unit/transaction/preprinted-spm-register',
					},
					{
						title: 'Preprinted SPM Take',
						url: '/module/unit/transaction/preprinted-spm-take',
					},
					{
						title: 'Unit Allocation',
						url: '/module/unit/transaction/unit-allocation',
					},
					{
						title: 'Prospect',
						url: '/module/unit/transaction/prospect',
					},
					{
						title: 'SPM',
						url: '/module/unit/transaction/spm',
					},
				],
			},
			{
				title: 'Finance',
				children: [
					{
						title: 'Account Receivable',
						children: [
							{
								title: 'Unit Invoice',
								url: '/module/finance/transaction/account-receivable/unit-invoice',
							},
						],
					},
				],
			},
		],
	},
	{
		title: 'Report',
		children: [
			{
				title: 'General',
				children: [
					{
						title: 'Print Form',
						url: '/module/general/report/print-form',
					},
				],
			},
		],
	},
]

export async function getMenu(): Promise<MenuRequestProps[]> {
	await sleep(1e3)
	return menu_list_data_dummy
}

// [
// 	{ title: 'General', url: '/module/general', parent: 'master' },
// 	{ title: 'Master', url: '/module/general/master', parent: null },
// 	{ title: 'Region', url: '/module/general/master/region', parent: 'general' },
// 	{ title: 'After Sales', url: '/module/aftersales/master', parent: 'master' },
// 	{ title: 'Item', url: '/module/aftersales/master/item', parent: 'aftersales' },
// 	{
// 		title: 'Item Class',
// 		url: '/module/aftersales/master/item/itemclass',
// 		parent: 'item',
// 	},
// ]
