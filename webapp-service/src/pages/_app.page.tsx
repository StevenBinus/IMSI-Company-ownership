import type { AppProps } from 'next/app'
import { Router } from 'next/router'
import { useEffect, useState } from 'react'
import PageLoad from '@components/PageLoad.component'
import { createTheme, ThemeProvider } from '@mui/material'
import Layout from '@components/Layout.component'
import { Roboto } from '@next/font/google'

const roboto = Roboto({ subsets: ['latin'], weight: ['400', '700'] })

const theme = createTheme({
	palette: {
		mode: 'light',
		primary: {
			main: '#2280ca',
			light: '#59aaef',
			dark: '#1d629b',
		},
		secondary: {
			main: '#E7EFF7',
		},
		info: {
			main: '#FFFF99',
		},
		background: {
			default: '#ebecf4',
		},
	},
	typography: {
		fontFamily: roboto.style.fontFamily,
		fontSize: 10,
	},
})

type PageWithLayout = AppProps & {
	Component: AppProps['Component'] & {
		PageLayout?: React.ComponentType
	}
}

export default function App({ Component, pageProps }: PageWithLayout) {
	const [loading, setLoading] = useState(false)

	useEffect(() => {
		Router.events.on('routeChangeStart', () => setLoading(true))
		Router.events.on('routeChangeComplete', () => setLoading(false))
		Router.events.on('routeChangeError', () => setLoading(false))
		return () => {
			Router.events.off('routeChangeStart', () => setLoading(true))
			Router.events.off('routeChangeComplete', () => setLoading(false))
			Router.events.off('routeChangeError', () => setLoading(false))
		}
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, [Router.events])

	if (Component.PageLayout) {
		return (
			<ThemeProvider theme={theme}>
				<PageLoad loading={loading} />
				<Component {...pageProps} />
			</ThemeProvider>
		)
	}
	return (
		<ThemeProvider theme={theme}>
			<Layout>
				<PageLoad loading={loading} />
				<Component {...pageProps} />
			</Layout>
		</ThemeProvider>
	)
}
