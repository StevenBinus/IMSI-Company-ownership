import DatePickerDMS from '@components/DatePickerDMS.component'
import TextFieldDMS from '@components/TextFieldDMS.component'
import TextFieldLookUpDMS from '@components/TextFieldLookUpDMS.component'
import {
	Box,
	Button,
	Dialog,
	DialogActions,
	DialogContent,
} from '@mui/material'
import { useState } from 'react'
import SaveIcon from '@mui/icons-material/Save'

interface VehicleModalProps {
	open: boolean
	handleClose: () => void
}

const VehicleModal = (props: VehicleModalProps) => {
	const [isFullscreen, setIsFullscreen] = useState(false)

	const handleFullscreenButton = () => {
		setIsFullscreen((isFullscreen) => !isFullscreen)
	}

	return (
		<Dialog
			maxWidth={false}
			open={props.open}
			onClose={props.handleClose}
			fullScreen={isFullscreen}
			aria-labelledby='list-modal-label'
			aria-describedby='list-modal-description'
			sx={{ zIndex: 1200 + 40 }}
		>
			<DialogActions sx={{ padding: '20px 20px 0 20px' }}>
				<Button onClick={handleFullscreenButton}>Fullscreen</Button>
				<Button onClick={props.handleClose}>Close</Button>
			</DialogActions>
			<DialogContent sx={{ padding: '0 20px 20px 20px' }}>
				<Box
					sx={{
						width: '90%',
						minWidth: '600px',
						backgroundColor: 'background.paper',
						boxShadow: '24px',
						padding: '4px',
					}}
				>
					<TextFieldDMS
						id='record_status'
						disabled
						value={'Active'}
						label={<span>Record Status</span>}
					/>
					<DatePickerDMS
						id='follow_up_date'
						label={<span>Follow Up Date</span>}
						date={null}
					/>
					<TextFieldLookUpDMS
						id='follow_up_code'
						label={<span>Follow Up Code</span>}
						dataColumn={[]}
						dataRow={[]}
						handleDataRowId={() => {
							return 1
						}}
						handleOnDoubleClick={() => {}}
						handleOnBlur={() => {}}
						listModal={false}
						handleCloseListModal={function (): void {
							throw new Error('Function not implemented.')
						}}
						handleOpenListModal={function (): void {
							throw new Error('Function not implemented.')
						}}
					/>
					<TextFieldDMS
						id='follow_up_note'
						multiline
						minRows={3}
						label={<span>Follow Up Note</span>}
					/>
					<DatePickerDMS
						id='result_date'
						label={<span>Result Date</span>}
						date={null}
					/>
					<TextFieldDMS
						id='result_note'
						multiline
						minRows={3}
						label={<span>Result Note</span>}
					/>
					<Box
						sx={{ width: '100%', justifyContent: 'flex-end', display: 'flex' }}
					>
						<Button
							disabled
							onClick={() => {}}
							variant='contained'
							startIcon={<SaveIcon />}
						>
							Ok
						</Button>
					</Box>
				</Box>
			</DialogContent>
		</Dialog>
	)
}

export default VehicleModal
