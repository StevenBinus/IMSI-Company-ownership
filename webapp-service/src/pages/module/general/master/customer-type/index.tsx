import Layout from '@components/Layout.component'
import ListModal from '@components/ListModal.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarMaster from '@components/ToolbarMaster.component'
import { Box, useTheme } from '@mui/material'
import { GridColDef } from '@mui/x-data-grid'
import { useFormik } from 'formik'
import { useState } from 'react'
import { object, string } from 'yup'
import {
	CustomerTypeProps,
	getAllCustomerType,
} from './api/getAllCustomerType.api'
import { getCustomerTypeById } from './api/getCustomerTypeById.api'

const validationSchema = object({
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

interface CustomerTypeMasterProps {
	refresh: () => void
}

const CustomerTypeMaster = (props: CustomerTypeMasterProps) => {
	const theme = useTheme()
	const [listModal, setListModal] = useState(false)
	const [dataRowListModal, setDataRowListModal] = useState([])
	const [isLoading, setIsLoading] = useState(false)

	const formik = useFormik({
		initialValues: {
			customer_type_id: null,
			customer_type: '',
			customer_type_description: '',
			customer_type_flag: '',
			customer_type_group: '',
			bbn: false,
			police_invoice: false,
			spm: false,
			tax_free: false,
			is_active: 'Active',
		},
		validationSchema: validationSchema,
		onSubmit: (values) => {
			alert(JSON.stringify(values, null, 2))
		},
	})

	const handleOpenListModal = async () => {
		setIsLoading(true)
		const storageTypeData = await getAllCustomerType()
		if (storageTypeData !== null) {
			setDataRowListModal(storageTypeData)
			setIsLoading(false)
			setListModal(true)
		}
	}
	const handleCloseListModal = () => {
		setListModal(false)
	}
	const handleOnDoubleClickListModal = (row: CustomerTypeProps) => {
		if (row !== null) {
			formik.setFieldValue('is_active', row.is_active ? 'Active' : 'Deactive')
			setListModal(false)
		}
	}

	const handleDataRowIdListModal = (row: CustomerTypeProps) => {
		return row.customer_type_id
	}

	const handleOnBlurStorageType = async () => {
		const storageTypeData = await getCustomerTypeById(
			formik.values.customer_type
		)
		if (storageTypeData !== null) {
			formik.setFieldValue(
				'is_active',
				storageTypeData.is_active ? 'Active' : 'Deactive'
			)
		}
	}

	const activeButtonValue = () => {
		if (formik.values.customer_type_id === null) return true
		if (formik.values.is_active === 'Active') return true

		return false
	}

	const handleActiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Active')
	}

	const deactiveButtonValue = () => {
		if (formik.values.customer_type_id === null) return true
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
				handleNewButton={props.refresh}
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
			</Box>
		</>
	)
}

const CustomerTypeMasterPage = () => {
	const [seed, setSeed] = useState(1)
	const reset = () => {
		setSeed(Math.random())
	}
	return (
		<Layout>
			<CustomerTypeMaster key={seed} refresh={reset} />
		</Layout>
	)
}

export default CustomerTypeMasterPage
