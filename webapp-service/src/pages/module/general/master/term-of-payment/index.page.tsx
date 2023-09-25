import dynamic from 'next/dynamic'
import { Box, Typography, useTheme } from '@mui/material'
import { GridColDef, GridValueGetterParams } from '@mui/x-data-grid'
import { useFormik } from 'formik'
import { useState } from 'react'
import { NumericFormat } from 'react-number-format'
import { number, object, string } from 'yup'
import Layout from '@components/Layout.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarMaster from '@components/ToolbarMaster.component'
import {
	getAllTermOfPayment,
	TermOfPaymentProps,
} from './api/getAllTermOfPayment.api'
import { getTermOfPaymentById } from './api/getTermOfPaymentById.api'
import useUserStore from '@utils/store.util'
const PageLoad = dynamic(() => import('@components/PageLoad.component'))
const ListModal = dynamic(() => import('@components/ListModal.component'))

const validationSchema = object({
	term_of_payment_code: string().required('Payment Code is required'),
	term_of_payment_name: string().required('Description  is required'),
	term_of_payment_policy: string().required('Top Policy  is required'),
	is_active: string().required('Record Status is required'),
	term_of_payment_interval: number().integer('Top Interval must be a number'),
	term_of_payment_installment: number().integer(
		'Top Installment must be a number'
	),
})

const dataGridColumns: GridColDef[] = [
	{
		field: 'term_of_payment_code',
		headerName: 'Term Of Payment Code',
		flex: 2,
	},
	{
		field: 'term_of_payment_name',
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

const TermOfPaymentMasterPage = () => {
	const theme = useTheme()
	const [listModal, setListModal] = useState(false)
	const [dataRowListModal, setDataRowListModal] = useState([])
	const [isLoading, setIsLoading] = useState(false)
	const store = useUserStore((state) => state)

	const formik = useFormik({
		initialValues: {
			term_of_payment_id: null,
			term_of_payment_code: '',
			term_of_payment_name: '',
			term_of_payment_installment: 1,
			term_of_payment_interval: 0,
			term_of_payment_policy: '-',
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
		const storageTypeData = await getAllTermOfPayment()
		if (storageTypeData !== null) {
			setDataRowListModal(storageTypeData)
			setIsLoading(false)
			setListModal(true)
		}
	}
	const handleCloseListModal = () => {
		setListModal(false)
	}
	const handleOnDoubleClickListModal = (row: TermOfPaymentProps) => {
		if (row !== null) {
			formik.setFieldValue('term_of_payment_id', row.term_of_payment_id)
			formik.setFieldValue('is_active', row.is_active ? 'Active' : 'Deactive')
			formik.setFieldValue('term_of_payment_code', row.term_of_payment_code)
			formik.setFieldValue('term_of_payment_name', row.term_of_payment_name)
			formik.setFieldValue(
				'term_of_payment_installment',
				row.term_of_payment_installment
			)
			formik.setFieldValue(
				'term_of_payment_interval',
				row.term_of_payment_interval
			)
			formik.setFieldValue('term_of_payment_policy', row.term_of_payment_policy)
			setListModal(false)
		}
	}

	const handleDataRowIdListModal = (row: TermOfPaymentProps) => {
		return row.term_of_payment_id
	}

	const handleOnBlurTermOfPayment = async () => {
		setIsLoading(true)
		const TermOfPaymentData = await getTermOfPaymentById(
			formik.values.term_of_payment_code
		)

		if (TermOfPaymentData !== null) {
			formik.setFieldValue(
				'term_of_payment_id',
				TermOfPaymentData.term_of_payment_id
			)
			formik.setFieldValue(
				'is_active',
				TermOfPaymentData.is_active ? 'Active' : 'Deactive'
			)
			formik.setFieldValue(
				'term_of_payment_code',
				TermOfPaymentData.term_of_payment_code
			)
			formik.setFieldValue(
				'term_of_payment_name',
				TermOfPaymentData.term_of_payment_name
			)
			formik.setFieldValue(
				'term_of_payment_installment',
				TermOfPaymentData.term_of_payment_installment
			)
			formik.setFieldValue(
				'term_of_payment_interval',
				TermOfPaymentData.term_of_payment_interval
			)
			formik.setFieldValue(
				'term_of_payment_policy',
				TermOfPaymentData.term_of_payment_policy
			)
		}
		setIsLoading(false)
	}

	const activeButtonValue = () => {
		if (formik.values.term_of_payment_id === null) return true
		if (formik.values.is_active === 'Active') return true

		return false
	}

	const handleActiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Active')
	}

	const deactiveButtonValue = () => {
		if (formik.values.term_of_payment_id === null) return true
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
					disabled={formik.values.term_of_payment_id !== null}
					id='term_of_payment_code'
					label={
						<span>
							Top Code<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.term_of_payment_code}
					onChange={formik.handleChange}
					onBlur={handleOnBlurTermOfPayment}
					error={
						formik.touched.term_of_payment_code &&
						Boolean(formik.errors.term_of_payment_code)
					}
					helperText={
						formik.touched.term_of_payment_code &&
						formik.errors.term_of_payment_code
					}
				/>
				<TextFieldDMS
					id='term_of_payment_name'
					label={
						<span>
							Description{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.term_of_payment_name}
					onChange={formik.handleChange}
					error={
						formik.touched.term_of_payment_name &&
						Boolean(formik.errors.term_of_payment_name)
					}
					helperText={
						formik.touched.term_of_payment_name &&
						formik.errors.term_of_payment_name
					}
				/>
				<TextFieldDMS
					id='term_of_payment_policy'
					label={
						<span>
							Top Policy{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.term_of_payment_policy}
					onChange={formik.handleChange}
					error={
						formik.touched.term_of_payment_policy &&
						Boolean(formik.errors.term_of_payment_policy)
					}
					helperText={
						formik.touched.term_of_payment_policy &&
						formik.errors.term_of_payment_policy
					}
				/>
				<NumericFormat
					customInput={TextFieldDMS}
					thousandSeparator
					id='term_of_payment_installment'
					label={<span>Top Installment</span>}
					value={formik.values.term_of_payment_installment}
					onValueChange={(element) => {
						formik.setFieldValue(
							'term_of_payment_installment',
							element.floatValue,
							true
						)
					}}
					isAllowed={(values) => {
						const { floatValue } = values
						return floatValue < 1000 && floatValue > 0
					}}
					error={
						formik.touched.term_of_payment_installment &&
						Boolean(formik.errors.term_of_payment_installment)
					}
					helperText={
						formik.touched.term_of_payment_installment &&
						formik.errors.term_of_payment_installment
					}
				/>
				<NumericFormat
					customInput={TextFieldDMS}
					thousandSeparator
					id='term_of_payment_interval'
					label={<span>Top Interval</span>}
					value={formik.values.term_of_payment_interval}
					onValueChange={(element) => {
						formik.setFieldValue(
							'term_of_payment_interval',
							element.floatValue,
							true
						)
					}}
					isAllowed={(values) => {
						const { floatValue } = values
						return floatValue < 100000 && floatValue > -1
					}}
					error={
						formik.touched.term_of_payment_interval &&
						Boolean(formik.errors.term_of_payment_interval)
					}
					helperText={
						formik.touched.term_of_payment_interval &&
						formik.errors.term_of_payment_interval
					}
				/>
			</Box>
		</>
	)
}

export default TermOfPaymentMasterPage
