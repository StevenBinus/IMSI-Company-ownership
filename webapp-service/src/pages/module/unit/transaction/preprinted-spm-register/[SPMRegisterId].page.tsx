import DatePickerDMS from '@components/DatePickerDMS.component'
import PageLoad from '@components/PageLoad.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarTransaction from '@components/ToolbarTransaction.component'
import { Button, Grid, Typography, useTheme } from '@mui/material'
import SettingsIcon from '@mui/icons-material/Settings'
import { useRouter } from 'next/router'
import { useFormik } from 'formik'
import dayjs from 'dayjs'
import useUserStore from '@utils/store.util'
import { NumericFormat } from 'react-number-format'
import DataGridDMS from '@components/DataGridDMS.component'
import { GridColDef } from '@mui/x-data-grid'
import {
	SPMRegisterDetailListProps,
	SPMRegisterDetailProps,
	getSPMRegisterDetail,
} from './api/getSPMRegisterDetail.api'
import { useEffect } from 'react'
import { AxiosError } from 'axios'

export const dataColumnSPMFormNumber: GridColDef[] = [
	{
		field: 'spm_form_registration_detail_id',
		headerName: 'No.',
		flex: 1,
	},
	{
		field: 'spm_document_number',
		headerName: 'SPM Form No.',
		flex: 2,
	},
]

const SPMRegisterDetailPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const { SPMRegisterId } = router.query
	const store = useUserStore((state) => state)

	const formik = useFormik({
		initialValues: {
			reference_document_number: SPMRegisterId,
			company_id: store.userStore.company,
			register_document_number: '',
			spm_received_date: dayjs(Date.now()),
			spm_received_by: '',
			spm_number_format: '',
			spm_number_from: 0,
			total_spm: 0,
			list_spm: [],
		},
		onSubmit: (values) => {
			alert(JSON.stringify(values, null, 2))
		},
	})

	useEffect(() => {
		if (SPMRegisterId) {
			getSPMRegisterDetail(Number(SPMRegisterId))
				.then((response) => {
					formik.setFieldValue('company_id', response.data.company_id, true)
					formik.setFieldValue(
						'register_document_number',
						response.data.register_document_number,
						true
					)
					formik.setFieldValue(
						'spm_received_by',
						response.data.spm_received_by,
						true
					)
					formik.setFieldValue(
						'spm_received_date',
						response.data.spm_received_date,
						true
					)
					formik.setFieldValue(
						'spm_number_format',
						response.data.spm_number_format,
						true
					)
					formik.setFieldValue(
						'spm_number_from',
						response.data.spm_number_from,
						true
					)
					formik.setFieldValue('total_spm', response.data.total_spm, true)
					formik.setFieldValue('list_spm', response.data.list_spm, true)
				})
				.catch((error: AxiosError) => {
					alert(error.message)
				})
		}
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, [])

	const handleBackButton = () => {
		router.push(`/module/unit/transaction/preprinted-spm-register`)
	}

	const handleSaveButton = async () => {
		await getSPMRegisterDetail(Number(SPMRegisterId))
			.then((response) => {
				formik.setFieldValue('company_id', response.data.company_id, true)
				formik.setFieldValue(
					'register_document_number',
					response.data.register_document_number,
					true
				)
				formik.setFieldValue(
					'spm_received_by',
					response.data.spm_received_by,
					true
				)
				formik.setFieldValue(
					'spm_received_date',
					response.data.spm_received_date,
					true
				)
				formik.setFieldValue(
					'spm_number_format',
					response.data.spm_number_format,
					true
				)
				formik.setFieldValue(
					'spm_number_from',
					response.data.spm_number_from,
					true
				)
				formik.setFieldValue('total_spm', response.data.total_spm, true)
				formik.setFieldValue('list_spm', response.data.list_spm, true)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
			})
	}

	return (
		<>
			<PageLoad loading={false} />
			<ToolbarTransaction
				handleBackButton={handleBackButton}
				handleSaveButton={handleSaveButton}
				DisableSaveButton
				DisableCloseOrderButton
				DisableNextButton
				DisableNewButton
				DisablePrintButton
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
					<TextFieldDMS
						disabled
						id='company_id'
						label={<span>Company</span>}
						value={formik.values.company_id}
					/>
					<TextFieldDMS
						disabled
						id='register_document_number'
						label={<span>Register Doc No</span>}
						value={formik.values.register_document_number}
					/>
					<DatePickerDMS
						disabled
						id='spm_received_date'
						label={<span>Received Date</span>}
						date={formik.values.spm_received_date}
					/>
					<TextFieldDMS
						disabled
						id='spm_received_by'
						label={<span>Received By</span>}
						value={formik.values.spm_received_by}
					/>
					<TextFieldDMS
						disabled
						id='spm_number_format'
						label={<span>Spm Form Format</span>}
						value={formik.values.spm_number_format}
						helperText={
							<>
								SPM Format Keyword
								<br />
								@M2 Transaction Month MM Format
								<br />
								@M3 Transaction Month name abbreviation 3 digit format
								<br />
								@Nx x = Number of digit 1-9 for Last No
								<br />
								@Y2 Transaction Year YY Format
								<br />
								@Y2 Transaction Year YY Format
								<br />
								@Y4 Transaction Year YYYY FormatSPM Format Keyword
							</>
						}
					/>
					<NumericFormat
						disabled
						customInput={TextFieldDMS}
						thousandSeparator
						id='spm_number_from'
						label={<span>Start SPM Form Seq.</span>}
						value={formik.values.spm_number_from}
						onValueChange={(element) => {
							if (element.floatValue === undefined) {
								formik.setFieldValue('spm_number_from', 0, true)
							} else {
								formik.setFieldValue(
									'spm_number_from',
									element.floatValue,
									true
								)
							}
						}}
					/>
					<NumericFormat
						disabled
						customInput={TextFieldDMS}
						thousandSeparator
						id='total_spm'
						label={<span>Total SPM Form</span>}
						value={formik.values.total_spm}
						onValueChange={(element) => {
							if (element.floatValue === undefined) {
								formik.setFieldValue('total_spm', 0, true)
							} else {
								formik.setFieldValue('total_spm', element.floatValue, true)
							}
						}}
					/>

					<Grid container item justifyContent='flex-end'>
						<Button disabled variant='contained' startIcon={<SettingsIcon />}>
							Generate
						</Button>
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
					<DataGridDMS
						pageSize={5}
						getRowId={(row: SPMRegisterDetailListProps) => {
							return row.spm_form_registration_detail_id
						}}
						columns={dataColumnSPMFormNumber}
						rows={formik.values.list_spm}
					/>
				</Grid>
			</Grid>
		</>
	)
}

export default SPMRegisterDetailPage
