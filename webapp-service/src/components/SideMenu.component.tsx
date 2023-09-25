'use client'
import {
	Autocomplete,
	Box,
	Collapse,
	Divider,
	Drawer,
	Grid,
	IconButton,
	List,
	ListItem,
	ListItemButton,
	TextField,
	Typography,
	styled,
	useTheme,
} from '@mui/material'
import FolderOpenIcon from '@mui/icons-material/FolderOpen'
import NoteAltOutlinedIcon from '@mui/icons-material/NoteAltOutlined'
import DirectionsCarOutlinedIcon from '@mui/icons-material/DirectionsCarOutlined'
import ConstructionOutlinedIcon from '@mui/icons-material/ConstructionOutlined'
import AddIcon from '@mui/icons-material/Add'
import RemoveIcon from '@mui/icons-material/Remove'
import PaidIcon from '@mui/icons-material/Paid'
import WebIcon from '@mui/icons-material/Web'
import { useRouter } from 'next/router'
import { useState } from 'react'
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft'
import useUserStore from '@utils/store.util'
import { MenuRequestProps } from './api/getMenu.api'
import { recursivelyFindKeyValueList } from '@utils/search.util'
import { DRAWER_WIDTH } from './Layout.component'
import { eraseCookie } from '@utils/cookies.util'
import LogoutIcon from '@mui/icons-material/Logout'
import SearchIcon from '@mui/icons-material/Search'

const DrawerHeader = styled('div')(({ theme }) => ({
	display: 'flex',
	alignItems: 'center',
	border: 0,
	padding: theme.spacing(0, 1),
	// necessary for content to be below app bar
	...theme.mixins.toolbar,
	justifyContent: 'flex-end',
}))

interface MenuNodeProps {
	node: MenuRequestProps
	handleNodeRoute: (url: any) => void
	handleNodeClick: (id: any) => void
	nodeOpen: any
	pathname: string
}

function MenuNode({
	node,
	handleNodeRoute,
	handleNodeClick,
	nodeOpen,
	pathname,
}: MenuNodeProps) {
	const theme = useTheme()
	if (!node) {
		return <span />
	}
	const nodeKey = node.title.toLowerCase().trim().replace(/\s+/g, '-')
	if (!node.children) {
		const isPathname = pathname.includes(node.url)
		return (
			<ListItem
				component='div'
				key={nodeKey}
				sx={{
					p: 0,
					pl: isPathname ? 0 : 1,
					// backgroundColor: isPathname ? theme.palette.primary.main : '',
					color: isPathname ? theme.palette.primary.contrastText : '',
					border: isPathname
						? `solid 1px ${theme.palette.primary.contrastText}`
						: '',
					borderRadius: ' 5px',
				}}
			>
				{isPathname ? (
					<Box
						sx={{
							minHeight: '35px',
							height: '100%',
							width: '5px',
							borderRadius: '3px 0 0 3px',
							backgroundColor: theme.palette.primary.contrastText,
						}}
					/>
				) : (
					<span />
				)}
				<ListItemButton
					role='button'
					aria-label={`menu-button-${nodeKey}`}
					onClick={() => handleNodeRoute(node.url)}
				>
					<WebIcon sx={{ marginRight: '5px' }} />
					<Typography>{node.title}</Typography>
				</ListItemButton>
			</ListItem>
		)
	}

	let icon = <FolderOpenIcon sx={{ marginRight: '5px' }} />
	switch (nodeKey) {
		case 'finance':
			icon = <PaidIcon sx={{ marginRight: '5px' }} />
			break
		case 'general':
			icon = <NoteAltOutlinedIcon sx={{ marginRight: '5px' }} />
			break
		case 'after-sales':
			icon = <ConstructionOutlinedIcon sx={{ marginRight: '5px' }} />
			break
		case 'unit':
			icon = <DirectionsCarOutlinedIcon sx={{ marginRight: '5px' }} />
			break
		default:
			icon = <FolderOpenIcon sx={{ marginRight: '5px' }} />
			break
	}
	return (
		<>
			<ListItem component='div' key={nodeKey} sx={{ p: 0 }}>
				<ListItemButton
					role='button'
					aria-label={`menu-button-${nodeKey}`}
					onClick={() => handleNodeClick(nodeKey)}
				>
					{nodeOpen[nodeKey] ? (
						<AddIcon sx={{ fontSize: '.8em' }} />
					) : (
						<RemoveIcon sx={{ fontSize: '.8em' }} />
					)}
					{icon}
					<Typography sx={{ fontSize: '.8em' }}>{node.title}</Typography>
				</ListItemButton>
			</ListItem>
			<Collapse in={!nodeOpen[nodeKey]}>
				<List component='div' sx={{ p: 0, pl: 2 }}>
					{node.children.map((c, index) => (
						<MenuNode
							node={c}
							key={index}
							handleNodeRoute={handleNodeRoute}
							handleNodeClick={handleNodeClick}
							nodeOpen={nodeOpen}
							pathname={pathname}
						/>
					))}
				</List>
			</Collapse>
		</>
	)
}

interface SideMenuProps {
	// modul: string
	open: boolean
	handleDrawerClose: () => void
}

const SideMenu = (props: SideMenuProps) => {
	const store = useUserStore((state) => state)
	const pathname = window.location.pathname
	const router = useRouter()
	const theme = useTheme()
	const menuData = recursivelyFindKeyValueList(
		'title',
		'',
		store.userStore.menu
	)
	const [value, setValue] = useState<{ label: string; id: string } | null>(null)
	const [inputValue, setInputValue] = useState('')

	const [open, setOpen] = useState({})
	function handleClick(id) {
		setOpen((prevState) => ({ ...prevState, [id]: !prevState[id] }))
	}

	function handleRoute(url) {
		setInputValue('')
		setValue(null)
		router.push(url)
	}

	const handleChangeModul = (data: string) => {
		if (data === 'Dashboard' && !pathname.includes('dashboard')) {
			setInputValue('')
			setValue(null)
			router.push('/dashboard')
		}
		if (data === 'Change Password' && !pathname.includes('change-password')) {
			setInputValue('')
			setValue(null)
			router.push('/change-password')
		}

		store.updateUserModule(data)
	}

	const isCurrentModule = (data: string) => {
		const isModuleData = data === store.userStore.module

		return isModuleData
	}

	const currentModulIndex = store.userStore.menu.findIndex(
		(item) =>
			item.title.toLowerCase().replace(/\s+/g, '') ===
			store.userStore.module.toLowerCase().replace(/\s+/g, '')
	)

	function getModulIndex(menu: string) {
		return store.userStore.menu.findIndex(
			(item) =>
				item.title.toLowerCase().replace(/\s+/g, '') ===
				menu.toLowerCase().replace(/\s+/g, '')
		)
	}

	const handleChangeAutoComplete = (
		newValue: { label: string; id: string } | null
	) => {
		if (newValue !== null) {
			setValue(newValue)
			if (newValue.id.includes('master')) {
				handleChangeModul('Master')
			}
			if (newValue.id.includes('transaction')) {
				handleChangeModul('Transaction')
			}
			if (newValue.id.includes('report')) {
				handleChangeModul('Report')
			}
			router.push(newValue.id)
		}
	}

	return (
		<>
			{store.userStore.menu === null ? (
				<span />
			) : (
				<Drawer
					sx={{
						width: DRAWER_WIDTH,
						flexShrink: 0,
						'& .MuiDrawer-paper': {
							border: 0,
							width: DRAWER_WIDTH,
							backgroundColor: theme.palette.primary.dark,
							color: theme.palette.primary.contrastText,
						},
						zIndex: 1200 + 20,
						display: 'flex',
					}}
					variant='persistent'
					anchor='left'
					open={props.open}
				>
					<DrawerHeader>
						<Box
							sx={{
								p: '2.6% 3%',
								width: '94%',
							}}
						>
							<Autocomplete
								sx={{
									'&.Mui-focused .MuiInputLabel-outlined': {
										color: theme.palette.primary.contrastText,
									},
									'& .MuiButtonBase-root': {
										color: theme.palette.primary.contrastText,
									},
									'& .MuiAutocomplete-inputRoot': {
										color: theme.palette.primary.contrastText,
										'& .MuiOutlinedInput-notchedOutline': {
											borderColor: theme.palette.primary.contrastText,
										},
										'&:hover .MuiOutlinedInput-notchedOutline': {
											borderColor: theme.palette.primary.contrastText,
										},
										'&.Mui-focused .MuiOutlinedInput-notchedOutline': {
											borderColor: theme.palette.primary.contrastText,
										},
									},
								}}
								selectOnFocus
								disablePortal
								id='combo-box-demo'
								value={value}
								onChange={(
									event: any,
									newValue: { label: string; id: string } | null
								) => {
									handleChangeAutoComplete(newValue)
								}}
								inputValue={inputValue}
								onInputChange={(event, newInputValue) => {
									setInputValue(newInputValue)
								}}
								isOptionEqualToValue={(option, value) => option.id === value.id}
								options={menuData}
								fullWidth
								freeSolo
								renderInput={(params) => (
									<TextField
										{...params}
										size='small'
										placeholder='Menu Search'
									/>
								)}
							/>
						</Box>
					</DrawerHeader>

					<Divider />
					<List component='div' sx={{ overflowY: 'auto', p: '5px' }}>
						<MenuNode
							node={store.userStore.menu[currentModulIndex]}
							handleNodeRoute={handleRoute}
							handleNodeClick={handleClick}
							nodeOpen={open}
							pathname={pathname}
						/>
					</List>
					<Divider />
					<List component='div' sx={{ p: 1 }}>
						{['Dashboard', 'Master', 'Transaction', 'Report'].map(
							(data, index) => (
								<ListItem
									component='div'
									sx={{
										padding: 0,
										color: isCurrentModule(data)
											? theme.palette.primary.contrastText
											: '',
										border: isCurrentModule(data)
											? `solid 1px ${theme.palette.primary.contrastText}`
											: '',
										borderRadius: ' 5px',
									}}
									key={index}
								>
									{isCurrentModule(data) ? (
										<Box
											sx={{
												minHeight: '35px',
												height: '100%',
												width: '5px',
												borderRadius: '3px 0 0 3px',
												backgroundColor: theme.palette.primary.contrastText,
											}}
										/>
									) : (
										<span />
									)}
									<ListItemButton
										role='button'
										aria-label={`menu-button-${data
											.toLowerCase()
											.trim()
											.replace(/\s+/g, '-')}`}
										onClick={() => handleChangeModul(data)}
									>
										<Typography>{data}</Typography>
									</ListItemButton>
								</ListItem>
							)
						)}
					</List>
					<Divider />
					<List component='div' sx={{ p: 1 }}>
						<ListItem
							component='div'
							sx={{
								padding: 0,
								color: isCurrentModule('Change Password')
									? theme.palette.primary.contrastText
									: '',
								border: isCurrentModule('Change Password')
									? `solid 1px ${theme.palette.primary.contrastText}`
									: '',
								borderRadius: ' 5px',
							}}
						>
							{isCurrentModule('Change Password') ? (
								<Box
									sx={{
										height: '35px',
										width: '5px',
										borderRadius: '5px 0 0 5px',
										backgroundColor: theme.palette.primary.contrastText,
									}}
								/>
							) : (
								<span />
							)}
							<ListItemButton
								role='button'
								aria-label={`menu-button-${'Change Password'
									.toLowerCase()
									.trim()
									.replace(/\s+/g, '-')}`}
								onClick={() => handleChangeModul('Change Password')}
							>
								<Typography>{'Change Password'}</Typography>
							</ListItemButton>
						</ListItem>
						<ListItem
							component='div'
							sx={{
								padding: 0,
								borderRadius: ' 5px',
								color: theme.palette.secondary.light,
							}}
						>
							<ListItemButton
								role='button'
								aria-label={`menu-button-logout`}
								onClick={() => {
									useUserStore.persist.clearStorage()
									eraseCookie('token')
									router.push('/')
								}}
							>
								<Grid container direction='row'>
									<Grid container item xs={10}>
										<Typography>Logout</Typography>
									</Grid>
									<Grid container item xs={2} justifyContent='flex-end'>
										<LogoutIcon />
									</Grid>
								</Grid>
							</ListItemButton>
						</ListItem>
					</List>
				</Drawer>
			)}
		</>
	)
}

export default SideMenu
