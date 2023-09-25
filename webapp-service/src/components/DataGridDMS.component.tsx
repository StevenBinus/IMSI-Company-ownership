import { alpha, styled } from '@mui/material'
import {
	DataGrid,
	DataGridProps,
	GridColumnMenuContainer,
	GridToolbarContainer,
	gridClasses,
} from '@mui/x-data-grid'
import React from 'react'

const ODD_OPACITY = 0.2

const StripedDataGrid = styled(DataGrid)(({ theme }) => ({
	[`& .${gridClasses.row}.even`]: {
		backgroundColor: theme.palette.grey[200],
		'&:hover, &.Mui-hovered': {
			backgroundColor: alpha(theme.palette.primary.main, ODD_OPACITY),
			'@media (hover: none)': {
				backgroundColor: 'transparent',
			},
		},
		'&.Mui-selected': {
			backgroundColor: alpha(
				theme.palette.primary.main,
				ODD_OPACITY + theme.palette.action.selectedOpacity
			),
			'&:hover, &.Mui-hovered': {
				backgroundColor: alpha(
					theme.palette.primary.main,
					ODD_OPACITY +
						theme.palette.action.selectedOpacity +
						theme.palette.action.hoverOpacity
				),
				// Reset on touch devices, it doesn't add specificity
				'@media (hover: none)': {
					backgroundColor: alpha(
						theme.palette.primary.main,
						ODD_OPACITY + theme.palette.action.selectedOpacity
					),
				},
			},
		},
	},
}))

function EmptyToolbar() {
	return <GridToolbarContainer></GridToolbarContainer>
}

function EmptyColumnMenu() {
	return (
		<GridColumnMenuContainer
			hideMenu={function (event: React.SyntheticEvent<Element, Event>): void {
				throw new Error('Function not implemented.')
			}}
			currentColumn={undefined}
			open={false}
		></GridColumnMenuContainer>
	)
}

const DataGridDMS = (props: DataGridProps) => {
	return (
		<StripedDataGrid
			{...props}
			sx={{
				grid: {
					display: 'flex',
					flexDirection: 'row-reverse',
				},
			}}
			getRowClassName={(params) =>
				params.indexRelativeToCurrentPage % 2 === 0 ? 'even' : 'odd'
			}
			density='compact'
			disableColumnMenu
			paginationMode='server'
			rowsPerPageOptions={[10, 25, 50]}
			pagination
			components={{
				Toolbar: EmptyToolbar,
				ColumnMenu: EmptyColumnMenu,
			}}
		/>
	)
}

export default DataGridDMS
