import TextFieldDMS from '@components/TextFieldDMS.component'
import {
	Box,
	Checkbox,
	Collapse,
	FormControlLabel,
	Grid,
	useTheme,
} from '@mui/material'
import React, { useState } from 'react'
import AddBoxOutlinedIcon from '@mui/icons-material/AddBoxOutlined'
import IndeterminateCheckBoxOutlinedIcon from '@mui/icons-material/IndeterminateCheckBoxOutlined'
import { NumericFormat } from 'react-number-format'
import DropDownListDMS from '@components/DropDownListDMS.component'

type Props = {}

const ProspectDetailFinancing = (props: Props) => {
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
					label='Financing'
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
					<DropDownListDMS
						id='payment_type'
						label={<span>Payment Type</span>}
						optionData={[]}
						valueData={undefined}
						onChangeValueData={function (value: any): void {
							throw new Error('Function not implemented.')
						}}
						getOptionLabel={function (option: any): string {
							throw new Error('Function not implemented.')
						}}
						isOptionEqualToValue={function (option: any, value: any): boolean {
							throw new Error('Function not implemented.')
						}}
					/>
					<NumericFormat
						customInput={TextFieldDMS}
						allowLeadingZeros
						id='retail_price_per_unit'
						label={<span>Retail Price per Unit</span>}
					/>
					<NumericFormat
						customInput={TextFieldDMS}
						allowLeadingZeros
						id='request_discount'
						label={<span>Request Discount</span>}
					/>
					<NumericFormat
						customInput={TextFieldDMS}
						allowLeadingZeros
						id='down_payment_budget'
						label={<span>Down Payment Budget</span>}
					/>
				</Collapse>
			</Grid>
		</Grid>
	)
}

export default ProspectDetailFinancing
