import {
	MenuRequestProps,
	menu_list_data_dummy,
} from '@components/api/getMenu.api'
import PageLoad from '@components/PageLoad.component'
import {
	Box,
	Button,
	Grid,
	TextField,
	Typography,
	useTheme,
} from '@mui/material'
import { eraseCookie, setCookie } from '@utils/cookies.util'
import useUserStore from '@utils/store.util'
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'
import { postLogin } from './api/postLogin.api'

const ResetPasswordPage = () => {
	const router = useRouter()
	const theme = useTheme()

	const store = useUserStore((state) => state)
	const [isLoading, setIsLoading] = useState(false)

	const handleLogin = async () => {
		setIsLoading(true)
		const loginData = await postLogin({
			username: '50641',
			password: 'Img50641',
		})
		setIsLoading(false)
		if (!loginData) {
			alert('Incorrect Login')
		}
		store.updateUserMenu(menu_list_data_dummy)
		store.updateUserCompany(1)
		store.updateUserModule('Dashboard')
		setCookie('token', loginData.token, 1)
		router.push('/dashboard')
	}

	useEffect(() => {
		eraseCookie('token')
		useUserStore.persist.clearStorage()
	}, [])

	return (
		<Grid
			container
			justifyContent='center'
			alignItems='center'
			direction='column'
			sx={{
				height: '100vh',
				backgroundImage: `url(/Loginbg.jpg)`,
				backgroundSize: 'cover',
			}}
		>
			<PageLoad loading={isLoading} />
			<Box
				sx={{
					backgroundColor: `rgba(0,0,0,0.5)`,
					height: '200px',
					width: '400px',
					maxWidth: '90vw',
					textAlign: 'center',
					color: theme.palette.primary.contrastText,
					borderRadius: '5px',
				}}
			>
				<Typography variant='h5' sx={{ margin: '2%', width: '90%' }}>
					Login Dealer Management System
				</Typography>
				<TextField
					variant='filled'
					label='User Id'
					id='user_id'
					size='small'
					sx={{
						margin: '2%',
						width: '80%',
						backgroundColor: theme.palette.background.paper,
						borderRadius: '5px',
					}}
				/>
				<TextField
					variant='filled'
					label='Password'
					id='password'
					type='password'
					size='small'
					sx={{
						margin: '2%',
						width: '80%',
						backgroundColor: theme.palette.background.paper,
						borderRadius: '5px',
					}}
				/>
				<Button
					id='login_button'
					variant='contained'
					sx={{ margin: '5%', width: '30%' }}
					onClick={handleLogin}
				>
					Login
				</Button>
			</Box>
		</Grid>
	)
}

ResetPasswordPage.PageLayout = <></>

export default ResetPasswordPage
