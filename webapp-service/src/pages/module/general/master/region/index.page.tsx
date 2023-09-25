import dynamic from 'next/dynamic'
import { Box, Grid, Typography, useTheme } from '@mui/material'
import { GridColDef, GridValueGetterParams } from '@mui/x-data-grid'
import { useFormik } from 'formik'
import { useState } from 'react'
import { object, string } from 'yup'
import { AxiosError } from 'axios'
import TextFieldLookUpDMS from '@components/TextFieldLookUpDMS.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarMaster from '@components/ToolbarMaster.component'
import { getAllRegion, RegionListProps } from './api/getAllRegion.api'
import { getRegionById } from './api/getRegionById.api'
import useUserStore from '@utils/store.util'
import { getRegionByCode } from './api/getRegionByCode.api'
import { UserListProps, getAllUser } from '../user/api/getAllUser.api'
import { getUserById } from '../user/api/getUserById'
import { getUserByNIK } from '../user/api/getUserByNIK'
const PageLoad = dynamic(() => import('@components/PageLoad.component'))
const ListModal = dynamic(() => import('@components/ListModal.component'))

const validationSchema = object({
	region_code: string().required('Regional Code is required'),
	region_name: string().required('Regional Name is required'),
	user_id: string().required('Regional Manager is required'),
	is_active: string().required('Record Status is required'),
})

export const dataColumnRegion: GridColDef[] = [
	{
		field: 'region_code',
		headerName: 'Regional Code',
		flex: 1,
	},
	{
		field: 'region_name',
		headerName: 'Regional Name',
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

const RegionMasterPage = () => {
	const theme = useTheme()
	const [listModalRegion, setListModalRegion] = useState(false)
	const [listModalUser, setListModalUser] = useState(false)
	const [dataRowModalRegion, setDataRowModalRegion] = useState([])
	const [dataRowModalUser, setDataRowModalUser] = useState([])
	const [isLoading, setIsLoading] = useState(false)
	const store = useUserStore((state) => state)

	const formik = useFormik({
		initialValues: {
			region_id: null,
			region_code: '',
			region_name: '',
			user_id: null,
			NIK: '',
			user_name: '',
			is_active: 'Active',
		},
		validationSchema: validationSchema,
		onSubmit: (values) => {
			alert(JSON.stringify(values, null, 2))
		},
	})

	const handleOpenListModalRegion = async () => {
		setIsLoading(true)
		await getAllRegion(0, 10)
			.then((response) => {
				setDataRowModalRegion(response.data)
				setIsLoading(false)
				setListModalRegion(true)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
				setIsLoading(false)
			})
	}

	const handleOnDoubleClickListModalRegion = async (row: RegionListProps) => {
		if (row !== null) {
			const regionData = await getRegionById(row.region_id)
			if (regionData !== null) {
				formik.setFieldValue('is_active', regionData.is_active)
				formik.setFieldValue('region_id', regionData.region_id)
				formik.setFieldValue('region_code', regionData.region_code)
				formik.setFieldValue('region_name', regionData.region_name)
				formik.setFieldValue('user_id', regionData.user_id)
				formik.setFieldValue('NIK', regionData.NIK)
				formik.setFieldValue('user_name', regionData.user_name)
			}
			setListModalRegion(false)
		}
	}

	const handleDataRowIdListModalRegion = (row: RegionListProps) => {
		return row.region_id
	}

	const handleOnBlurRegion = async () => {
		setIsLoading(true)
		const regionData = await getRegionByCode(formik.values.region_code)
		if (regionData !== null) {
			formik.setFieldValue('is_active', regionData.is_active)
			formik.setFieldValue('region_id', regionData.region_id)
			formik.setFieldValue('region_code', regionData.region_code)
			formik.setFieldValue('region_name', regionData.region_name)
			formik.setFieldValue('user_id', regionData.user_id)
			formik.setFieldValue('NIK', regionData.NIK)
			formik.setFieldValue('user_name', regionData.user_name)
		}
		setIsLoading(false)
	}

	const handleOpenListModalUser = async () => {
		setIsLoading(true)
		const regionData = await getAllUser()
		if (regionData !== null) {
			setDataRowModalUser(regionData)
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
				formik.setFieldValue('user_name', userData.user_name)
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

	const activeButtonValue = () => {
		if (formik.values.region_id === null) return true
		if (formik.values.is_active === 'Active') return true

		return false
	}

	const handleActiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Active')
	}

	const deactiveButtonValue = () => {
		if (formik.values.region_id === null) return true
		if (formik.values.is_active === 'Deactive') return true

		return false
	}
	const handleDeactiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Deactive')
	}

	return (
		<>
			<PageLoad loading={isLoading} />
			<ListModal
				open={listModalRegion}
				handleClose={() => setListModalRegion(false)}
				dataColumn={dataColumnRegion}
				dataRow={dataRowModalRegion}
				handleDataRowId={handleDataRowIdListModalRegion}
				handleOnDoubleClick={handleOnDoubleClickListModalRegion}
			/>
			<ToolbarMaster
				DisableBackButton
				DisableNextButton
				DisableActiveButton={activeButtonValue()}
				handleActiveButton={handleActiveButtonListModal}
				DisableDeactiveButton={deactiveButtonValue()}
				handleDeactiveButton={handleDeactiveButtonListModal}
				handleSaveButton={formik.handleSubmit}
				handleListButton={handleOpenListModalRegion}
				DisableListButton={formik.values.region_id !== null}
				handleNewButton={store.updateUserSeed}
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
							disabled
							id='is_active'
							label={
								<span>
									Record Status{' '}
									<span style={{ color: theme.palette.error.main }}>*</span>
								</span>
							}
							value={formik.values.is_active}
							onChange={formik.handleChange}
							error={
								formik.touched.is_active && Boolean(formik.errors.is_active)
							}
							helperText={formik.touched.is_active && formik.errors.is_active}
						/>
						<TextFieldDMS
							disabled={formik.values.region_id !== null}
							id='region_code'
							label={
								<span>
									Regional Code{' '}
									<span style={{ color: theme.palette.error.main }}>*</span>
								</span>
							}
							value={formik.values.region_code}
							onChange={formik.handleChange}
							onBlur={handleOnBlurRegion}
							error={
								formik.touched.region_code && Boolean(formik.errors.region_code)
							}
							helperText={
								formik.touched.region_code && formik.errors.region_code
							}
						/>
						<TextFieldDMS
							id='region_name'
							label={
								<span>
									Regional Name{' '}
									<span style={{ color: theme.palette.error.main }}>*</span>
								</span>
							}
							value={formik.values.region_name}
							onChange={formik.handleChange}
							error={
								formik.touched.region_name && Boolean(formik.errors.region_name)
							}
							helperText={
								formik.touched.region_name && formik.errors.region_name
							}
						/>

						<TextFieldLookUpDMS
							descriptionValue={formik.values.user_name}
							id='NIK'
							label={
								<span>
									Regional Manager{' '}
									<span style={{ color: theme.palette.error.main }}>*</span>
								</span>
							}
							value={formik.values.NIK}
							onChange={formik.handleChange}
							error={
								formik.touched.user_name && Boolean(formik.errors.user_name)
							}
							helperText={formik.touched.user_name && formik.errors.user_name}
							dataColumn={dataColumnModalUser}
							dataRow={dataRowModalUser}
							handleDataRowId={handleDataRowIdListModalUser}
							handleOnDoubleClick={handleOnDoubleClickListModalUser}
							handleOnBlur={handleOnBlurUser}
							listModal={listModalUser}
							handleOpenListModal={handleOpenListModalUser}
							handleCloseListModal={() => setListModalUser(false)}
						/>
					</Grid>
				</Grid>
			</Grid>
		</>
	)
}

export default RegionMasterPage
