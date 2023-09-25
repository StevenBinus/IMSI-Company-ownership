import { Grid, IconButton, Popover, Typography } from '@mui/material'
import { useRef, useState } from 'react'
import InfoIcon from '@mui/icons-material/Info'

interface UnitAllocationInfoType {
	spm_number: string
	vehicle_desc: string
	engine_no: string
	customer_purchase_order: string
}

export const UnitAllocationInfo = (props: UnitAllocationInfoType) => {
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
					<Typography>{props.vehicle_desc}</Typography>
					<Typography>{props.engine_no}</Typography>
					<Typography>{props.customer_purchase_order}</Typography>
				</Grid>
			</Popover>
		</IconButton>
	)
}
