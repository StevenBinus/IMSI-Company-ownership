import DataGridDMS from '@components/DataGridDMS.component'
import DateRangePickerDMS from '@components/DateRangePickerDMS.component'
import DropDownListDMS from '@components/DropDownListDMS.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import { Box, Button, Grid, useTheme } from '@mui/material'
import { GridColDef } from '@mui/x-data-grid'
import SearchIcon from '@mui/icons-material/Search'
import { useRouter } from 'next/router'

const dataGridColumns: GridColDef[] = [
	{
		field: 'sales_rep',
		headerName: 'Sales Rep',
		flex: 1,
	},
	{
		field: 'prospect_no',
		headerName: 'Prospect No.',
		flex: 1,
	},
	{
		field: 'prospect_date',
		headerName: 'Prospect Date',
		flex: 1,
	},
	{
		field: 'prospect_name',
		headerName: 'Prospect Name',
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
]

const SPMTransactionNewPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const handleBackButton = () => {
		router.push('/module/unit/transaction/spm')
	}
	const handleOnDoubleClick = (id: number) => {
		router.push(`/module/unit/transaction/spm/new/${id}`)
	}
	return (
		<>
			<PageLoad loading={false} />
			<ToolbarTransaction
				handleBackButton={handleBackButton}
				DisableCloseOrderButton
				DisableNextButton
				DisableNewButton
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

						<TextFieldDMS
							id='prospect_name'
							label={<span>Prospect Name</span>}
						/>
						<DateRangePickerDMS
							id='prospect_date'
							label={<span>Prospect Date</span>}
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

						<TextFieldDMS
							id='search_keyword'
							label={<span>Search Keyword</span>}
						/>
						<Grid container item justifyContent='flex-end'>
							<Button
								onClick={() => {}}
								variant='contained'
								startIcon={<SearchIcon />}
							>
								Search
							</Button>
						</Grid>
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

export default SPMTransactionNewPage
