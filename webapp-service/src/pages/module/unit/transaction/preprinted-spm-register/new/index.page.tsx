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
} from '../api/getSPMRegisterDetail.api'
import { number, object, string } from 'yup'
import { postSPMRegister } from '../api/postSPMRegister.api'
import { AxiosError } from 'axios'

const validationSchema = object({
	spm_number_format: string().required('Spm Form Format'),
	spm_number_from: number()
		.required('Start SPM Form Seq. is required')
		.positive('Total SPM Form must be a positive value')
		.min(1, 'Total SPM Form must be larger than 0'),
	total_spm: number()
		.required('Total SPM Form is required')
		.positive('Total SPM Form must be a positive value')
		.min(1, 'Total SPM Form must be larger than 0'),
})

export const dataColumnSPMFormNumber: GridColDef[] = [
	{
		field: 'spm_number',
		headerName: 'No.',
		flex: 1,
	},
	{
		field: 'spm_form_number',
		headerName: 'SPM Form No.',
		flex: 2,
	},
]

const NewSPMRegisterPage = () => {
	const theme = useTheme()
	const router = useRouter()
	const store = useUserStore((state) => state)

	const formik = useFormik({
		initialValues: {
			company_id: store.userStore.company,
			register_document_number: '',
			spm_received_date: dayjs(Date.now()),
			spm_received_by: 'Designater User',
			spm_number_format: '',
			spm_number_from: 0,
			total_spm: 0,
			list_spm: [],
		},
		validationSchema: validationSchema,
		onSubmit: (values) => {
			postSPMRegister({
				company_id: values.company_id,
				spm_received_by: values.spm_received_by,
				spm_received_date: values.spm_received_date.toISOString(),
				spm_number_format: values.spm_number_format,
				spm_number_from: values.spm_number_from,
				total_spm: values.total_spm,
				reference_document_number: '',
			})
				.then((response) => {
					console.log(response)
					router.push(
						`/module/unit/transaction/preprinted-spm-register/${response.data.register_system_number}`
					)
				})
				.catch((error: AxiosError) => {
					alert(error.message)
				})
		},
	})

	const handleBackButton = () => {
		router.push(`/module/unit/transaction/preprinted-spm-register`)
	}

	const handleSaveButton = () => {}

	return (
		<>
			<PageLoad loading={false} />
			<ToolbarTransaction
				handleBackButton={handleBackButton}
				handleSaveButton={handleSaveButton}
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
						id='spm_number_format'
						label={<span>Spm Form Format</span>}
						value={formik.values.spm_number_format}
						onChange={formik.handleChange}
						error={
							formik.touched.spm_number_format &&
							Boolean(formik.errors.spm_number_format)
						}
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
						error={
							formik.touched.spm_number_from &&
							Boolean(formik.errors.spm_number_from)
						}
						helperText={
							formik.touched.spm_number_from && formik.errors.spm_number_from
						}
					/>
					<NumericFormat
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
						error={formik.touched.total_spm && Boolean(formik.errors.total_spm)}
						helperText={formik.touched.total_spm && formik.errors.total_spm}
					/>

					<Grid container item justifyContent='flex-end'>
						<Button
							onClick={formik.submitForm}
							variant='contained'
							startIcon={<SettingsIcon />}
						>
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

export default NewSPMRegisterPage
