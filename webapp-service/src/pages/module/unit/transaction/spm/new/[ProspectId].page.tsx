import DatePickerDMS from '@components/DatePickerDMS.component'
import DropDownListDMS from '@components/DropDownListDMS.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import TextFieldLookUpDMS from '@components/TextFieldLookUpDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import { Box, Button, Grid, useTheme } from '@mui/material'
import LockOpenIcon from '@mui/icons-material/LockOpen'
import { useRouter } from 'next/router'

const SPMTransactionNewDetailPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const { ProspectId } = router.query
	const handleBackButton = () => {
		router.push('/module/unit/transaction/spm/new')
	}
	const handleNewButton = () => {
		router.push('/module/unit/transaction/spm/new')
	}
	return (
		<>
			<PageLoad loading={false} />
			<ToolbarTransaction
				handleBackButton={handleBackButton}
				handleNewButton={handleNewButton}
				DisableNextButton
				DisablePrintButton
				DisableCloseOrderButton
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
						<TextFieldDMS id='sales_rep' label={<span>Sales Rep.</span>} />
						<TextFieldDMS
							disabled
							id='SPM_doc_no'
							value={ProspectId}
							label={<span>SPM Doc. No.</span>}
						/>
						<DatePickerDMS
							id='SPM_date'
							label={<span>SPM Date</span>}
							date={null}
						/>
						<TextFieldLookUpDMS
							id='SPM_code'
							label={<span>SPM Code</span>}
							dataColumn={[]}
							dataRow={[]}
							handleDataRowId={() => {
								return 1
							}}
							handleOnDoubleClick={() => {}}
							handleOnBlur={() => {}}
							hideDescriptionValue
							listModal={false}
							handleCloseListModal={function (): void {
								throw new Error('Function not implemented.')
							}}
							handleOpenListModal={function (): void {
								throw new Error('Function not implemented.')
							}}
						/>
						<TextFieldLookUpDMS
							id='customer_code'
							label={<span>Customer Code</span>}
							dataColumn={[]}
							dataRow={[]}
							handleDataRowId={() => {
								return 1
							}}
							handleOnDoubleClick={() => {}}
							handleOnBlur={() => {}}
							hideDescriptionValue
							listModal={false}
							handleCloseListModal={function (): void {
								throw new Error('Function not implemented.')
							}}
							handleOpenListModal={function (): void {
								throw new Error('Function not implemented.')
							}}
						/>
					</Grid>
				</Grid>

				<Grid
					container
					sx={{
						padding: '2% 12%',
						margin: '0 2% 2% 2%',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Grid container item maxWidth='1000px'>
						<TextFieldDMS id='title_prefix' label={<span>Title Prefix</span>} />
						<TextFieldDMS id='SPM_name' label={<span>SPM Name</span>} />
						<TextFieldDMS id='title_suffix' label={<span>Title Suffix</span>} />
						<DropDownListDMS
							id='SPM_gender'
							label={<span>SPM Gender</span>}
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
							id='SPM_type'
							label={<span>SPM Type</span>}
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
							id='SPM_source'
							label={<span>SPM Source</span>}
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
								startIcon={<LockOpenIcon />}
							>
								Reactivate
							</Button>
						</Grid>
					</Grid>
				</Grid>
			</Grid>
		</>
	)
}

export default SPMTransactionNewDetailPage
