import {
	Grid,
	TextField,
	TextFieldProps,
	Typography,
	useTheme,
} from '@mui/material'

const TextFieldDMS = (props: TextFieldProps) => {
	const theme = useTheme()
	return (
		<Grid container alignItems='flex-start' sx={{ paddingBottom: '10px' }}>
			<Grid container item alignItems='center' xs={4}>
				<Typography
					sx={{
						paddingBottom: props.error ? 'calc(8.5px + .75rem)' : '',
						paddingTop: '8.5px',
					}}
				>
					{props.label}
				</Typography>
			</Grid>
			<Grid container item xs={8}>
				<TextField
					{...props}
					fullWidth
					size='small'
					label=''
					inputProps={{
						'aria-label': `textfield-dms-${props.id
							.toString()
							.toLowerCase()
							.trim()
							.replace(/_+/g, '-')}`,
					}}
					sx={{
						'& .MuiInputBase-input.Mui-disabled': {
							WebkitTextFillColor: theme.palette.secondary.contrastText,
							backgroundColor: theme.palette.secondary.main,
						},
					}}
				/>
			</Grid>
		</Grid>
	)
}

export default TextFieldDMS
