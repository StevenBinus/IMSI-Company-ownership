import DropDownListDMS from '@components/DropDownListDMS.component'
import ListModal from '@components/ListModal.component'
import PageLoad from '@components/PageLoad.component'
import SkeletonLoad from '@components/SkeletonLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarMaster from '@components/ToolbarMaster.component'
import { Box, useTheme } from '@mui/material'
import { GridColDef } from '@mui/x-data-grid'
import useUserStore from '@utils/store.util'
import { useFormik } from 'formik'
import React, { useState } from 'react'
import { NumericFormat } from 'react-number-format'
import { number, object, string } from 'yup'
import {
	CashFlowCodeListProps,
	getAllCashFlowCode,
} from './api/getAllCashFlowCode.api'
import {
	CashFlowGroupProps,
	useGetAllCashFlowGroup,
} from './api/getAllCashFlowGroup.api'
import {
	CashFlowGroupDetailProps,
	useGetAllCashFlowGroupDetail,
} from './api/getAllCashFlowGroupDetail.api'
import {
	CashFlowTypeProps,
	useGetAllCashFlowType,
} from './api/getAllCashFlowType.api'
import { getCashFlowCodeById } from './api/getCashFlowCodeById.api'

const validationSchema = object({
	cash_flow_type_id: string().required('Cash Flow Type is required'),
	cash_flow_group_id: string().required('Cash Flow Group is required'),
	cash_flow_group_detail_id: string().required('Table Key 1 Type is required'),
	cash_flow_code: string().required('Cash Flow Code is required'),
	sequence_number: number()
		.integer('Sequence Number must be a number')
		.required('Sequence Number is required'),
	is_active: string().required('Record Status is required'),
})

const dataGridColumns: GridColDef[] = [
	{
		field: 'cash_flow_code',
		headerName: 'Code',
		flex: 2,
	},
	{
		field: 'cash_flow_type',
		headerName: 'Type',
		flex: 1,
	},
	{
		field: 'cash_flow_group',
		headerName: 'Cash Flow Table Key',
		flex: 3,
	},
	{
		field: 'cash_flow_group_detail',
		headerName: 'Cash Flow Table Key Desc.',
		flex: 4,
	},
]

const CashFlowCodeMasterPage = () => {
	const theme = useTheme()
	const [listModal, setListModal] = useState(false)
	const [dataRowListModal, setDataRowListModal] = useState([])
	const [isLoading, setIsLoading] = useState(false)

	const store = useUserStore((state) => state)

	const { dataCashFlowType, isLoadingCashFlowType } = useGetAllCashFlowType()
	const { dataCashFlowGroup, isLoadingCashFlowGroup } = useGetAllCashFlowGroup()
	const { dataCashFlowGroupDetail, isLoadingCashFlowGroupDetail } =
		useGetAllCashFlowGroupDetail()

	const formik = useFormik({
		initialValues: {
			cash_flow_code_id: null,
			cash_flow_code: '',
			cash_flow_code_description: '',
			cash_flow_type_id: null,
			cash_flow_group_id: null,
			cash_flow_group_detail_id: null,
			sequence_number: 0,
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
		const storageTypeData = await getAllCashFlowCode()
		if (storageTypeData !== null) {
			setDataRowListModal(storageTypeData)
			setIsLoading(false)
			setListModal(true)
		}
	}
	const handleCloseListModal = () => {
		setListModal(false)
	}

	const handleOnDoubleClickListModal = async (row: CashFlowCodeListProps) => {
		setListModal(false)
		setIsLoading(true)
		const companyOwnershipData = await getCashFlowCodeById(
			row.cash_flow_code.toString()
		)
		if (companyOwnershipData !== null) {
			formik.setFieldValue(
				'is_active',
				companyOwnershipData.is_active ? 'Active' : 'Deactive'
			)
			formik.setFieldValue(
				'cash_flow_code_id',
				companyOwnershipData.cash_flow_code_id
			)
			formik.setFieldValue(
				'cash_flow_code',
				companyOwnershipData.cash_flow_code
			)
			formik.setFieldValue(
				'cash_flow_code_description',
				companyOwnershipData.cash_flow_code_description
			)
			formik.setFieldValue(
				'cash_flow_type_id',
				companyOwnershipData.cash_flow_type_id
			)
			formik.setFieldValue(
				'cash_flow_group_id',
				companyOwnershipData.cash_flow_group_id
			)
			formik.setFieldValue(
				'cash_flow_group_detail_id',
				companyOwnershipData.cash_flow_group_detail_id
			)
			formik.setFieldValue(
				'sequence_number',
				companyOwnershipData.sequence_number
			)
		}
		setIsLoading(false)
	}

	const handleDataRowIdListModal = (row: CashFlowCodeListProps) => {
		return row.cash_flow_code_id
	}

	const activeButtonValue = () => {
		if (formik.values.cash_flow_code_id === null) return true
		if (formik.values.is_active === 'Active') return true

		return false
	}

	const handleActiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Active')
	}

	const deactiveButtonValue = () => {
		if (formik.values.cash_flow_code_id === null) return true
		if (formik.values.is_active === 'Deactive') return true

		return false
	}
	const handleDeactiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Deactive')
	}

	const handleOnBlurCompanyOwnershipType = async () => {
		setIsLoading(true)
		const companyOwnershipData = await getCashFlowCodeById(
			formik.values.cash_flow_code
		)
		if (companyOwnershipData !== null) {
			formik.setFieldValue(
				'is_active',
				companyOwnershipData.is_active ? 'Active' : 'Deactive'
			)
			formik.setFieldValue(
				'cash_flow_code_id',
				companyOwnershipData.cash_flow_code_id
			)
			formik.setFieldValue(
				'cash_flow_code',
				companyOwnershipData.cash_flow_code
			)
			formik.setFieldValue(
				'cash_flow_code_description',
				companyOwnershipData.cash_flow_code_description
			)
			formik.setFieldValue(
				'cash_flow_type_id',
				companyOwnershipData.cash_flow_type_id
			)
			formik.setFieldValue(
				'cash_flow_group_id',
				companyOwnershipData.cash_flow_group_id
			)
			formik.setFieldValue(
				'cash_flow_group_detail_id',
				companyOwnershipData.cash_flow_group_detail_id
			)
			formik.setFieldValue(
				'sequence_number',
				companyOwnershipData.sequence_number
			)
		}
		setIsLoading(false)
	}

	if (
		isLoadingCashFlowType ||
		isLoadingCashFlowGroup ||
		isLoadingCashFlowGroupDetail
	) {
		return <SkeletonLoad />
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
				<DropDownListDMS
					label={
						<span>
							Cash Flow Type{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					error={
						formik.touched.cash_flow_type_id &&
						Boolean(formik.errors.cash_flow_type_id)
					}
					helperText={
						formik.touched.cash_flow_type_id &&
						(formik.errors.cash_flow_type_id as string)
					}
					optionData={dataCashFlowType}
					valueData={formik.values.cash_flow_type_id}
					onChangeValueData={(data: CashFlowTypeProps) => {
						formik.setFieldValue('cash_flow_type_id', data.cash_flow_type_id)
					}}
					id={'cash_flow_type'}
					getOptionLabel={(option: any) => {
						if (typeof option !== 'object') {
							const cash_flow_type_result = dataCashFlowType.find(
								(data) => data.cash_flow_type_id === option
							)
							return cash_flow_type_result.cash_flow_type ?? ''
						}
						return option.cash_flow_type
					}}
					isOptionEqualToValue={(option: any, value: any) => {
						return option.cash_flow_type_id === value
					}}
				/>

				<DropDownListDMS
					label={
						<span>
							Cash Flow Group{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					error={
						formik.touched.cash_flow_group_id &&
						Boolean(formik.errors.cash_flow_group_id)
					}
					helperText={
						formik.touched.cash_flow_group_id &&
						(formik.errors.cash_flow_group_id as string)
					}
					optionData={dataCashFlowGroup}
					valueData={formik.values.cash_flow_group_id}
					onChangeValueData={(data: CashFlowGroupProps) => {
						formik.setFieldValue('cash_flow_group_id', data.cash_flow_group_id)
					}}
					id={'cash_flow_group'}
					getOptionLabel={(option: any) => {
						if (typeof option !== 'object') {
							const cash_flow_group_result = dataCashFlowGroup.find(
								(data) => data.cash_flow_group_id === option
							)
							return cash_flow_group_result.cash_flow_group ?? ''
						}
						return option.cash_flow_group
					}}
					isOptionEqualToValue={(option: any, value: any) => {
						return option.cash_flow_group_id === value
					}}
				/>

				<DropDownListDMS
					label={
						<span>
							Table Key 1{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					error={
						formik.touched.cash_flow_group_detail_id &&
						Boolean(formik.errors.cash_flow_group_detail_id)
					}
					helperText={
						formik.touched.cash_flow_group_detail_id &&
						(formik.errors.cash_flow_group_detail_id as string)
					}
					optionData={dataCashFlowGroupDetail}
					valueData={formik.values.cash_flow_group_detail_id}
					onChangeValueData={(data: CashFlowGroupDetailProps) => {
						formik.setFieldValue(
							'cash_flow_group_detail_id',
							data.cash_flow_group_detail_id
						)
					}}
					id={'cash_flow_group_detail'}
					getOptionLabel={(option: any) => {
						if (typeof option !== 'object') {
							const cash_flow_group_detail_result =
								dataCashFlowGroupDetail.find(
									(data) => data.cash_flow_group_detail_id === option
								)
							return cash_flow_group_detail_result.cash_flow_group_detail ?? ''
						}
						return option.cash_flow_group_detail
					}}
					isOptionEqualToValue={(option: any, value: any) => {
						return option.cash_flow_group_detail_id === value
					}}
				/>
				<TextFieldDMS
					id='cash_flow_code'
					disabled={formik.values.cash_flow_code_id !== null}
					label={
						<span>
							Cash Flow Code{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.cash_flow_code}
					onChange={formik.handleChange}
					onBlur={handleOnBlurCompanyOwnershipType}
					error={
						formik.touched.cash_flow_code &&
						Boolean(formik.errors.cash_flow_code)
					}
					helperText={
						formik.touched.cash_flow_code && formik.errors.cash_flow_code
					}
				/>
				<NumericFormat
					customInput={TextFieldDMS}
					thousandSeparator
					id='sequence_number'
					label={
						<span>
							Sequence No.{' '}
							<span style={{ color: theme.palette.error.main }}>*</span>
						</span>
					}
					value={formik.values.sequence_number}
					onValueChange={(element) => {
						if (element.floatValue === undefined) {
							formik.setFieldValue('sequence_number', 0, true)
						} else {
							formik.setFieldValue('sequence_number', element.floatValue, true)
						}
					}}
					error={
						formik.touched.sequence_number &&
						Boolean(formik.errors.sequence_number)
					}
					helperText={
						formik.touched.sequence_number && formik.errors.sequence_number
					}
				/>
				<TextFieldDMS
					id='cash_flow_code_description'
					disabled={formik.values.sequence_number < 1}
					label={<span>Description</span>}
					value={formik.values.cash_flow_code_description}
					onChange={formik.handleChange}
					error={
						formik.touched.cash_flow_code_description &&
						Boolean(formik.errors.cash_flow_code_description)
					}
					helperText={
						formik.touched.cash_flow_code_description &&
						formik.errors.cash_flow_code_description
					}
				/>
			</Box>
		</>
	)
}

export default CashFlowCodeMasterPage
