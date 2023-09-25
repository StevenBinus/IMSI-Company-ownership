import {
	Box,
	Button,
	Checkbox,
	Collapse,
	FormControlLabel,
	Grid,
	useTheme,
} from '@mui/material'
import React, { useState } from 'react'
import AddBoxOutlinedIcon from '@mui/icons-material/AddBoxOutlined'
import IndeterminateCheckBoxOutlinedIcon from '@mui/icons-material/IndeterminateCheckBoxOutlined'
import DataGridDMS from '@components/DataGridDMS.component'
import { GridColDef } from '@mui/x-data-grid'
import NoteAddIcon from '@mui/icons-material/NoteAdd'
import HighlightOffIcon from '@mui/icons-material/HighlightOff'
import FollowUpModal from './ProspectDetailFollowUpModal.component'

const dataGridColumns: GridColDef[] = [
	{
		field: 'follow_up_date',
		headerName: 'Follow Up Date',
		flex: 1,
	},
	{
		field: 'follow_up_desc',
		headerName: 'Follow Up Desc',
		flex: 1,
	},
	{
		field: 'follow_up_note',
		headerName: 'Follow Up Note',
		flex: 1,
	},
	{
		field: 'result_date',
		headerName: 'Result Date',
		flex: 1,
	},
	{
		field: 'result_note',
		headerName: 'Result Note',
		flex: 1,
	},
]

type Props = {}

const ProspectDetailFollowUp = (props: Props) => {
	const theme = useTheme()
	const [isActive, setIsActive] = useState(false)
	const [isTestDrive, setIsTestDrive] = useState(false)
	const [followUpModal, setFollowUpModal] = useState(false)
	return (
		<>
			<FollowUpModal
				open={followUpModal}
				handleClose={() => setFollowUpModal(false)}
			/>
			<Grid
				container
				direction='column'
				sx={{
					padding: '2% 0',
					borderRadius: '5px',
				}}
			>
				<Grid container item>
					<FormControlLabel
						checked={isActive}
						label='Follow Up'
						onChange={() => setIsActive((prev) => !prev)}
						control={
							<Checkbox
								icon={<AddBoxOutlinedIcon />}
								checkedIcon={<IndeterminateCheckBoxOutlinedIcon />}
							/>
						}
					/>
				</Grid>
				<Grid container item>
					<Collapse
						in={isActive}
						unmountOnExit
						sx={{
							padding: '2%',
							width: '100%',
						}}
					>
						<Box
							sx={{
								height: '300px',
							}}
						>
							<DataGridDMS
								pageSize={5}
								getRowId={(row: { value: string; label: string }) => {
									return row.value
								}}
								checkboxSelection
								onRowDoubleClick={(data) => {}}
								columns={dataGridColumns}
								rows={[]}
							/>
						</Box>
						<Button
							sx={{ margin: '10px 10px 0 0' }}
							startIcon={<NoteAddIcon />}
							variant='contained'
							onClick={() => setFollowUpModal(true)}
						>
							Add
						</Button>
						<Button
							sx={{ margin: '10px 10px 0 0' }}
							startIcon={<HighlightOffIcon />}
							variant='contained'
						>
							Delete
						</Button>
					</Collapse>
				</Grid>
			</Grid>
		</>
	)
}

export default ProspectDetailFollowUp
