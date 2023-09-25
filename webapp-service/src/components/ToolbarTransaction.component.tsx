import styled from '@emotion/styled'
import { AppBar, Button, Toolbar, ButtonProps, useTheme } from '@mui/material'
import ArrowCircleLeftIcon from '@mui/icons-material/ArrowCircleLeft'
import ArrowCircleRightIcon from '@mui/icons-material/ArrowCircleRight'
import DescriptionIcon from '@mui/icons-material/Description'
import SaveIcon from '@mui/icons-material/Save'
import ForwardToInboxIcon from '@mui/icons-material/ForwardToInbox'
import HighlightOffIcon from '@mui/icons-material/HighlightOff'
import LockIcon from '@mui/icons-material/Lock'
import PrintIcon from '@mui/icons-material/Print'

const ToolbarButton = styled(Button)<ButtonProps>(({ theme }) => ({
	textTransform: 'none',
}))

interface ToolbarTransactionProps {
	handleBackButton?: () => void
	DisableBackButton?: boolean
	handleNextButton?: () => void
	DisableNextButton?: boolean
	handleSaveButton?: () => void
	DisableSaveButton?: boolean
	handleNewButton?: () => void
	DisableNewButton?: boolean
	handleSubmitButton?: () => void
	DisableSubmitButton?: boolean
	handleVoidButton?: () => void
	DisableVoidButton?: boolean
	handleCloseOrderButton?: () => void
	DisableCloseOrderButton?: boolean
	handlePrintButton?: () => void
	DisablePrintButton?: boolean
}

const ToolbarTransaction = ({
	handleBackButton,
	DisableBackButton = false,
	handleNextButton,
	DisableNextButton = false,
	handleSaveButton,
	DisableSaveButton = false,
	handleNewButton,
	DisableNewButton = false,
	handleSubmitButton,
	DisableSubmitButton = false,
	handleVoidButton,
	DisableVoidButton = false,
	handleCloseOrderButton,
	DisableCloseOrderButton = false,
	handlePrintButton,
	DisablePrintButton = false,
}: ToolbarTransactionProps) => {
	const theme = useTheme()
	return (
		<AppBar
			position='sticky'
			sx={{
				top: '64px',
				zIndex: 1200 + 10,
				backgroundColor: theme.palette.background.paper,
				color: theme.palette.primary.main,
				// boxShadow: 'none',
				// borderBottom: `1px solid ${theme.palette.primary.main}`,
			}}
		>
			<Toolbar sx={{ minHeight: '0 !important' }}>
				<ToolbarButton
					disabled={DisableBackButton}
					onClick={handleBackButton}
					color='inherit'
				>
					<ArrowCircleLeftIcon /> Back
				</ToolbarButton>
				<ToolbarButton
					disabled={DisableNextButton}
					onClick={handleNextButton}
					color='inherit'
				>
					<ArrowCircleRightIcon /> Next
				</ToolbarButton>
				<ToolbarButton
					disabled={DisableNewButton}
					onClick={handleNewButton}
					color='inherit'
				>
					<DescriptionIcon /> New
				</ToolbarButton>
				<ToolbarButton
					disabled={DisableSaveButton}
					onClick={handleSaveButton}
					color='inherit'
				>
					<SaveIcon /> Save
				</ToolbarButton>
				<ToolbarButton
					disabled={DisableSubmitButton}
					onClick={handleSubmitButton}
					color='inherit'
				>
					<ForwardToInboxIcon /> Submit
				</ToolbarButton>
				<ToolbarButton
					disabled={DisableVoidButton}
					onClick={handleVoidButton}
					color='inherit'
				>
					<HighlightOffIcon /> Void
				</ToolbarButton>
				<ToolbarButton
					disabled={DisableCloseOrderButton}
					onClick={handleCloseOrderButton}
					color='inherit'
				>
					<LockIcon /> Close Order
				</ToolbarButton>
				<ToolbarButton
					disabled={DisablePrintButton}
					onClick={handlePrintButton}
					color='inherit'
				>
					<PrintIcon /> Print
				</ToolbarButton>
			</Toolbar>
		</AppBar>
	)
}

export default ToolbarTransaction
