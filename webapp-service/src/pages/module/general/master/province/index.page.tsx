import dynamic from 'next/dynamic'
import { Box, useTheme } from '@mui/material'
import { GridColDef } from '@mui/x-data-grid'
import { useFormik } from 'formik'
import { useState } from 'react'
import { object, string } from 'yup'
import Layout from '@components/Layout.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarMaster from '@components/ToolbarMaster.component'
import { getAllProvince, ProvinceProps } from './api/getAllProvince.api'
import { getProvinceById } from './api/getProvinceById.api'
import useUserStore from '@utils/store.util'
const PageLoad = dynamic(() => import('@components/PageLoad.component'))
const ListModal = dynamic(() => import('@components/ListModal.component'))

const validationSchema = object({
	storage_type_name: string().required('Storage Type is required'),
	storage_type_description: string().required('Description  is required'),
	is_active: string().required('Record Status is required'),
})

const dataGridColumns: GridColDef[] = [
	{
		field: 'storage_type_name',
		headerName: 'Storage Type',
		flex: 1,
	},
	{
		field: 'storage_type_description',
		headerName: 'Description',
		flex: 2,
	},
	{ field: 'is_active', headerName: 'Status', flex: 1 },
]

const ProvinceMasterPage = () => {
	const theme = useTheme()
	const [listModal, setListModal] = useState(false)
	const [dataRowListModal, setDataRowListModal] = useState([])
	const [isLoading, setIsLoading] = useState(false)
	const store = useUserStore((state) => state)

	const formik = useFormik({
		initialValues: {
			storage_type_id: null,
			storage_type_name: '',
			storage_type_description: '',
			is_active: 'Active',
		},
		validationSchema: validationSchema,
		onSubmit: (values) => {
			alert(JSON.stringify(values, null, 2))
		},
	})

	const handleOpenListModal = async () => {
		setIsLoading(true)
		const storageTypeData = await getAllProvince()
		if (storageTypeData !== null) {
			setDataRowListModal(storageTypeData)
			setIsLoading(false)
			setListModal(true)
		}
	}
	const handleCloseListModal = () => {
		setListModal(false)
	}
	const handleOnDoubleClickListModal = (row: ProvinceProps) => {
		if (row !== null) {
			formik.setFieldValue('is_active', row.is_active ? 'Active' : 'Deactive')
			formik.setFieldValue('storage_type_name', row.storage_type_name)
			formik.setFieldValue(
				'storage_type_description',
				row.storage_type_description
			)
			formik.setFieldValue('storage_type_id', row.storage_type_id)
			setListModal(false)
		}
	}

	const handleDataRowIdListModal = (row: ProvinceProps) => {
		return row.storage_type_id
	}

	const handleOnBlurStorageType = async () => {
		const storageTypeData = await getProvinceById(
			formik.values.storage_type_name
		)
		if (storageTypeData !== null) {
			formik.setFieldValue(
				'is_active',
				storageTypeData.is_active ? 'Active' : 'Deactive'
			)
			formik.setFieldValue(
				'storage_type_name',
				storageTypeData.storage_type_name
			)
			formik.setFieldValue(
				'storage_type_description',
				storageTypeData.storage_type_description
			)
			formik.setFieldValue('storage_type_id', storageTypeData.storage_type_id)
		}
	}

	const activeButtonValue = () => {
		if (formik.values.storage_type_id === null) return true
		if (formik.values.is_active === 'Active') return true

		return false
	}

	const handleActiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Active')
	}

	const deactiveButtonValue = () => {
		if (formik.values.storage_type_id === null) return true
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
				open={listModal}
				handleClose={handleCloseListModal}
				dataColumn={dataGridColumns}
				dataRow={dataRowListModal}
				handleDataRowId={handleDataRowIdListModal}
				handleOnDoubleClick={handleOnDoubleClickListModal}
			/>
			<ToolbarMaster
				DisableBackButton
				DisableNextButton
				DisableActiveButton={activeButtonValue()}
				handleActiveButton={handleActiveButtonListModal}
				DisableDeactiveButton={deactiveButtonValue()}
				handleDeactiveButton={handleDeactiveButtonListModal}
				handleSaveButton={formik.handleSubmit}
				handleListButton={handleOpenListModal}
				handleNewButton={store.updateUserSeed}
			/>
			<Box sx={{ maxWidth: '540px', padding: '1%' }}>
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
					error={formik.touched.is_active && Boolean(formik.errors.is_active)}
					helperText={formik.touched.is_active && formik.errors.is_active}
				/>
				<TextFieldDMS
					id='storage_type_name'
					label={
						<span>
							Storage Type{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.storage_type_name}
					onChange={formik.handleChange}
					onBlur={handleOnBlurStorageType}
					error={
						formik.touched.storage_type_name &&
						Boolean(formik.errors.storage_type_name)
					}
					helperText={
						formik.touched.storage_type_name && formik.errors.storage_type_name
					}
				/>
				<TextFieldDMS
					id='storage_type_description'
					label={
						<span>
							Description{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.storage_type_description}
					onChange={formik.handleChange}
					error={
						formik.touched.storage_type_description &&
						Boolean(formik.errors.storage_type_description)
					}
					helperText={
						formik.touched.storage_type_description &&
						formik.errors.storage_type_description
					}
				/>
			</Box>
		</>
	)
}

export default ProvinceMasterPage
