import {
	Box,
	Grid,
	TextField,
	TextFieldProps,
	Typography,
	useTheme,
} from '@mui/material'
import { DatePicker, LocalizationProvider } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import { Dayjs } from 'dayjs'
import React from 'react'

type DatePickerDMSProps = {
	date: Dayjs | null
	setDate?: (date: Dayjs | null) => void
	disableFuture?: boolean
} & TextFieldProps

const DatePickerDMS = (props: DatePickerDMSProps) => {
	const theme = useTheme()
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
				<LocalizationProvider dateAdapter={AdapterDayjs}>
					<DatePicker
						disableFuture={props.disableFuture}
						disabled={props.disabled}
						value={props.date}
						inputFormat='DD/MM/YYYY'
						onChange={(newValue) => {
							props.setDate(newValue)
						}}
						renderInput={({ inputRef, inputProps, InputProps }) => (
							<Box
								ref={inputRef}
								sx={{ display: 'flex', alignItems: 'center' }}
							>
								<TextField
									disabled={props.disabled}
									fullWidth
									size='small'
									label=''
									inputProps={inputProps}
									ref={inputRef}
									sx={{
										'& .MuiInputBase-input.Mui-disabled': {
											WebkitTextFillColor: theme.palette.secondary.contrastText,
											backgroundColor: theme.palette.secondary.main,
										},
									}}
								/>
								{InputProps?.endAdornment}
							</Box>
						)}
					/>
				</LocalizationProvider>
			</Grid>
		</Grid>
	)
}

export default DatePickerDMS
