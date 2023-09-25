import DataGridDMS from '@components/DataGridDMS.component'
import DateRangePickerDMS from '@components/DateRangePickerDMS.component'
import DropDownListDMS from '@components/DropDownListDMS.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import { Box, Button, Grid, useTheme } from '@mui/material'
import { GridColDef, GridValueGetterParams } from '@mui/x-data-grid'
import SearchIcon from '@mui/icons-material/Search'
import { useRouter } from 'next/router'
import { SPMInfo } from './component/SPMInfo.component'

const dataGridColumns: GridColDef[] = [
	{
		field: 'sales_rep',
		headerName: 'Sales Rep',
		flex: 1,
	},
	{
		field: 'spm_no',
		headerName: 'SPM No.',
		flex: 1,
	},
	{
		field: 'spm_date',
		headerName: 'SPM Date',
		flex: 1,
	},
	{
		field: 'order_name',
		headerName: 'Order Name',
		flex: 1,
	},
	{
		field: 'variant',
		headerName: 'Variant',
		flex: 1,
	},
	{
		field: 'qty',
		headerName: 'Qty',
		flex: 1,
	},
	{
		field: 'approval_status',
		headerName: 'Approval Status',
		flex: 1,
	},
	{
		field: 'info',
		headerName: 'Info',
		flex: 1,
		renderCell: (params: GridValueGetterParams) => {
			return (
				<SPMInfo
					spm_number={params.row.spm_number}
					approval_by={params.row.approval_by}
					approval_remark={params.row.approval_remark}
				/>
			)
		},
	},
]

const SPMTransactionPage = () => {
	const theme = useTheme()
	const router = useRouter()

	const handleNewButton = () => {
		router.push('/module/unit/transaction/spm/new')
	}
	const handleOnDoubleClick = (id: number) => {
		router.push(`/module/unit/transaction/spm/${id}`)
	}

	return (
		<>
			<PageLoad loading={false} />
			<ToolbarTransaction
				handleNewButton={handleNewButton}
				DisableBackButton
				DisableCloseOrderButton
				DisableNextButton
				DisablePrintButton
				DisableSaveButton
				DisableSubmitButton
				DisableVoidButton
			/>
			<Grid
				container
				item
				alignItems='center'
				direction='column'
				sx={{ minHeight: '89.9vh' }}
			>
				<Grid
					container
					item
					sx={{
						padding: '2% 12%',
						margin: '2%',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Grid container item maxWidth='1000px'>
						<DropDownListDMS
							id='sales_representative'
							label={<span>Sales Representative</span>}
							optionData={[]}
							valueData={undefined}
							onChangeValueData={function (value: any): void {
								throw new Error('Function not implemented.')
							}}
							getOptionLabel={function (option: any): string {
								throw new Error('Function not implemented.')
							}}
							isOptionEqualToValue={function (
								option: any,
								value: any
							): boolean {
								throw new Error('Function not implemented.')
							}}
						/>
						<DateRangePickerDMS
							id='spm_date'
							label={<span>SPM Date</span>}
							dateTo={null}
							dateFrom={null}
						/>
						<DropDownListDMS
							id='brand'
							label={<span>Brand</span>}
							optionData={[]}
							valueData={undefined}
							onChangeValueData={function (value: any): void {
								throw new Error('Function not implemented.')
							}}
							getOptionLabel={function (option: any): string {
								throw new Error('Function not implemented.')
							}}
							isOptionEqualToValue={function (
								option: any,
								value: any
							): boolean {
								throw new Error('Function not implemented.')
							}}
						/>
						<DropDownListDMS
							id='model'
							label={<span>Model</span>}
							optionData={[]}
							valueData={undefined}
							onChangeValueData={function (value: any): void {
								throw new Error('Function not implemented.')
							}}
							getOptionLabel={function (option: any): string {
								throw new Error('Function not implemented.')
							}}
							isOptionEqualToValue={function (
								option: any,
								value: any
							): boolean {
								throw new Error('Function not implemented.')
							}}
						/>
						<DropDownListDMS
							id='variant'
							label={<span>Variant</span>}
							optionData={[]}
							valueData={undefined}
							onChangeValueData={function (value: any): void {
								throw new Error('Function not implemented.')
							}}
							getOptionLabel={function (option: any): string {
								throw new Error('Function not implemented.')
							}}
							isOptionEqualToValue={function (
								option: any,
								value: any
							): boolean {
								throw new Error('Function not implemented.')
							}}
						/>

						<TextFieldDMS id='spm_doc_no' label={<span>SPM Doc No.</span>} />
						<TextFieldDMS id='order_name' label={<span>Order Name</span>} />
						<TextFieldDMS
							id='search_keyword'
							label={<span>Search Keyword</span>}
						/>
						<Button
							onClick={() => {}}
							variant='contained'
							startIcon={<SearchIcon />}
						>
							Search
						</Button>
					</Grid>
				</Grid>
				<Grid
					container
					sx={{
						height: '310px',
						padding: '2%',
						margin: '0 2% 2% 2%',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Grid container item>
						<DataGridDMS
							pageSize={5}
							getRowId={(row: { value: string; label: string }) => {
								return row.value
							}}
							onRowDoubleClick={(data) => handleOnDoubleClick(data.row.value)}
							columns={dataGridColumns}
							rows={[]}
						/>
					</Grid>
				</Grid>
			</Grid>
		</>
	)
}

export default SPMTransactionPage
