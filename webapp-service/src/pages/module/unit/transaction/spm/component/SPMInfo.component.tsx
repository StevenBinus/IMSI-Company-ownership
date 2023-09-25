import { Grid, IconButton, Popover, Typography } from '@mui/material'
import { useRef, useState } from 'react'
import InfoIcon from '@mui/icons-material/Info'

interface SPMInfoType {
	spm_number: string
	approval_by: string
	approval_remark: string
}

export const SPMInfo = (props: SPMInfoType) => {
	const [openedPopover, setOpenedPopover] = useState(false)
	const popoverAnchor = useRef(null)

	const popoverEnter = () => {
		setOpenedPopover(true)
	}

	const popoverLeave = () => {
		setOpenedPopover(false)
	}

	return (
		<IconButton
			ref={popoverAnchor}
			onMouseEnter={popoverEnter}
			onMouseLeave={popoverLeave}
		>
			<InfoIcon />
			<Popover
				id={`icon-info-${props.spm_number}`}
				anchorEl={popoverAnchor.current}
				open={openedPopover}
				anchorOrigin={{
					vertical: 'center',
					horizontal: 'right',
				}}
				sx={{
					pointerEvents: 'none',
				}}
			>
				<Grid container direction='column' sx={{ padding: '10px' }}>
					<Typography>{props.approval_by}</Typography>
					<Typography>{props.approval_remark}</Typography>
				</Grid>
			</Popover>
		</IconButton>
	)
}
