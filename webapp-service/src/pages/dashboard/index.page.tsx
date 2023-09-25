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
import { DashboardProps } from './api/getDashboardData.api'
import HistoryIcon from '@mui/icons-material/History'
import ListAltIcon from '@mui/icons-material/ListAlt'
import UpdateIcon from '@mui/icons-material/Update'

const dataGridColumns: GridColDef[] = [
	{
		field: 'transaction_type',
		headerName: 'Transaction',
		flex: 1,
	},
	{
		field: 'approval_name',
		headerName: 'Approval',
		flex: 1,
	},
	{
		field: 'count',
		headerName: 'Count',
		flex: 1,
	},
]

export const dataColumnNews: GridColDef[] = [
	{
		field: 'title',
		headerName: 'Title',
		flex: 1,
	},
	{
		field: 'headline',
		headerName: 'Headline',
		flex: 2,
	},
	{
		field: 'date',
		headerName: 'Date',
		flex: 1,
	},
]

export const dataColumnFollowUp: GridColDef[] = [
	{
		field: 'prospect_number',
		headerName: 'Prospect No.',
		flex: 1,
	},
	{
		field: 'prospect_date',
		headerName: 'Prospect Date',
		flex: 2,
	},
	{
		field: 'prospect_name',
		headerName: 'Name',
		flex: 2,
	},
	{
		field: 'follow_up_date',
		headerName: 'Follow Up Date',
		flex: 2,
	},
	{
		field: 'result_date',
		headerName: 'Result Date',
		flex: 2,
	},
	{
		field: 'follow_up_stage',
		headerName: 'Stage',
		flex: 2,
	},
	{
		field: 'follow_up_age',
		headerName: 'Age',
		flex: 2,
	},
	{
		field: 'follow_up_note',
		headerName: 'Follow Up Note',
		flex: 2,
	},
]

const SPMRegisterPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const [listModalUser, setListModalUser] = useState(false)
	const [dataRowModalUser, setDataRowModalUser] = useState([])
	const [searchTableData, setSearchTableData] = useState([])
	const [isLoading, setIsLoading] = useState(false)

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

	return (
		<>
			<PageLoad loading={isLoading} />
			<Grid
				container
				item
				alignItems='center'
				direction='column'
				sx={{ minHeight: '93vh' }}
			>
				<Grid
					container
					item
					direction='column'
					sx={{
						minHeight: '240px',
						padding: '2%',
						margin: '1% 2% 0 2%',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Grid container item>
						<Typography variant='h4' sx={{ paddingBottom: '1%' }}>
							News List
						</Typography>
					</Grid>
					<DataGridDMS
						pageSize={5}
						getRowId={(row: DashboardProps) => {
							return row.document_id
						}}
						onRowDoubleClick={(data) =>
							handleOnDoubleClick(data.row.document_id)
						}
						columns={dataColumnNews}
						rows={searchTableData}
					/>
				</Grid>
				<Grid
					container
					item
					direction='row'
					sx={{
						padding: '1%',
						margin: '1% 0 0 0',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Grid container item direction='row'>
						<Grid
							container
							item
							xs={3}
							justifyContent='flex-start'
							alignItems='center'
						>
							<Button startIcon={<ListAltIcon />}>
								<Typography variant='h5' textTransform='none'>
									Requested Approval List
								</Typography>
							</Button>
						</Grid>
						<Box display='flex' justifyContent='center' alignItems='center'>
							|
						</Box>
						<Grid
							container
							item
							xs={3}
							justifyContent='center'
							alignItems='center'
						>
							<Button startIcon={<HistoryIcon />}>
								<Typography variant='h5' textTransform='none'>
									Approved History
								</Typography>
							</Button>
						</Grid>
						<Box display='flex' justifyContent='center' alignItems='center'>
							|
						</Box>
						<Grid
							container
							item
							xs={3}
							justifyContent='center'
							alignItems='center'
						>
							<Button startIcon={<UpdateIcon />}>
								<Typography variant='h5' textTransform='none'>
									Approval History
								</Typography>
							</Button>
						</Grid>
					</Grid>
				</Grid>
				<Grid
					container
					item
					direction='column'
					sx={{
						minHeight: '240px',
						padding: '2%',
						margin: '1% 2% 0 2%',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Grid
						container
						item
						direction='row'
						sx={{
							paddingBottom: '1%',
						}}
					>
						<Button>
							<Typography variant='h4' textTransform='none'>
								Approval List
							</Typography>
						</Button>
					</Grid>

					<DataGridDMS
						pageSize={5}
						getRowId={(row: DashboardProps) => {
							return row.document_id
						}}
						onRowDoubleClick={(data) =>
							handleOnDoubleClick(data.row.document_id)
						}
						columns={dataGridColumns}
						rows={searchTableData}
					/>
				</Grid>
				<Grid
					container
					item
					direction='column'
					xs={12}
					sx={{
						minHeight: '240px',
						padding: '2%',
						margin: '1%',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Typography variant='h4' sx={{ paddingBottom: '1%' }}>
						Follow Up Notes
					</Typography>
					<DataGridDMS
						pageSize={5}
						getRowId={(row: DashboardProps) => {
							return row.document_id
						}}
						onRowDoubleClick={(data) =>
							handleOnDoubleClick(data.row.document_id)
						}
						columns={dataColumnFollowUp}
						rows={searchTableData}
					/>
				</Grid>
			</Grid>
		</>
	)
}

export default SPMRegisterPage
