import {
	Box,
	BoxProps,
	Button,
	Dialog,
	DialogActions,
	DialogContent,
	styled,
} from '@mui/material'
import {
	DataGrid,
	GridColDef,
	GridSortModel,
	GridToolbarContainer,
} from '@mui/x-data-grid'
import { Dispatch, useEffect, useState } from 'react'
import ListModalFooter, { FilterProps } from './ListModalFooter.component'

const ModalBox = styled(Box)<BoxProps>(({ theme }) => ({
	width: '100%',
	minWidth: '600px',
	height: '400px',
	backgroundColor: theme.palette.background.paper,
	boxShadow: '24px',
	padding: '4px',
}))

function CustomToolbar() {
	return <GridToolbarContainer></GridToolbarContainer>
}

interface ListModalProps {
	open: boolean
	handleClose: () => void
	dataColumn: GridColDef[]
	dataRow: any[]
	handleDataRowId: (row: any) => any
	handleOnDoubleClick: (row: any) => void
	isLoading?: boolean
	totalDataRow?: number
	page?: number
	setPage?: Dispatch<React.SetStateAction<number>>
	pageSize?: number
	setPageSize?: Dispatch<React.SetStateAction<number>>
	handleSortTable?: (data: GridSortModel) => void
	handleSearchButton?: (data: FilterProps[]) => void
}

const ListModal = (props: ListModalProps) => {
	const [isFullscreen, setIsFullscreen] = useState(false)

	const handleFullscreenButton = () => {
		setIsFullscreen((isFullscreen) => !isFullscreen)
	}

	const [rowCountState, setRowCountState] = useState(props.totalDataRow || 0)
	useEffect(() => {
		setRowCountState((prevRowCountState) =>
			props.totalDataRow !== undefined ? props.totalDataRow : prevRowCountState
		)
	}, [props.totalDataRow, setRowCountState])

	return (
		<Dialog
			maxWidth={false}
			open={props.open}
			onClose={props.handleClose}
			fullScreen={isFullscreen}
			aria-labelledby='list-modal-label'
			aria-describedby='list-modal-description'
			sx={{ zIndex: 1200 + 40 }}
		>
			<DialogActions sx={{ padding: '20px 20px 0 20px' }}>
				<Button onClick={handleFullscreenButton}>Fullscreen</Button>
				<Button onClick={props.handleClose}>Close</Button>
			</DialogActions>
			<DialogContent sx={{ padding: '0 20px 20px 20px' }}>
				<ModalBox>
					<DataGrid
						sx={{
							grid: {
								display: 'flex',
								flexDirection: 'row-reverse',
							},
						}}
						density='compact'
						disableColumnMenu
						rowCount={rowCountState}
						rows={props.dataRow}
						columns={props.dataColumn}
						getRowId={props.handleDataRowId}
						onRowDoubleClick={(data) => props.handleOnDoubleClick(data.row)}
						paginationMode='server'
						pagination
						loading={props.isLoading}
						sortingMode='server'
						onSortModelChange={(model, details) => props.handleSortTable(model)}
						components={{
							Footer: ListModalFooter,
							Toolbar: CustomToolbar,
						}}
						componentsProps={{
							footer: {
								dataColumn: props.dataColumn,
								handleSearchButton: props.handleSearchButton,
								totalDataRow: props.totalDataRow,
								page: props.page,
								setPage: props.setPage,
								pageSize: props.pageSize,
								setPageSize: props.setPageSize,
							},
						}}
					/>
				</ModalBox>
			</DialogContent>
		</Dialog>
	)
}

export default ListModal
