import { Backdrop, CircularProgress } from '@mui/material'

interface PageLoadProps {
	loading: boolean
}

const PageLoad = (props: PageLoadProps) => {
	return (
		<>
			{props.loading ? (
				<Backdrop sx={{ zIndex: 3000 + 10 }} open={true}>
					<CircularProgress color='secondary' />
				</Backdrop>
			) : (
				<></>
			)}
		</>
	)
}

export default PageLoad
