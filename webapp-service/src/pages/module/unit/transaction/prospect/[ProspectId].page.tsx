import DatePickerDMS from '@components/DatePickerDMS.component'
import DropDownListDMS from '@components/DropDownListDMS.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import TextFieldLookUpDMS from '@components/TextFieldLookUpDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import { Box, Button, Grid, useTheme } from '@mui/material'
import LockOpenIcon from '@mui/icons-material/LockOpen'
import { useRouter } from 'next/router'
import ProspectDetailCustomer from './component/ProspectDetailCustomer.component'
import ProspectDetailVehicle from './component/ProspectDetailVehicle.components'
import ProspectDetailFinancing from './component/ProspectDetailFinancing.component'
import ProspectDetailOther from './component/ProspectDetailOther.component'
import ProspectDetailFollowUp from './component/ProspectDetailFollowUp.component'
import ProspectDetailStage from './component/ProspectDetailStage.component'
import ProspectDetailDrop from './component/ProspectDetailDrop.component'

const ProspectTransactionDetailPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const { ProspectId } = router.query

	const handleBackButton = () => {
		router.push(`/module/unit/transaction/prospect`)
	}

	const handleSaveButton = () => {}

	return (
		<>
			<PageLoad loading={false} />
			<ToolbarTransaction
				handleBackButton={handleBackButton}
				handleSaveButton={handleSaveButton}
				DisableCloseOrderButton
				DisableNextButton
				DisableNewButton
				DisablePrintButton
				DisableSubmitButton
				DisableVoidButton
			/>
			<Grid
				container
				item
				justifyContent='center'
				alignItems='center'
				direction='column'
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
							id='prospect_doc_no'
							value={ProspectId}
							label={<span>Prospect Doc. No.</span>}
						/>
						<DatePickerDMS
							id='prospect_date'
							label={<span>Prospect Date</span>}
							date={null}
							disableFuture
						/>
						<TextFieldLookUpDMS
							id='prospect_code'
							label={<span>Prospect Code</span>}
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
						<TextFieldDMS
							id='prospect_name'
							label={<span>Prospect Name</span>}
						/>
						<TextFieldDMS id='title_suffix' label={<span>Title Suffix</span>} />
						<DropDownListDMS
							id='prospect_gender'
							label={<span>Prospect Gender</span>}
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
							id='prospect_type'
							label={<span>Prospect Type</span>}
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
							id='prospect_source'
							label={<span>Prospect Source</span>}
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
						<ProspectDetailCustomer />
						<ProspectDetailVehicle />
						<ProspectDetailFinancing />
						<ProspectDetailOther />
						<ProspectDetailFollowUp />
						<ProspectDetailStage />
						<ProspectDetailDrop />
						<Grid
							container
							justifyContent='flex-end'
							sx={{
								padding: '0 0 2% 0',
								borderRadius: '5px',
							}}
						>
							<Button
								disabled
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

export default ProspectTransactionDetailPage
