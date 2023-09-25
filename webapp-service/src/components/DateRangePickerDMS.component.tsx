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

type DateRangePickerDMSProps = {
	dateFrom: Dayjs | null
	setDateFrom?: (date: Dayjs | null) => void
	dateTo: Dayjs | null
	setDateTo?: (date: Dayjs | null) => void
} & TextFieldProps

const DateRangePickerDMS = (props: DateRangePickerDMSProps) => {
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
			<Grid item xs={3.5}>
				<LocalizationProvider dateAdapter={AdapterDayjs}>
					<DatePicker
						value={props.dateFrom}
						inputFormat='DD/MM/YYYY'
						onChange={(newValue) => {
							if (props.dateFrom <= newValue) {
								props.setDateTo(newValue)
							}
							props.setDateFrom(newValue)
						}}
						renderInput={({ inputRef, inputProps, InputProps }) => (
							<Box
								ref={inputRef}
								sx={{ display: 'flex', alignItems: 'center' }}
							>
								<TextField
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
			<Grid container item xs={1} justifyContent='center'>
				<Typography>to</Typography>
			</Grid>
			<Grid item xs={3.5}>
				<LocalizationProvider dateAdapter={AdapterDayjs}>
					<DatePicker
						value={props.dateTo}
						minDate={props.dateFrom}
						inputFormat='DD/MM/YYYY'
						onChange={(newValue) => {
							props.setDateTo(newValue)
						}}
						renderInput={({ inputRef, inputProps, InputProps }) => (
							<Box
								ref={inputRef}
								sx={{ display: 'flex', alignItems: 'center' }}
							>
								<TextField
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

export default DateRangePickerDMS
