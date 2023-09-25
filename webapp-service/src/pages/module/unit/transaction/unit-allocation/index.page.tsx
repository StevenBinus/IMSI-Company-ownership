import DataGridDMS from '@components/DataGridDMS.component'
import DateRangePickerDMS from '@components/DateRangePickerDMS.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import {
	Box,
	Button,
	Grid,
	IconButton,
	Menu,
	MenuItem,
	Popover,
	Typography,
	useTheme,
} from '@mui/material'
import { GridColDef, GridValueGetterParams } from '@mui/x-data-grid'
import SearchIcon from '@mui/icons-material/Search'
import { useRouter } from 'next/router'
import { useRef, useState } from 'react'

import TextFieldLookUpDMS from '@components/TextFieldLookUpDMS.component'
import { useFormik } from 'formik'
import {
	UserListProps,
	getAllUser,
} from 'src/pages/module/general/master/user/api/getAllUser.api'
import { getUserById } from 'src/pages/module/general/master/user/api/getUserById'
import { getUserByNIK } from 'src/pages/module/general/master/user/api/getUserByNIK'
import { NumericFormat } from 'react-number-format'
import dayjs from 'dayjs'
import { AxiosError } from 'axios'
import {
	UnitAllocationProps,
	getUnitAllocationSearch,
} from './api/getUnitAllocationSearch.api'
import DropDownListDMS from '@components/DropDownListDMS.component'
import RadioButtonDMS from '@components/RadioButtonDMS.component'
import { UnitAllocationInfo } from './component/UnitAllocationInfo.component'
import ListModal from '@components/ListModal.component'

const dataGridColumnAllocation: GridColDef[] = [
	{
		field: 'location',
		headerName: 'Location',
		flex: 1,
	},
	{
		field: 'chassis_no',
		headerName: 'Chassis No',
		flex: 1,
	},
	{
		field: 'engine_no',
		headerName: 'Engine No',
		flex: 1,
	},
	{
		field: 'year',
		headerName: 'Year',
		flex: 1,
	},
	{
		field: 'aging',
		headerName: 'Aging',
		flex: 1,
	},
	{
		field: 'remark',
		headerName: 'Remark',
		flex: 1,
	},
]

const dataGridColumns: GridColDef[] = [
	{
		field: 'spm_number',
		headerName: 'SPM No.',
		flex: 1,
	},
	{
		field: 'spm_date',
		headerName: 'SPM Date',
		flex: 1,
	},
	{
		field: 'corporate_purchase_order_no',
		headerName: 'Corp PoNo  ',
		flex: 1,
	},
	{
		field: 'order_by',
		headerName: 'Order By Name',
		flex: 1,
	},
	{
		field: 'allocated_chassis_no',
		headerName: 'Allocated Chassis No.',
		flex: 1,
	},
	{
		field: 'allocated_date',
		headerName: 'Allocation Date',
		flex: 1,
	},
	{
		field: 'allocated_by',
		headerName: 'Allocation By',
		flex: 1,
	},
	{
		field: 'action',
		headerName: 'Action',
		flex: 1,
	},
	{
		field: 'info',
		headerName: 'Info',
		flex: 1,
		renderCell: (params: GridValueGetterParams) => {
			return (
				<UnitAllocationInfo
					spm_number={params.row.spm_number}
					vehicle_desc={params.row.vehicle_desc}
					engine_no={params.row.engine_no}
					customer_purchase_order={params.row.customer_purchase_order}
				/>
			)
		},
	},
]

const UnitAllocationPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const [searchTableData, setSearchTableData] = useState([])
	const [isLoading, setIsLoading] = useState(false)

	const [listModalAllocation, setListModalAllocation] = useState(false)
	const [dataRowModalAllocation, setDataRowModalAllocation] = useState([])
	const [ModalAllocationTotalData, setModalAllocationTotalData] = useState(0)
	const [ModalAllocationPage, setModalAllocationPage] = useState(0)
	const [ModalAllocationPageSize, setModalAllocationPageSize] = useState(10)

	const [UnitAllocationPage, setUnitAllocationPage] = useState(0)
	const [UnitAllocationPageSize, setUnitAllocationPageSize] = useState(10)
	const [UnitAllocationTotal, setUnitAllocationTotal] = useState(0)

	const formik = useFormik({
		initialValues: {
			register_batch_no: '',
			user_id: null,
			NIK: '',
			received_by: '',
			spm_date_from: null,
			spm_date_to: null,
			spm_form_format: '',
			start_spm_seq: 0,
			total_spm_form: 0,
			spm_no: '',
			stnk_name: '',
			allocated_chassis_no: '',
		},
		onSubmit: (values) => {
			alert(JSON.stringify(values, null, 2))
		},
	})

	const handleNewButton = () => {
		router.push(`/module/unit/transaction/preprinted-spm-register/new`)
	}

	const handleOnDoubleClick = (id: number, action: string) => {
		if (action === 'Deallocate') {
			setListModalAllocation(true)
		}
		if (action === 'Allocate') {
			setDataRowModalAllocation([
				{
					area_id: '3',
					location: '3',
					chassis_no: '3',
					engine_no: '3',
					year: '3',
					aging: '3',
					remark: '3',
				},
			])
			setListModalAllocation(true)
		}
	}

	const handleSearchButton = async () => {
		setIsLoading(true)
		await getUnitAllocationSearch(
			UnitAllocationPage,
			UnitAllocationPageSize,
			formik.values.register_batch_no,
			formik.values.received_by,
			formik.values.spm_date_from
				? dayjs(formik.values.spm_date_from).toISOString()
				: undefined,
			formik.values.spm_date_to
				? dayjs(formik.values.spm_date_to).toISOString()
				: undefined,
			formik.values.spm_form_format,
			formik.values.start_spm_seq,
			formik.values.total_spm_form
		)
			.then((response) => {
				setUnitAllocationTotal(response.total_rows)
				setSearchTableData(response.data)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
				setSearchTableData([])
			})
		setIsLoading(false)
	}

	const handleSPMPage = async (data: number) => {
		setIsLoading(true)
		setUnitAllocationPage(data)
		await getUnitAllocationSearch(
			data,
			UnitAllocationPageSize,
			formik.values.register_batch_no,
			formik.values.received_by,
			formik.values.spm_date_from
				? dayjs(formik.values.spm_date_from).toISOString()
				: undefined,
			formik.values.spm_date_to
				? dayjs(formik.values.spm_date_to).toISOString()
				: undefined,
			formik.values.spm_form_format,
			formik.values.start_spm_seq,
			formik.values.total_spm_form
		)
			.then((response) => {
				setUnitAllocationTotal(response.total_rows)
				setSearchTableData(response.data)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
				setSearchTableData([])
			})
		setIsLoading(false)
	}

	const handleSPMPageSize = async (data: number) => {
		setIsLoading(true)
		setUnitAllocationPageSize(data)
		await getUnitAllocationSearch(
			UnitAllocationPage,
			data,
			formik.values.register_batch_no,
			formik.values.received_by,
			formik.values.spm_date_from
				? dayjs(formik.values.spm_date_from).toISOString()
				: undefined,
			formik.values.spm_date_to
				? dayjs(formik.values.spm_date_to).toISOString()
				: undefined,
			formik.values.spm_form_format,
			formik.values.start_spm_seq,
			formik.values.total_spm_form
		)
			.then((response) => {
				setUnitAllocationTotal(response.total_rows)
				setSearchTableData(response.data)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
				setSearchTableData([])
			})
		setIsLoading(false)
	}

	const handleCloseListModalAllocation = () => {
		setListModalAllocation(false)
	}

	const handleOnDoubleClickListModalAllocation = async (row: any) => {
		if (row !== null) {
			// await getAreaById(row.area_id)
			// 	.then((response) => {
			// 		formik.setFieldValue(
			// 			'is_active',
			// 			response.data.is_active ? 'Active' : 'Deactive'
			// 		)
			// 		formik.setFieldValue('sales_area_code', response.data.area_code)
			// 		formik.setFieldValue('area_description', response.data.description)
			// 		formik.setFieldValue('region_id', response.data.region_id)
			// 		formik.setFieldValue('region_code', response.data.region_code)
			// 		formik.setFieldValue('region_name', response.data.region_name)
			// 		formik.setFieldValue('area_id', response.data.area_id)
			// 		setListModalAllocation(false)
			// 	})
			// 	.catch((error: AxiosError) => {
			// 		alert(error.message)
			// 	})
		}
	}

	const handleDataRowIdListModalAllocation = (row: any) => {
		return row.area_id
	}

	return (
		<>
			<PageLoad loading={isLoading} />
			<ListModal
				open={listModalAllocation}
				handleClose={handleCloseListModalAllocation}
				dataColumn={dataGridColumnAllocation}
				dataRow={dataRowModalAllocation}
				handleDataRowId={handleDataRowIdListModalAllocation}
				handleOnDoubleClick={handleOnDoubleClickListModalAllocation}
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
						<DropDownListDMS
							id='color'
							label={<span>Color</span>}
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
							dateFrom={formik.values.spm_date_from}
							setDateFrom={(date) =>
								formik.setFieldValue('spm_date_from', date, true)
							}
							dateTo={formik.values.spm_date_to}
							setDateTo={(date) =>
								formik.setFieldValue('spm_date_to', date, true)
							}
						/>
						<TextFieldDMS
							id='spm_no'
							label={<span>SPM No.</span>}
							value={formik.values.spm_no}
							onChange={formik.handleChange}
						/>
						<TextFieldDMS
							id='stnk_name'
							label={<span>STNK Name</span>}
							value={formik.values.stnk_name}
							onChange={formik.handleChange}
						/>
						<TextFieldDMS
							id='allocated_chassis_no'
							label={<span>Allocated Chassis No.</span>}
							value={formik.values.allocated_chassis_no}
							onChange={formik.handleChange}
						/>
						<RadioButtonDMS
							row
							id='allocation_status'
							label={<span>Allocation Status</span>}
							listValue={[
								{ value: 'Not Allocated Yet', label: 'Not Allocated Yet' },
								{ value: 'Allocated', label: 'Allocated' },
								{ value: 'All', label: 'All' },
							]}
						/>
						<RadioButtonDMS
							row
							id='purchase_order_status'
							label={<span>Purchase Order Status</span>}
							listValue={[
								{ value: 'Not Yet PO', label: 'Not Yet PO' },
								{ value: 'Already PO', label: 'Already PO' },
								{ value: 'All', label: 'All' },
							]}
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
							getRowId={(row: UnitAllocationProps) => {
								return row.spm_number
							}}
							onRowDoubleClick={(data) =>
								handleOnDoubleClick(data.row.spm_number, data.row.action)
							}
							columns={dataGridColumns}
							rows={searchTableData}
							page={UnitAllocationPage}
							onPageChange={handleSPMPage}
							pageSize={UnitAllocationPageSize}
							onPageSizeChange={handleSPMPageSize}
						/>
					</Grid>
				</Grid>
			</Grid>
		</>
	)
}

export default UnitAllocationPage
