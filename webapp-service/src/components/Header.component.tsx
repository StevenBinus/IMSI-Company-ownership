import { styled } from '@mui/material/styles'
import MuiAppBar from '@mui/material/AppBar'
import {
	Toolbar,
	Typography,
	IconButton,
	Box,
	Grid,
	AppBarProps as MuiAppBarProps,
} from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu'
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft'
import SideMenu from './SideMenu.component'
import { DRAWER_WIDTH } from './Layout.component'
import Link from 'next/link'
import CompanySelectHeader from './CompanySelectHeader.component'
import { useRouter } from 'next/router'
import useUserStore from '@utils/store.util'
import { eraseCookie } from '@utils/cookies.util'

interface AppBarProps extends MuiAppBarProps {
	open?: boolean
}

const AppBar = styled(MuiAppBar, {
	shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
	backgroundColor: theme.palette.background.paper,
	color: theme.palette.primary.main,
	boxShadow: 'none',
	borderBottom: `1px solid ${theme.palette.divider}`,
	zIndex: 1200 + 30,
	transition: theme.transitions.create(['margin', 'width'], {
		easing: theme.transitions.easing.sharp,
		duration: theme.transitions.duration.leavingScreen,
	}),
	...(open && {
		width: `calc(100% - ${DRAWER_WIDTH}px)`,
		marginLeft: `${DRAWER_WIDTH}px`,
		transition: theme.transitions.create(['margin', 'width'], {
			easing: theme.transitions.easing.easeOut,
			duration: theme.transitions.duration.enteringScreen,
		}),
	}),
}))

const HeaderLink = styled(Link)(({ theme }) => ({
	color: theme.palette.primary.main,
	textDecoration: 'none',
}))

interface HeaderProps {
	currentMenu?: string
	open: boolean
	handleDrawerOpen: () => void
	handleDrawerClose: () => void
}

const Header = (props: HeaderProps) => {
	const router = useRouter()

	return (
		<>
			<AppBar position='fixed' open={props.open}>
				<Toolbar
					sx={{
						minWidth: props.open ? '620px' : '660px',
						justifyContent: 'flex-end',
					}}
				>
					<IconButton
						color='inherit'
						aria-label='open drawer'
						onClick={
							props.open ? props.handleDrawerClose : props.handleDrawerOpen
						}
						edge='start'
						sx={{ mr: 2 }}
					>
						{props.open ? <ChevronLeftIcon /> : <MenuIcon />}
					</IconButton>
					<Box
						sx={{
							height: '64px',
							width: 'auto',
							cursor: 'pointer',
						}}
						component='img'
						src='/IMS-LOGO.png'
						onClick={() => {
							router.push('/dashboard')
						}}
						alt='Feature Image'
					/>
					<Box sx={{ minWidth: '400px', flexGrow: 1 }}>
						<Grid container direction='column' item>
							<Grid container direction='row' justifyContent='flex-end' item>
								<Grid item>
									<Typography fontWeight={'bold'}>
										Welcome, Designated User
									</Typography>
								</Grid>
							</Grid>
							<Grid
								container
								item
								direction='row'
								alignItems='center'
								justifyContent='flex-end'
							>
								<Grid container item xs='auto'>
									&nbsp;
									<Typography variant='h6' noWrap component='div'>
										{props.currentMenu ? `${props.currentMenu} Menu` : ''}
									</Typography>
									&nbsp;
								</Grid>
								<Grid container item xs='auto'>
									<CompanySelectHeader />
								</Grid>
							</Grid>
						</Grid>
					</Box>
				</Toolbar>
			</AppBar>
			<SideMenu open={props.open} handleDrawerClose={props.handleDrawerClose} />
		</>
	)
}

export default Header
