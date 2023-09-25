import { sleep } from '@utils/test.util'

export async function getMenuCheck() {
	await sleep(1e3)
	return [
		'/dashboard',
		'/module/general/master/region',
		'/module/general/master/area',
		'/module/general/master/storage-type',
		'/module/general/master/term-of-payment',
		'/module/general/master/company-ownership',
		'/module/finance/master/general-ledger/cash-flow-code',
		'/module/general/report/print-form',

		'/module/finance/transaction/account-receivable/unit-invoice',
		'/module/unit/transaction/unit-allocation',
		'/module/unit/transaction/prospect',
		'/module/unit/transaction/spm',
		'/module/unit/transaction/preprinted-spm-register',
		'/module/unit/transaction/preprinted-spm-take',
	]
}
