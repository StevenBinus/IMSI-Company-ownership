import {
	Button,
	Grid,
	StandardTextFieldProps,
	TextField,
	TextFieldProps,
	Typography,
	useTheme,
} from '@mui/material'
import { GridColDef, GridSortModel } from '@mui/x-data-grid'
import dynamic from 'next/dynamic'
import React, { Dispatch, useState } from 'react'
import { FilterProps } from './ListModalFooter.component'
const ListModal = dynamic(() => import('./ListModal.component'))

interface TextFieldLookUpDMSProps extends StandardTextFieldProps {
	handleOnBlur: () => void
	dataColumn: GridColDef[]
	dataRow: any[]
	handleDataRowId: (row: any) => number
	handleOnDoubleClick: (row: any) => void
	listModal: boolean
	handleCloseListModal: () => void
	handleOpenListModal: () => void
	descriptionValue?: string
	hideDescriptionValue?: boolean
	isLoading?: boolean
	totalDataRow?: number
	page?: number
	setPage?: Dispatch<React.SetStateAction<number>>
	pageSize?: number
	setPageSize?: Dispatch<React.SetStateAction<number>>
	handleSortTable?: (data: GridSortModel) => void
	handleSearchButton?: (data: FilterProps[]) => void
}

const TextFieldLookUpDMS = ({
	handleOnBlur,
	dataColumn,
	dataRow,
	handleDataRowId,
	handleOnDoubleClick,
	listModal,
	handleCloseListModal,
	handleOpenListModal,
	descriptionValue,
	hideDescriptionValue = false,
	isLoading,
	totalDataRow,
	page,
	setPage,
	pageSize,
	setPageSize,
	handleSortTable,
	handleSearchButton,
	...props
}: TextFieldLookUpDMSProps) => {
	const theme = useTheme()
	return (
		<>
			<ListModal
				open={listModal}
				handleClose={handleCloseListModal}
				dataColumn={dataColumn}
				dataRow={dataRow}
				handleDataRowId={handleDataRowId}
				handleOnDoubleClick={handleOnDoubleClick}
				isLoading={isLoading}
				totalDataRow={totalDataRow}
				page={page}
				setPage={setPage}
				pageSize={pageSize}
				setPageSize={setPageSize}
				handleSortTable={handleSortTable}
				handleSearchButton={handleSearchButton}
			/>
			<Grid container alignItems='center' sx={{ paddingBottom: '10px' }}>
				<Grid item xs={4}>
					<Typography
						sx={{ paddingBottom: props.error ? 'calc(8.5px + .75rem)' : '' }}
					>
						{props.label}
					</Typography>
				</Grid>
				<Grid item xs={3.5}>
					<TextField
						fullWidth
						{...props}
						onBlur={handleOnBlur}
						inputProps={{
							'aria-label': `textfield-dms-${props.id
								.toString()
								.toLowerCase()
								.trim()
								.replace(/_+/g, '-')}`,
						}}
						size='small'
						label=''
						sx={{
							'& .MuiInputBase-input.Mui-disabled': {
								WebkitTextFillColor: theme.palette.secondary.contrastText,
								backgroundColor: theme.palette.secondary.main,
							},
						}}
					/>
				</Grid>
				<Grid container justifyContent='center' item xs={1}>
					<Button
						sx={{
							minWidth: 0,
							marginBottom: props.error ? 'calc(8.5px + .75rem)' : '',
						}}
						variant='contained'
						onClick={handleOpenListModal}
					>
						...
					</Button>
				</Grid>
				<Grid item xs={3.5}>
					<TextField
						disabled
						fullWidth
						size='small'
						label=''
						value={descriptionValue}
						inputProps={{
							'aria-label': `textfield-dms-${props.id
								.toString()
								.toLowerCase()
								.trim()
								.replace(/_+/g, '-')}`,
						}}
						sx={{
							'& .MuiInputBase-input.Mui-disabled': {
								WebkitTextFillColor: theme.palette.secondary.contrastText,
								backgroundColor: theme.palette.secondary.main,
							},
							paddingBottom: props.error ? 'calc(8.5px + .75rem)' : '',
							display: hideDescriptionValue ? 'none' : 'inline',
						}}
					/>
				</Grid>
			</Grid>
		</>
	)
}

export default TextFieldLookUpDMS
