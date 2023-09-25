import {
	Autocomplete,
	Grid,
	TextField,
	Typography,
	useTheme,
} from '@mui/material'
import { Dispatch, SetStateAction, useState } from 'react'

interface DropDownListDMSProps {
	id: string
	label: JSX.Element
	disabled?: boolean
	error?: boolean
	helperText?: string
	optionData: any[]
	valueData: any
	onChangeValueData: Dispatch<SetStateAction<any>>
	getOptionLabel: (option: any) => string
	isOptionEqualToValue: (option: any, value: any) => boolean
}

const DropDownListDMS = (props: DropDownListDMSProps) => {
	const theme = useTheme()
	const DropDownListId = props.id
		.toString()
		.toLowerCase()
		.trim()
		.replace(/_+/g, '-')

	const [inputData, setinputData] = useState('')

	return (
		<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
			<Grid item xs={4}>
				<Typography
					sx={{ paddingBottom: props.error ? 'calc(8.5px + .75rem)' : '' }}
				>
					{props.label}
				</Typography>
			</Grid>
			<Grid item xs={8}>
				<Autocomplete
					size='small'
					disabled={props.disabled}
					fullWidth
					disablePortal
					aria-label={`drop_down_list_${DropDownListId}`}
					id={`drop_down_list_${DropDownListId}`}
					disableClearable
					getOptionLabel={props.getOptionLabel}
					isOptionEqualToValue={props.isOptionEqualToValue}
					value={props.valueData}
					onChange={(event, newValue: any | null) => {
						props.onChangeValueData(newValue)
					}}
					inputValue={inputData}
					onInputChange={(event, newInputValue: string) => {
						setinputData(newInputValue)
					}}
					options={props.optionData}
					sx={{
						width: '100%',
						display: 'inline-block',
						backgroundColor: props.disabled
							? 'secondary.main'
							: 'background.paper',
						borderRadius: '5px',
						WebkitTextFillColor: props.disabled
							? theme.palette.secondary.contrastText
							: '',
					}}
					slotProps={{
						popper: {
							sx: {
								zIndex: 1000,
							},
						},
					}}
					renderInput={(params) => (
						<TextField
							{...params}
							error={props.error}
							helperText={props.helperText}
							variant='outlined'
							inputProps={{
								...params.inputProps,
								'aria-label': `input-drop-down-list-${DropDownListId}`,
							}}
						/>
					)}
				/>
			</Grid>
		</Grid>
	)
}

export default DropDownListDMS
