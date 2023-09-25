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
import DropDownListDMS from '@components/DropDownListDMS.component'

type Props = {}

const ProspectDetailOther = (props: Props) => {
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
					label='Other'
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
						id='change_sales_rep'
						label={<span>Change Sales Rep. To</span>}
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
					<TextFieldDMS id='reference' label={<span>Reference</span>} />
					<TextFieldDMS
						id='notes'
						multiline
						minRows={4}
						label={<span>Notes</span>}
					/>
				</Collapse>
			</Grid>
		</Grid>
	)
}

export default ProspectDetailOther
