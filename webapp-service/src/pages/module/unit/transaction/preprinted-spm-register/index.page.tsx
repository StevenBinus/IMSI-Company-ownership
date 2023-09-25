import DataGridDMS from '@components/DataGridDMS.component'
import DateRangePickerDMS from '@components/DateRangePickerDMS.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import { Box, Button, Grid, Typography, useTheme } from '@mui/material'
import { GridColDef, GridValueGetterParams } from '@mui/x-data-grid'
import SearchIcon from '@mui/icons-material/Search'
import { useRouter } from 'next/router'
import { useState } from 'react'
import {
	SPMRegisterProps,
	getSPMRegisterSearch,
} from './api/getSPMRegisterSearch.api'
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

const dataGridColumns: GridColDef[] = [
	{
		field: 'register_document_number',
		headerName: 'Batch No.',
		flex: 1,
	},
	{
		field: 'spm_received_by',
		headerName: 'Received By',
		flex: 1,
	},
	{
		field: 'spm_received_date',
		headerName: 'Received Date',
		flex: 1,
	},
	{
		field: 'spm_number_format',
		headerName: 'SPM Form Format',
		flex: 1,
	},
	{
		field: 'total_spm',
		headerName: 'Total SPM Form',
		flex: 1,
	},
	{
		field: 'spm_number_from',
		headerName: 'Start SPM Form Seq.',
		flex: 1,
	},
]

export const dataColumnModalUser: GridColDef[] = [
	{
		field: 'NIK',
		headerName: 'Emp. No',
		flex: 1,
	},
	{
		field: 'user_name',
		headerName: 'Employee Name',
		flex: 2,
	},
	{
		field: 'user_position',
		headerName: 'Position',
		flex: 2,
	},
	{
		field: 'is_active',
		headerName: 'Status',
		flex: 1,
		renderCell: (params: GridValueGetterParams) => {
			return (
				<Typography>{params.row.is_active ? 'Active' : 'Deactive'}</Typography>
			)
		},
	},
]

const SPMRegisterPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const [listModalUser, setListModalUser] = useState(false)
	const [dataRowModalUser, setDataRowModalUser] = useState([])
	const [searchTableData, setSearchTableData] = useState([])
	const [isLoading, setIsLoading] = useState(false)

	const [SPMPage, setSPMPage] = useState(0)
	const [SPMPageSize, setSPMPageSize] = useState(10)
	const [SPMTotal, setSPMTotal] = useState(0)

	const formik = useFormik({
		initialValues: {
			register_batch_no: '',
			user_id: null,
			NIK: '',
			received_by: '',
			received_date_from: null,
			received_date_to: null,
			spm_form_format: '',
			start_spm_seq: 0,
			total_spm_form: 0,
		},
		onSubmit: (values) => {
			alert(JSON.stringify(values, null, 2))
		},
	})

	const handleOpenListModalUser = async () => {
		setIsLoading(true)
		const userData = await getAllUser()
		if (userData !== null) {
			setDataRowModalUser(userData)
		}
		setIsLoading(false)
		setListModalUser(true)
	}

	const handleOnDoubleClickListModalUser = async (row: UserListProps) => {
		setIsLoading(true)
		if (row !== null) {
			const userData = await getUserById(row.user_id)
			if (userData !== null) {
				formik.setFieldValue('user_id', userData.user_id)
				formik.setFieldValue('NIK', userData.NIK)
				formik.setFieldValue('spm_received_by', userData.user_name)
			}
		}
		setIsLoading(false)
		setListModalUser(false)
	}

	const handleDataRowIdListModalUser = (row: UserListProps) => {
		return row.user_id
	}

	const handleOnBlurUser = async () => {
		setIsLoading(true)
		const userData = await getUserByNIK(formik.values.NIK)
		if (userData !== null) {
			formik.setFieldValue('user_id', userData.user_id)
			formik.setFieldValue('user_name', userData.user_name)
		} else {
			formik.setFieldValue('user_id', null)
			formik.setFieldValue('user_name', '')
		}
		setIsLoading(false)
	}

	const handleNewButton = () => {
		router.push(`/module/unit/transaction/preprinted-spm-register/new`)
	}

	const handleOnDoubleClick = (id: number) => {
		router.push(`/module/unit/transaction/preprinted-spm-register/${id}`)
	}

	const handleSearchButton = async () => {
		setIsLoading(true)
		await getSPMRegisterSearch(
			SPMPage,
			SPMPageSize,
			formik.values.register_batch_no,
			formik.values.received_by,
			formik.values.received_date_from
				? dayjs(formik.values.received_date_from).toISOString()
				: undefined,
			formik.values.received_date_to
				? dayjs(formik.values.received_date_to).toISOString()
				: undefined,
			formik.values.spm_form_format,
			formik.values.start_spm_seq,
			formik.values.total_spm_form
		)
			.then((response) => {
				setSPMTotal(response.total_rows)
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
		setSPMPage(data)
		await getSPMRegisterSearch(
			data,
			SPMPageSize,
			formik.values.register_batch_no,
			formik.values.received_by,
			formik.values.received_date_from
				? dayjs(formik.values.received_date_from).toISOString()
				: undefined,
			formik.values.received_date_to
				? dayjs(formik.values.received_date_to).toISOString()
				: undefined,
			formik.values.spm_form_format,
			formik.values.start_spm_seq,
			formik.values.total_spm_form
		)
			.then((response) => {
				setSPMTotal(response.total_rows)
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
		setSPMPageSize(data)
		await getSPMRegisterSearch(
			SPMPage,
			data,
			formik.values.register_batch_no,
			formik.values.received_by,
			formik.values.received_date_from
				? dayjs(formik.values.received_date_from).toISOString()
				: undefined,
			formik.values.received_date_to
				? dayjs(formik.values.received_date_to).toISOString()
				: undefined,
			formik.values.spm_form_format,
			formik.values.start_spm_seq,
			formik.values.total_spm_form
		)
			.then((response) => {
				setSPMTotal(response.total_rows)
				setSearchTableData(response.data)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
				setSearchTableData([])
			})
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
						<TextFieldDMS
							id='register_batch_no'
							label={<span>Register Batch No</span>}
							value={formik.values.register_batch_no}
							onChange={formik.handleChange}
						/>
						<TextFieldLookUpDMS
							descriptionValue={formik.values.received_by}
							id='received_by'
							label={<span>Received By</span>}
							value={formik.values.NIK}
							onChange={formik.handleChange}
							dataColumn={dataColumnModalUser}
							dataRow={dataRowModalUser}
							handleDataRowId={handleDataRowIdListModalUser}
							handleOnDoubleClick={handleOnDoubleClickListModalUser}
							handleOnBlur={handleOnBlurUser}
							listModal={listModalUser}
							handleOpenListModal={handleOpenListModalUser}
							handleCloseListModal={() => setListModalUser(false)}
						/>
						<DateRangePickerDMS
							id='received_date'
							label={<span>Received Date</span>}
							dateFrom={formik.values.received_date_from}
							setDateFrom={(date) =>
								formik.setFieldValue('received_date_from', date, true)
							}
							dateTo={formik.values.received_date_to}
							setDateTo={(date) =>
								formik.setFieldValue('received_date_to', date, true)
							}
						/>
						<TextFieldDMS
							id='spm_form_format'
							label={<span>SPM Form Format</span>}
							value={formik.values.spm_form_format}
							onChange={formik.handleChange}
						/>
						<NumericFormat
							customInput={TextFieldDMS}
							thousandSeparator
							id='start_spm_seq'
							label={<span>Start SPM Form Seq.</span>}
							value={formik.values.start_spm_seq}
							onValueChange={(element) => {
								if (element.floatValue === undefined) {
									formik.setFieldValue('start_spm_seq', 0, true)
								} else {
									formik.setFieldValue(
										'start_spm_seq',
										element.floatValue,
										true
									)
								}
							}}
						/>
						<NumericFormat
							customInput={TextFieldDMS}
							thousandSeparator
							id='total_spm_form'
							label={<span>Total SPM Form</span>}
							value={formik.values.total_spm_form}
							onValueChange={(element) => {
								if (element.floatValue === undefined) {
									formik.setFieldValue('total_spm_form', 0, true)
								} else {
									formik.setFieldValue(
										'total_spm_form',
										element.floatValue,
										true
									)
								}
							}}
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
							getRowId={(row: SPMRegisterProps) => {
								return row.register_system_number
							}}
							onRowDoubleClick={(data) =>
								handleOnDoubleClick(data.row.register_system_number)
							}
							columns={dataGridColumns}
							rows={searchTableData}
							page={SPMPage}
							onPageChange={handleSPMPage}
							pageSize={SPMPageSize}
							onPageSizeChange={handleSPMPageSize}
						/>
					</Grid>
				</Grid>
			</Grid>
		</>
	)
}

export default SPMRegisterPage
