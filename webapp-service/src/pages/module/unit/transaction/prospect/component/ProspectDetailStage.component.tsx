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
type Props = {}

const ProspectDetailStage = (props: Props) => {
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
					label='Stage'
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
					<TextFieldDMS disabled id='cc' label={<span>CC</span>} />
					<TextFieldDMS disabled id='ch' label={<span>CH</span>} />
					<TextFieldDMS disabled id='spm_date' label={<span>SPM Date</span>} />
					<TextFieldDMS disabled id='spm_no' label={<span>SPM No</span>} />
				</Collapse>
			</Grid>
		</Grid>
	)
}

export default ProspectDetailStage
