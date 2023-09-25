import DatePickerDMS from '@components/DatePickerDMS.component'
import DropDownListDMS from '@components/DropDownListDMS.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import TextFieldLookUpDMS from '@components/TextFieldLookUpDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import { Box, Button } from '@mui/material'
import LockOpenIcon from '@mui/icons-material/LockOpen'
import ProspectDetailCustomer from './ProspectDetailCustomer.component'
import ProspectDetailDrop from './ProspectDetailDrop.component'
import ProspectDetailFinancing from './ProspectDetailFinancing.component'
import ProspectDetailFollowUp from './ProspectDetailFollowUp.component'
import ProspectDetailOther from './ProspectDetailOther.component'
import ProspectDetailStage from './ProspectDetailStage.component'
import ProspectDetailVehicle from './ProspectDetailVehicle.components'
import FileSaver from 'file-saver'

type ProspectDetailProps = {
	prospectId?: number
	handleBackButton: () => void
}

const ProspectDetail = (props: ProspectDetailProps) => {
	return (
		<>
			<PageLoad loading={false} />
			<ToolbarTransaction handleBackButton={props.handleBackButton} />
			<Box sx={{ maxWidth: '540px', padding: '1%' }}>
				<TextFieldDMS id='sales_rep' label={<span>Sales Rep.</span>} />
				<TextFieldDMS
					disabled
					id='prospect_doc_no'
					value={props.prospectId}
					label={<span>Prospect Doc. No.</span>}
				/>
				<DatePickerDMS
					id='prospect_date'
					label={<span>Prospect Date</span>}
					date={null}
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
			</Box>

			<Box sx={{ maxWidth: '540px', padding: '1%' }}>
				<TextFieldDMS id='title_prefix' label={<span>Title Prefix</span>} />
				<TextFieldDMS id='prospect_name' label={<span>Prospect Name</span>} />
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
					isOptionEqualToValue={function (option: any, value: any): boolean {
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
					isOptionEqualToValue={function (option: any, value: any): boolean {
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
					isOptionEqualToValue={function (option: any, value: any): boolean {
						throw new Error('Function not implemented.')
					}}
				/>
				<TextFieldDMS id='search_keyword' label={<span>Search Keyword</span>} />
			</Box>
			<ProspectDetailCustomer />
			<ProspectDetailVehicle />
			<ProspectDetailFinancing />
			<ProspectDetailOther />
			<ProspectDetailFollowUp />
			<ProspectDetailStage />
			<ProspectDetailDrop />
			<Button
				onClick={() => {}}
				variant='contained'
				startIcon={<LockOpenIcon />}
			>
				Reactivate
			</Button>
		</>
	)
}

export default ProspectDetail
