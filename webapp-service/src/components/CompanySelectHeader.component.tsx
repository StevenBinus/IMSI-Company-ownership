import { Autocomplete, Skeleton, TextField, useTheme } from '@mui/material'
import useUserStore from '@utils/store.util'
import React, { useEffect, useState } from 'react'
import { useGetCompanyList, Usercompany } from './api/getCompanyList.api'
import { getMenu } from './api/getMenu.api'
import { useRouter } from 'next/router'

const CompanySelectHeader = () => {
	const theme = useTheme()
	const { dataCompanyList, isLoadingCompanyListData } = useGetCompanyList()
	const router = useRouter()

	const store = useUserStore((state) => state)

	const [company, setCompany] = useState<number | null>(store.userStore.company)
	const [inputCompany, setInputCompany] = useState('')

	useEffect(() => {
		if (company !== store.userStore.company) {
			setCompany(store.userStore.company)
		}
	}, [store, company])

	const handleChangeCompany = async (data: Usercompany) => {
		setCompany(data.company_id)
		store.updateUserCompany(data.company_id)
		const menu = await getMenu()
		store.updateUserMenu(menu)
		store.updateUserModule('Dashboard')
		router.push('/dashboard')
	}

	if (isLoadingCompanyListData) {
		return (
			<Skeleton
				variant='rounded'
				width={'100%'}
				height={30}
				sx={{ marginBottom: '15px' }}
			/>
		)
	}

	return (
		<Autocomplete
			size='small'
			fullWidth
			disablePortal
			aria-label='autocomplete_select_company'
			id='autocomplete_select_company'
			disableClearable
			getOptionLabel={(option: any) => {
				if (typeof option !== 'object') {
					const company_result = dataCompanyList.find(
						(data) => data.company_id === option
					)
					return company_result.company_name ?? ''
				}
				return option.company_name
			}}
			isOptionEqualToValue={(option: any, value: any) => {
				return option.company_id === value
			}}
			value={company}
			onChange={(event, newValue: any | null) => {
				handleChangeCompany(newValue)
			}}
			inputValue={inputCompany}
			onInputChange={(event, newInputValue: string) => {
				setInputCompany(newInputValue)
			}}
			options={dataCompanyList}
			sx={{
				minWidth: '320px',
				width: '100%',
				display: 'inline-block',
				borderRadius: '5px',
				'&.Mui-focused .MuiInputLabel-outlined': {
					color: theme.palette.primary.main,
				},
				'& .MuiButtonBase-root': {
					color: theme.palette.primary.main,
				},
				'& .MuiAutocomplete-inputRoot': {
					color: theme.palette.primary.main,
					'& .MuiOutlinedInput-notchedOutline': {
						borderColor: theme.palette.primary.main,
					},
					'&:hover .MuiOutlinedInput-notchedOutline': {
						borderColor: theme.palette.primary.main,
					},
					'&.Mui-focused .MuiOutlinedInput-notchedOutline': {
						borderColor: theme.palette.primary.main,
					},
				},
			}}
			renderInput={(params) => (
				<TextField
					{...params}
					inputProps={{
						...params.inputProps,
						'aria-label': 'input_select_company',
					}}
					InputProps={{
						...params.InputProps,
						disableUnderline: true,
					}}
				/>
			)}
		/>
	)
}

export default CompanySelectHeader
