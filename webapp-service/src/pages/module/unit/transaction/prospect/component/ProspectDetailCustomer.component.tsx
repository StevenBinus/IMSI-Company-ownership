import TextFieldDMS from '@components/TextFieldDMS.component'
import {
	Box,
	Button,
	Checkbox,
	Collapse,
	FormControlLabel,
	Grid,
	InputAdornment,
	useTheme,
} from '@mui/material'
import React, { useState } from 'react'
import AddBoxOutlinedIcon from '@mui/icons-material/AddBoxOutlined'
import IndeterminateCheckBoxOutlinedIcon from '@mui/icons-material/IndeterminateCheckBoxOutlined'
import Typography from '@mui/material/Typography'
import { NumericFormat, PatternFormat } from 'react-number-format'
import DatePickerDMS from '@components/DatePickerDMS.component'
import DropDownListDMS from '@components/DropDownListDMS.component'

type Props = {}

const ProspectDetailCustomer = (props: Props) => {
	const theme = useTheme()
	const [isActive, setIsActive] = useState(false)
	return (
		<Grid
			container
			direction='column'
			sx={{
				padding: '2% 0',
				borderRadius: '5px',
			}}
		>
			<Grid container item>
				<FormControlLabel
					checked={isActive}
					label='Customer Detail'
					onChange={() => setIsActive((prev) => !prev)}
					control={
						<Checkbox
							icon={<AddBoxOutlinedIcon />}
							checkedIcon={<IndeterminateCheckBoxOutlinedIcon />}
						/>
					}
				/>
			</Grid>
			<Grid container item>
				<Collapse
					in={isActive}
					unmountOnExit
					sx={{
						padding: '2%',
						width: '100%',
					}}
				>
					<TextFieldDMS id='address' label={<span>Address</span>} />
					<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
						<Grid item xs={4}>
							<Typography>Select Area</Typography>
						</Grid>
						<Grid item xs={8}>
							<Button
								variant='contained'
								color='primary'
								sx={{ minWidth: '0' }}
							>
								...
							</Button>
						</Grid>
					</Grid>
					<Box sx={{ paddingLeft: '30px' }}>
						<TextFieldDMS
							disabled
							id='kelurahan'
							label={<span>Kelurahan</span>}
						/>
						<TextFieldDMS
							disabled
							id='kecamatan'
							label={<span>Kecamatan</span>}
						/>
						<TextFieldDMS
							disabled
							id='kabupaten'
							label={<span>Kabupaten</span>}
						/>
						<TextFieldDMS
							disabled
							id='province'
							label={<span>Province</span>}
						/>
						<TextFieldDMS disabled id='city' label={<span>City</span>} />
						<TextFieldDMS
							disabled
							id='zip_code'
							label={<span> Zip Code</span>}
						/>
					</Box>
					<NumericFormat
						customInput={TextFieldDMS}
						allowLeadingZeros
						id='phone_no'
						label={<span>Phone No</span>}
					/>
					<NumericFormat
						customInput={TextFieldDMS}
						allowLeadingZeros
						id='fax_no'
						label={<span>Fax No</span>}
					/>
					<PatternFormat
						id='mobile_phone'
						label={<span>Mobile Phone</span>}
						customInput={TextFieldDMS}
						format='+62 #### #### ####'
						allowEmptyFormatting
					/>
					<TextFieldDMS
						id='email_address'
						type='email'
						label={<span>Email Address</span>}
					/>
					<Typography sx={{ paddingBottom: '10px', paddingTop: '20px' }}>
						Contact Person
					</Typography>
					<Box sx={{ paddingLeft: '30px' }}>
						<TextFieldDMS id='name' label={<span>Name</span>} />
						<DropDownListDMS
							id='gender'
							label={<span>Gender</span>}
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
							id='job_title'
							label={<span>Job Title</span>}
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
						<NumericFormat
							customInput={TextFieldDMS}
							allowLeadingZeros
							id='mobile_phone'
							label={<span>Mobile Phone</span>}
						/>
						<TextFieldDMS
							id='email_address'
							label={<span>Email Address</span>}
						/>
					</Box>
					<Typography sx={{ paddingBottom: '10px', paddingTop: '20px' }}>
						Customer Group
					</Typography>
					<Box sx={{ paddingLeft: '30px' }}>
						<DropDownListDMS
							id='bussiness_category'
							label={<span>Bussiness Category</span>}
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
							id='sub_category'
							label={<span>Sub Category</span>}
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
						<TextFieldDMS id='website' label={<span>Website</span>} />
					</Box>
					<Box sx={{ paddingBottom: '10px', paddingTop: '20px' }}>
						<DatePickerDMS
							id='buying_date_plan'
							label={<span>Buying Date Plan</span>}
							date={null}
						/>
					</Box>
				</Collapse>
			</Grid>
		</Grid>
	)
}

export default ProspectDetailCustomer
