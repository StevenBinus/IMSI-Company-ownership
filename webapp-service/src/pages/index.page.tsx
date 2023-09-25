import { useRouter } from 'next/router'
import { useEffect } from 'react'

const HomePage = () => {
	const router = useRouter()

	useEffect(() => {
		router.replace('/auth/login')
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, [])

	return <></>
}

HomePage.PageLayout = <></>

export default HomePage
