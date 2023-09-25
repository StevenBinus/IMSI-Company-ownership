import TextFieldDMS from '@components/TextFieldDMS.component'
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
import TextFieldLookUpDMS from '@components/TextFieldLookUpDMS.component'
import DatePickerDMS from '@components/DatePickerDMS.component'
import DropDownListDMS from '@components/DropDownListDMS.component'
import DataGridDMS from '@components/DataGridDMS.component'
import { GridColDef } from '@mui/x-data-grid'
import NoteAddIcon from '@mui/icons-material/NoteAdd'
import HighlightOffIcon from '@mui/icons-material/HighlightOff'

const dataGridColumns: GridColDef[] = [
	{
		field: 'colour',
		headerName: 'Colour',
		flex: 1,
	},
	{
		field: 'qty',
		headerName: 'Quantity',
		flex: 1,
	},
	{
		field: 'expected_delivery',
		headerName: 'Expected Delivery',
		flex: 1,
	},
]

type Props = {}

const ProspectDetailVehicle = (props: Props) => {
	const theme = useTheme()
	const [isActive, setIsActive] = useState(false)
	const [isTestDrive, setIsTestDrive] = useState(false)
	return (
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
					label='Vehicle Detail'
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
					<DropDownListDMS
						id='brand'
						label={<span>Brand</span>}
						optionData={[]}
						valueData={undefined}
						onChangeValueData={function (value: any): void {
							throw new Error('Function not implemented.')
						}}
						getOptionLabel={function (option: any): string {
							throw new Error('Function not implemented.')
						}}
						isOptionEqualToValue={function (option: any, value: any): boolean {
							throw new Error('Function not implemented.')
						}}
					/>
					<DropDownListDMS
						id='model'
						disabled
						label={<span>Model</span>}
						optionData={[]}
						valueData={undefined}
						onChangeValueData={function (value: any): void {
							throw new Error('Function not implemented.')
						}}
						getOptionLabel={function (option: any): string {
							throw new Error('Function not implemented.')
						}}
						isOptionEqualToValue={function (option: any, value: any): boolean {
							throw new Error('Function not implemented.')
						}}
					/>
					<DropDownListDMS
						id='variant'
						disabled
						label={<span>Variant</span>}
						optionData={[]}
						valueData={undefined}
						onChangeValueData={function (value: any): void {
							throw new Error('Function not implemented.')
						}}
						getOptionLabel={function (option: any): string {
							throw new Error('Function not implemented.')
						}}
						isOptionEqualToValue={function (option: any, value: any): boolean {
							throw new Error('Function not implemented.')
						}}
					/>
					<TextFieldLookUpDMS
						id='option_code'
						label={<span>Option Code</span>}
						dataColumn={[]}
						dataRow={[]}
						handleDataRowId={() => {
							return 1
						}}
						handleOnDoubleClick={() => {}}
						handleOnBlur={() => {}}
						listModal={false}
						handleCloseListModal={function (): void {
							throw new Error('Function not implemented.')
						}}
						handleOpenListModal={function (): void {
							throw new Error('Function not implemented.')
						}}
					/>
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
					<Box sx={{ paddingBottom: '10px', paddingTop: '20px' }}>
						<FormControlLabel
							checked={isTestDrive}
							label='Test Drive'
							labelPlacement='start'
							onChange={() => setIsTestDrive((prev) => !prev)}
							control={<Checkbox />}
							sx={{ margin: 0 }}
						/>
						<Box sx={{ paddingLeft: '30px' }}>
							<DatePickerDMS
								disabled={!isTestDrive}
								id='test_drive_schedule'
								label={<span>Test Drive Schedule</span>}
								date={null}
							/>
							<DatePickerDMS
								disabled={!isTestDrive}
								id='test_drive_actual'
								label={<span>Test Drive Actual</span>}
								date={null}
							/>
						</Box>
					</Box>
					<TextFieldDMS
						id='competitor_product'
						label={<span>Competitor Product</span>}
					/>
				</Collapse>
			</Grid>
		</Grid>
	)
}

export default ProspectDetailVehicle
