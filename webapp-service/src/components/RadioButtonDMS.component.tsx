import {
	FormControl,
	FormControlLabel,
	Grid,
	Radio,
	RadioGroup,
	Typography,
} from '@mui/material'
import { ChangeEvent } from 'react'

interface RadioButtonDMSProps {
	id?: string
	label?: JSX.Element
	value?: any
	error?: boolean
	row?: boolean
	handleChangeValue?: (
		event: ChangeEvent<HTMLInputElement>,
		value: string
	) => void
	listValue?: { value: any; label: any }[]
}

const RadioButtonDMS = (props: RadioButtonDMSProps) => {
	return (
		<Grid container sx={{ paddingBottom: '10px' }}>
			<Grid container item xs={4}>
				<Typography
					sx={{
						paddingBottom: props.error ? 'calc(8.5px + .75rem)' : '',
						paddingTop: '9px',
					}}
				>
					{props.label}
				</Typography>
			</Grid>
			<Grid container item xs={8}>
				<FormControl>
					<RadioGroup
						aria-labelledby='demo-controlled-radio-buttons-group'
						name='controlled-radio-buttons-group'
						row={props.row}
						value={props.value}
						onChange={props.handleChangeValue}
					>
						{props.listValue.map((data, key) => (
							<FormControlLabel
								key={key}
								value={data.value}
								control={<Radio />}
								label={data.label}
							/>
						))}
					</RadioGroup>
				</FormControl>
			</Grid>
		</Grid>
	)
}

export default RadioButtonDMS
