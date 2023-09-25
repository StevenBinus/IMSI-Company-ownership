import dynamic from 'next/dynamic'
import { Box, Typography, useTheme } from '@mui/material'
import {
	GridColDef,
	GridSortModel,
	GridValueGetterParams,
} from '@mui/x-data-grid'
import { useFormik } from 'formik'
import { useState } from 'react'
import { object, string } from 'yup'
import ToolbarMaster from '@components/ToolbarMaster.component'
import Layout from '@components/Layout.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import {
	CompanyOwnershipProps,
	getAllCompanyOwnership,
} from './api/getAllCompanyOwnership.api'
import { getCompanyOwnershipById } from './api/getCompanyOwnershipById.api'
import useUserStore from '@utils/store.util'
const PageLoad = dynamic(() => import('@components/PageLoad.component'))
const ListModal = dynamic(() => import('@components/ListModal.component'))

const validationSchema = object({
	company_ownership_type: string().required('Ownership Type is required'),
	company_ownership_name: string().required('Description  is required'),
	is_active: string().required('Record Status is required'),
})

const dataGridColumns: GridColDef[] = [
	{
		field: 'company_ownership_type',
		headerName: 'Ownership Type',
		flex: 1,
	},
	{
		field: 'company_ownership_name',
		headerName: 'Description',
		flex: 2,
	},
	{
		field: 'is_active',
		headerName: 'Status',
		flex: 1,
		renderCell: (params: GridValueGetterParams) => {
			return (
				<Typography>
					{Boolean(params.row.is_active) ? 'Active' : 'Deactive'}
				</Typography>
			)
		},
	},
]

const CompanyOwnershipMasterPage = () => {
	const theme = useTheme()
	const [listModal, setListModal] = useState(false)
	const [dataRowListModal, setDataRowListModal] = useState([])
	const [isLoading, setIsLoading] = useState(false)
	const store = useUserStore((state) => state)

	const formik = useFormik({
		initialValues: {
			company_ownership_id: null,
			company_ownership_type: '',
			company_ownership_name: '',
			is_active: 'Active',
		},
		validationSchema: validationSchema,
		onSubmit: (values) => {
			console.log(values)
			alert(JSON.stringify(values, null, 2))
		},
	})

	const handleOpenListModal = async () => {
		setIsLoading(true)
		const storageTypeData = await getAllCompanyOwnership()
		if (storageTypeData !== null) {
			setDataRowListModal(storageTypeData)
			setIsLoading(false)
			setListModal(true)
		}
	}
	const handleCloseListModal = () => {
		setListModal(false)
	}

	const handleOnDoubleClickListModal = (row: CompanyOwnershipProps) => {
		if (row !== null) {
			formik.setFieldValue('company_ownership_id', row.company_ownership_id)
			formik.setFieldValue('company_ownership_type', row.company_ownership_type)
			formik.setFieldValue('company_ownership_name', row.company_ownership_name)
			formik.setFieldValue('is_active', row.is_active ? 'Active' : 'Deactive')
			setListModal(false)
		}
	}

	const handleDataRowIdListModal = (row: CompanyOwnershipProps) => {
		return row.company_ownership_id
	}

	const handleSortTableListModel = (data: GridSortModel) => {
		console.log(data)
	}

	const activeButtonValue = () => {
		if (formik.values.company_ownership_id === null) return true
		if (formik.values.is_active === 'Active') return true

		return false
	}

	const handleActiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Active')
	}

	const deactiveButtonValue = () => {
		if (formik.values.company_ownership_id === null) return true
		if (formik.values.is_active === 'Deactive') return true

		return false
	}
	const handleDeactiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Deactive')
	}

	const handleOnBlurCompanyOwnershipType = async () => {
		setIsLoading(true)
		const companyOwnershipData = await getCompanyOwnershipById(
			formik.values.company_ownership_type
		)
		if (companyOwnershipData !== null) {
			formik.setFieldValue(
				'is_active',
				companyOwnershipData.is_active ? 'Active' : 'Deactive'
			)
			formik.setFieldValue(
				'company_ownership_name',
				companyOwnershipData.company_ownership_name
			)
			formik.setFieldValue(
				'company_ownership_type',
				companyOwnershipData.company_ownership_type
			)
			formik.setFieldValue(
				'company_ownership_id',
				companyOwnershipData.company_ownership_id
			)
		}
		setIsLoading(false)
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
				handleSortTable={handleSortTableListModel}
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
					id='company_ownership_type'
					disabled={formik.values.company_ownership_id !== null}
					label={
						<span>
							Ownership Type{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.company_ownership_type}
					onChange={formik.handleChange}
					onBlur={handleOnBlurCompanyOwnershipType}
					error={
						formik.touched.company_ownership_type &&
						Boolean(formik.errors.company_ownership_type)
					}
					helperText={
						formik.touched.company_ownership_type &&
						formik.errors.company_ownership_type
					}
				/>
				<TextFieldDMS
					id='company_ownership_name'
					label={
						<span>
							Description{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.company_ownership_name}
					onChange={formik.handleChange}
					error={
						formik.touched.company_ownership_name &&
						Boolean(formik.errors.company_ownership_name)
					}
					helperText={
						formik.touched.company_ownership_name &&
						formik.errors.company_ownership_name
					}
				/>
			</Box>
		</>
	)
}

export default CompanyOwnershipMasterPage
