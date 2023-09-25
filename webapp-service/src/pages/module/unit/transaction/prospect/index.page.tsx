import DataGridDMS from '@components/DataGridDMS.component'
import DateRangePickerDMS from '@components/DateRangePickerDMS.component'
import DropDownListDMS from '@components/DropDownListDMS.component'
import PageLoad from '@components/PageLoad.component'
import RadioButtonDMS from '@components/RadioButtonDMS.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import { Box, Button, Grid, Typography, useTheme } from '@mui/material'
import { GridColDef } from '@mui/x-data-grid'
import SearchIcon from '@mui/icons-material/Search'
import { useRouter } from 'next/router'
import { useState } from 'react'
import { ProspectListProps, getAllProspect } from './api/getAllProspect.api'

const dataGridColumns: GridColDef[] = [
	{
		field: 'sales_name',
		headerName: 'Sales Name',
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
		field: 'last_stage',
		headerName: 'Last Stage',
		flex: 1,
	},
	{
		field: 'age',
		headerName: 'Age',
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
	{
		field: 'status',
		headerName: 'Status',
		flex: 1,
	},
]

const ProspectTransactionPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const [searchTableData, setSearchTableData] = useState([])
	const [isLoading, setIsLoading] = useState(false)

	const handleNewButton = () => {
		router.push(`/module/unit/transaction/prospect/new`)
	}

	const handleOnDoubleClick = (id: number) => {
		router.push(`/module/unit/transaction/prospect/${id}`)
	}

	const handleSearchButton = async () => {
		setIsLoading(true)
		const result = await getAllProspect()
		setSearchTableData(result)
		setIsLoading(false)
	}
	return (
		<>
			<PageLoad loading={isLoading} />
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
							id='prospect_date'
							label={<span>Prospect Date</span>}
							dateTo={null}
							dateFrom={null}
						/>
						<TextFieldDMS
							id='prospect_name'
							label={<span>Prospect Name</span>}
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
						<RadioButtonDMS
							row
							id='prospect_status'
							label={<span>Prospect Status</span>}
							listValue={[
								{ value: 'All', label: 'All' },
								{ value: 'Active', label: 'Active' },
								{ value: 'Win', label: 'Win' },
								{ value: 'Drop', label: 'Drop' },
							]}
						/>
						<DropDownListDMS
							id='prospect_stage'
							label={<span>Prospect Stage</span>}
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
								onClick={handleSearchButton}
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
						padding: '2%',
						margin: '0 2% 2% 2%',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Grid
						item
						container
						sx={{
							height: '310px',
						}}
					>
						<DataGridDMS
							pageSize={5}
							getRowId={(row: ProspectListProps) => {
								return row.prospect_no
							}}
							onRowDoubleClick={(data) => handleOnDoubleClick(data.row.value)}
							columns={dataGridColumns}
							rows={searchTableData}
						/>
					</Grid>
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={12}>
							<Typography>
								Untuk stage blank, &apos;CC&apos; dan &apos;CH`&apos; :
							</Typography>
						</Grid>
					</Grid>
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={1}>
							<Box
								sx={{
									width: '40px',
									aspectRatio: '2/1',
									backgroundColor: 'white',
									border: '1px solid black',
								}}
							/>
						</Grid>
						<Grid item xs={11}>
							<Typography>
								Follow Up Date &lt;= 7 Days; or Prospect Status = Win
							</Typography>
						</Grid>
					</Grid>
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={1}>
							<Box
								sx={{
									width: '40px',
									aspectRatio: '2/1',
									backgroundColor: 'yellow',
									border: '1px solid black',
								}}
							/>
						</Grid>
						<Grid item xs={11}>
							<Typography>Follow Up Date &gt; 7 Days</Typography>
						</Grid>
					</Grid>
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={1}>
							<Box
								sx={{
									width: '40px',
									aspectRatio: '2/1',
									backgroundColor: 'red',
									border: '1px solid black',
								}}
							/>
						</Grid>
						<Grid item xs={11}>
							<Typography>Follow Up Date &gt; 14 Days</Typography>
						</Grid>
					</Grid>
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={12}>
							<Typography>
								Untuk stage &apos;P&apos;,&apos;HP&apos;, dan &apos;DO&apos; :
							</Typography>
						</Grid>
					</Grid>
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={1}>
							<Box
								sx={{
									width: '40px',
									aspectRatio: '2/1',
									backgroundColor: 'blue',
									color: 'white',
									border: '1px solid black',
								}}
							>
								XX
							</Box>
						</Grid>
						<Grid item xs={11}>
							<Typography>
								Follow Up Date &lt;= 7 Days; or Prospect Status = Win
							</Typography>
						</Grid>
					</Grid>
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={1}>
							<Box
								sx={{
									width: '40px',
									aspectRatio: '2/1',
									backgroundColor: 'blue',
									color: 'yellow',
									border: '1px solid black',
								}}
							>
								XX
							</Box>
						</Grid>
						<Grid item xs={11}>
							<Typography>Follow Up Date &gt; 7 Days</Typography>
						</Grid>
					</Grid>
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={1}>
							<Box
								sx={{
									width: '40px',
									aspectRatio: '2/1',
									backgroundColor: 'blue',
									color: 'red',
									border: '1px solid black',
								}}
							>
								XX
							</Box>
						</Grid>
						<Grid item xs={11}>
							<Typography>Follow Up Date &gt; 14 Days</Typography>
						</Grid>
					</Grid>
				</Grid>
			</Grid>
		</>
	)
}

export default ProspectTransactionPage
