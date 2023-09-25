import { Skeleton } from '@mui/material'

const SkeletonLoad = () => {
	return (
		<>
			<Skeleton
				variant='rounded'
				width={'100%'}
				height={60}
				sx={{ marginBottom: '15px' }}
			/>
			<Skeleton
				variant='rounded'
				width={'50%'}
				height={40}
				sx={{ marginBottom: '15px' }}
			/>
			<Skeleton
				variant='rounded'
				width={'50%'}
				height={40}
				sx={{ marginBottom: '15px' }}
			/>
			<Skeleton
				variant='rounded'
				width={'50%'}
				height={40}
				sx={{ marginBottom: '15px' }}
			/>
		</>
	)
}

export default SkeletonLoad
