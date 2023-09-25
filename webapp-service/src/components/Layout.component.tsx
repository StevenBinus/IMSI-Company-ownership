import { useState } from 'react'
import Head from 'next/head'
import { Box, styled, useTheme } from '@mui/material'
import Header from './Header.component'
import NoSSRWrapper from './NoSSRWrapper.component'
import useUserStore from '@utils/store.util'
import { recursivelyFindKeyValue } from '@utils/search.util'

export const DRAWER_WIDTH = 410

const DrawerHeader = styled('div')(({ theme }) => ({
	display: 'flex',
	alignItems: 'center',
	padding: theme.spacing(0, 1),
	// necessary for content to be below app bar
	...theme.mixins.toolbar,
	justifyContent: 'flex-end',
}))

const Main = styled('main', { shouldForwardProp: (prop) => prop !== 'open' })<{
	open?: boolean
}>(({ theme, open }) => ({
	flexGrow: 1,
	padding: 0,
	transition: theme.transitions.create('margin', {
		easing: theme.transitions.easing.sharp,
		duration: theme.transitions.duration.leavingScreen,
	}),
	marginLeft: `-${DRAWER_WIDTH}px`,
	...(open && {
		transition: theme.transitions.create('margin', {
			easing: theme.transitions.easing.easeOut,
			duration: theme.transitions.duration.enteringScreen,
		}),
		marginLeft: 0,
	}),
}))

const Layout = ({ children }: any) => {
	const theme = useTheme()
	const [open, setOpen] = useState(true)

	const store = useUserStore((state) => state)

	const handleDrawerOpen = () => {
		setOpen(true)
	}

	const handleDrawerClose = () => {
		setOpen(false)
	}

	const getCurrentMenu = () => {
		if (typeof window !== 'undefined') {
			// Client-side-only code

			const menu = recursivelyFindKeyValue(
				'url',
				window.location.pathname,
				store.userStore.menu
			)
			return menu.value.title
		}
		return undefined
	}

	return (
		<>
			<Head>
				<title>IMS</title>
				<meta name='description' content='DMS Indomobil' />
				<meta name='viewport' content='width=device-width, initial-scale=1' />
				<link rel='icon' href='/favicon.ico' />
			</Head>
			<NoSSRWrapper>
				<Box
					sx={{
						display: 'flex',
						'& #menu-': {
							zIndex: '2300',
						},
					}}
				>
					<Header
						currentMenu={getCurrentMenu()}
						open={open}
						handleDrawerOpen={handleDrawerOpen}
						handleDrawerClose={handleDrawerClose}
					/>
					<Main
						open={open}
						key={store.userStore.seed}
						sx={{
							backgroundColor: theme.palette.background.default,
						}}
					>
						<DrawerHeader />
						<section>{children}</section>
					</Main>
				</Box>
			</NoSSRWrapper>
		</>
	)
}

export default Layout
