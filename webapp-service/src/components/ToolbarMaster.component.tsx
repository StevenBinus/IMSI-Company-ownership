import styled from '@emotion/styled'
import { AppBar, Button, Toolbar, ButtonProps, useTheme } from '@mui/material'
import ArrowCircleLeftIcon from '@mui/icons-material/ArrowCircleLeft'
import ArrowCircleRightIcon from '@mui/icons-material/ArrowCircleRight'
import DescriptionIcon from '@mui/icons-material/Description'
import SaveIcon from '@mui/icons-material/Save'
import LockOpenOutlinedIcon from '@mui/icons-material/LockOpenOutlined'
import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import ListAltIcon from '@mui/icons-material/ListAlt'

const ToolbarButton = styled(Button)<ButtonProps>(({ theme }) => ({
	textTransform: 'none',
}))

interface ToolbarMasterProps {
	handleBackButton?: () => void
	DisableBackButton?: boolean
	handleNextButton?: () => void
	DisableNextButton?: boolean
	handleSaveButton?: () => void
	DisableSaveButton?: boolean
	handleNewButton?: () => void
	DisableNewButton?: boolean
	handleActiveButton?: () => void
	DisableActiveButton?: boolean
	handleDeactiveButton?: () => void
	DisableDeactiveButton?: boolean
	handleListButton?: () => void
	DisableListButton?: boolean
}

const ToolbarMaster = ({
	handleBackButton,
	DisableBackButton = false,
	handleNextButton,
	DisableNextButton = false,
	handleSaveButton,
	DisableSaveButton = false,
	handleNewButton,
	DisableNewButton = false,
	handleActiveButton,
	DisableActiveButton = false,
	handleDeactiveButton,
	DisableDeactiveButton = false,
	handleListButton,
	DisableListButton = false,
}: ToolbarMasterProps) => {
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
					id='back_toolbar_button'
					disabled={DisableBackButton}
					onClick={handleBackButton}
					color='inherit'
				>
					<ArrowCircleLeftIcon /> Back
				</ToolbarButton>
				<ToolbarButton
					id='next_toolbar_button'
					disabled={DisableNextButton}
					onClick={handleNextButton}
					color='inherit'
				>
					<ArrowCircleRightIcon /> Next
				</ToolbarButton>
				<ToolbarButton
					id='new_toolbar_button'
					disabled={DisableNewButton}
					onClick={handleNewButton}
					color='inherit'
				>
					<DescriptionIcon /> New
				</ToolbarButton>
				<ToolbarButton
					id='save_toolbar_button'
					disabled={DisableSaveButton}
					onClick={handleSaveButton}
					color='inherit'
				>
					<SaveIcon /> Save
				</ToolbarButton>
				<ToolbarButton
					id='activate_toolbar_button'
					disabled={DisableActiveButton}
					onClick={handleActiveButton}
					color='inherit'
				>
					<LockOpenOutlinedIcon /> Activate
				</ToolbarButton>
				<ToolbarButton
					id='deactivate_toolbar_button'
					disabled={DisableDeactiveButton}
					onClick={handleDeactiveButton}
					color='inherit'
				>
					<LockOutlinedIcon /> Deactivate
				</ToolbarButton>
				<ToolbarButton
					id='list_toolbar_button'
					disabled={DisableListButton}
					onClick={handleListButton}
					color='inherit'
				>
					<ListAltIcon /> List
				</ToolbarButton>
			</Toolbar>
		</AppBar>
	)
}

export default ToolbarMaster
