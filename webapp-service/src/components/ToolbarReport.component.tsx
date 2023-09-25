import styled from '@emotion/styled'
import { AppBar, Button, Toolbar, ButtonProps, useTheme } from '@mui/material'
import DescriptionIcon from '@mui/icons-material/Description'
import PrintIcon from '@mui/icons-material/Print'
import SettingsIcon from '@mui/icons-material/Settings'

const ToolbarButton = styled(Button)<ButtonProps>(({ theme }) => ({
	textTransform: 'none',
}))

interface ToolbarReportProps {
	handleNewButton?: () => void
	DisableNewButton?: boolean
	handleProcessButton?: () => void
	DisableProcessButton?: boolean
	handlePrintButton?: () => void
	DisablePrintButton?: boolean
}

const ToolbarReport = ({
	handleNewButton,
	DisableNewButton = false,
	handleProcessButton,
	DisableProcessButton = false,
	handlePrintButton,
	DisablePrintButton = false,
}: ToolbarReportProps) => {
	const theme = useTheme()
	return (
		<AppBar
			position='sticky'
			sx={{
				top: '64px',
				zIndex: 1200 + 10,
				backgroundColor: theme.palette.background.paper,
				color: theme.palette.primary.main,
			}}
		>
			<Toolbar sx={{ minHeight: '0 !important' }}>
				<ToolbarButton
					disabled={DisableNewButton}
					onClick={handleNewButton}
					color='inherit'
				>
					<DescriptionIcon /> New
				</ToolbarButton>
				<ToolbarButton
					disabled={DisableProcessButton}
					onClick={handleProcessButton}
					color='inherit'
				>
					<SettingsIcon /> Process
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

export default ToolbarReport
