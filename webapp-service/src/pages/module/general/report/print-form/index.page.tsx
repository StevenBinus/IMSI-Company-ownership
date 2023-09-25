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
	PrintFormProps,
	getPrintFormSearch,
} from './api/getPrintFormSearch.api'
import DropDownListDMS from '@components/DropDownListDMS.component'
import useUserStore from '@utils/store.util'
import ToolbarReport from '@components/ToolbarReport.component'

const dataGridColumns: GridColDef[] = [
	{
		field: 'document_number',
		headerName: 'Doc No.',
		flex: 1,
	},
	{
		field: 'document_date',
		headerName: 'Doc. Date',
		flex: 1,
	},
	{
		field: 'document_user',
		headerName: 'Customer / Supplier',
		flex: 1,
	},
	{
		field: 'tax_invoice_number',
		headerName: 'Tax Invoice No.',
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
	const store = useUserStore((state) => state)
	const [listModalUser, setListModalUser] = useState(false)
	const [dataRowModalUser, setDataRowModalUser] = useState([])
	const [searchTableData, setSearchTableData] = useState([])
	const [isLoading, setIsLoading] = useState(false)

	const formik = useFormik({
		initialValues: {
			unit_module: true,
			after_sales_module: true,
			finance_module: true,
			form_name: '',
			document_date_from: null,
			document_date_to: null,
			document_number: '',
			user_id: null,
			NIK: '',
			document_user: '',
			brand_id: 0,
			brand: '',
			profit_center_id: 0,
			profit_center: '',
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
		store.updateUserSeed()
	}

	const handleOnDoubleClick = (id: number) => {
		router.push(`/module/general/report/print-form/${id}`)
	}

	const handleSearchButton = async () => {
		setIsLoading(true)
		await getPrintFormSearch(0, 5)
			.then((response) => {
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
			<ToolbarReport />
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
							id='modul'
							label={<span>Modul</span>}
							value={''}
							onChange={formik.handleChange}
						/>
						<DropDownListDMS
							id='form_name'
							label={<span>Form Name</span>}
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
							id='document_date'
							label={<span>Document Date</span>}
							dateFrom={formik.values.document_date_from}
							setDateFrom={(date) =>
								formik.setFieldValue('document_date_from', date, true)
							}
							dateTo={formik.values.document_date_to}
							setDateTo={(date) =>
								formik.setFieldValue('document_date_to', date, true)
							}
						/>

						<TextFieldLookUpDMS
							descriptionValue={formik.values.document_number}
							id='document_number'
							label={<span>Document Number</span>}
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

						<TextFieldLookUpDMS
							descriptionValue={formik.values.document_user}
							id='document_user'
							label={<span>Customer / Supplier</span>}
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
							id='profit_center'
							label={<span>Profit Center</span>}
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
							pageSize={5}
							getRowId={(row: PrintFormProps) => {
								return row.document_id
							}}
							onRowDoubleClick={(data) =>
								handleOnDoubleClick(data.row.document_id)
							}
							columns={dataGridColumns}
							rows={searchTableData}
						/>
					</Grid>
				</Grid>
			</Grid>
		</>
	)
}

export default SPMRegisterPage
