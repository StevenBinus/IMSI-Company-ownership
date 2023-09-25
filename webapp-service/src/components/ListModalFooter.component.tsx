import { Button, Grid, InputBase, TablePagination } from '@mui/material'
import { GridColDef } from '@mui/x-data-grid'
import React, { Dispatch, useState } from 'react'

export interface FilterProps {
	field: string
	filter: string
	flex: number
}

interface ListModalFooterProps {
	dataColumn: GridColDef[]
	handleSearchButton: (data: FilterProps[]) => void
	totalDataRow?: number
	page?: number
	setPage?: Dispatch<React.SetStateAction<number>>
	pageSize?: number
	setPageSize?: Dispatch<React.SetStateAction<number>>
}

const ListModalFooter = (props: ListModalFooterProps) => {
	const [filterState, setFilterState] = useState<FilterProps[]>(
		props.dataColumn.map((item) => ({
			field: item.field,
			filter: '',
			flex: item.flex,
		}))
	)
	console.log(filterState)
	return (
		<Grid container sx={{ width: '100%' }}>
			{filterState.map((item, key) => (
				<Grid container item key={key} flex={item.flex}>
					<InputBase
						sx={{ border: '1px solid black', width: '100%' }}
						value={item.filter}
						onChange={(e) => {
							let tempFilterState = [...filterState]
							tempFilterState[key].filter = e.target.value
							setFilterState(tempFilterState)
						}}
					/>
				</Grid>
			))}
			<Grid container item xs={12}>
				<Grid container justifyContent='flex-start' item xs={6}>
					<TablePagination
						component='div'
						count={props.totalDataRow}
						page={props.page}
						onPageChange={(
							event: React.MouseEvent<HTMLButtonElement> | null,
							newPage: number
						) => {
							props.setPage(newPage)
						}}
						rowsPerPageOptions={[10, 25, 50]}
						rowsPerPage={props.pageSize}
						onRowsPerPageChange={(
							event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
						) => {
							props.setPageSize(parseInt(event.target.value))
							props.setPage(0)
						}}
					/>
				</Grid>
				<Grid
					container
					justifyContent='flex-end'
					alignItems='center'
					item
					xs={6}
				>
					<Button
						sx={{ height: '60%', marginRight: '5%' }}
						variant='contained'
						onClick={() => props.handleSearchButton(filterState)}
					>
						Search
					</Button>
				</Grid>
			</Grid>
		</Grid>
	)
}

export default ListModalFooter
