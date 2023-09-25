import dynamic from 'next/dynamic'
import { Box, Grid, Typography, useTheme } from '@mui/material'
import { GridColDef, GridValueGetterParams } from '@mui/x-data-grid'
import { useFormik } from 'formik'
import { useState } from 'react'
import { object, string } from 'yup'
import TextFieldDMS from '@components/TextFieldDMS.component'
import ToolbarMaster from '@components/ToolbarMaster.component'
import useUserStore from '@utils/store.util'
import { AreaListProps, getAllArea } from './api/getAllArea.api'
import { AreaProps, getAreaById } from './api/getAreaById.api'
import { getAreaByCode } from './api/getAreaByCode.api'
import { getRegionByCode } from '../region/api/getRegionByCode.api'
import { RegionListProps, getAllRegion } from '../region/api/getAllRegion.api'
import { getRegionById } from '../region/api/getRegionById.api'
import { dataColumnRegion } from '../region/index.page'
import TextFieldLookUpDMS from '@components/TextFieldLookUpDMS.component'
import { AxiosError } from 'axios'
const PageLoad = dynamic(() => import('@components/PageLoad.component'))
const ListModal = dynamic(() => import('@components/ListModal.component'))

const validationSchema = object({
	sales_area_code: string().required('Sales Area Code is required'),
	region_code: string().required('Regional Code  is required'),
	description: string().required('Record Status is required'),
})

export const dataColumnArea: GridColDef[] = [
	{
		field: 'area_code',
		headerName: 'Sales Area Code',
		flex: 1,
	},
	{
		field: 'description',
		headerName: 'Description',
		flex: 2,
	},
	{
		field: 'is_active',
		headerName: 'Status',
		flex: 1,
		renderCell: (params: GridValueGetterParams) => {
			return (
				<Typography>
					{Boolean(params.row.is_active) ? 'Active' : 'Deactive'}
				</Typography>
			)
		},
	},
]

const RegionMasterPage = () => {
	const theme = useTheme()
	const [listModalArea, setListModalArea] = useState(false)
	const [listModalRegion, setListModalRegion] = useState(false)
	const [dataRowModalArea, setDataRowModalArea] = useState([])
	const [dataRowModalRegion, setDataRowModalRegion] = useState([])
	const [isLoading, setIsLoading] = useState(false)

	const [areaTotalData, setAreaTotalData] = useState(0)
	const [areaPage, setAreaPage] = useState(0)
	const [areaPageSize, setAreaPageSize] = useState(10)
	const [areaQueryOf, setAreaQueryOf] = useState<string | null>()
	const [areaQueryBy, setAreaQueryBy] = useState<string | null>()

	const [regionTotalData, setRegionTotalData] = useState(0)
	const [regionPage, setRegionPage] = useState(0)
	const [regionPageSize, setRegionPageSize] = useState(10)
	const [regionQueryOf, setRegionQueryOf] = useState<string[] | null>()
	const [regionQueryBy, setRegionQueryBy] = useState<string[] | null>()

	const store = useUserStore((state) => state)

	const formik = useFormik({
		initialValues: {
			area_id: null,
			sales_area_code: '',
			area_description: '',
			region_id: '',
			region_code: '',
			region_name: '',
			is_active: 'Active',
		},
		validationSchema: validationSchema,
		onSubmit: (values) => {
			alert(JSON.stringify(values, null, 2))
		},
	})

	const handleOpenListModalArea = async () => {
		setIsLoading(true)
		await getAllArea(areaPage, areaPageSize, areaQueryOf, areaQueryBy)
			.then((response) => {
				setAreaTotalData(response.total_rows)
				setDataRowModalArea(response.data)
				setListModalArea(true)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
				setDataRowModalArea([])
			})
		setIsLoading(false)
	}
	const handleCloseListModalArea = () => {
		setListModalArea(false)
	}
	const handleOnDoubleClickListModalArea = async (row: AreaListProps) => {
		if (row !== null) {
			await getAreaById(row.area_id)
				.then((response) => {
					formik.setFieldValue(
						'is_active',
						response.data.is_active ? 'Active' : 'Deactive'
					)
					formik.setFieldValue('sales_area_code', response.data.area_code)
					formik.setFieldValue('area_description', response.data.description)
					formik.setFieldValue('region_id', response.data.region_id)
					formik.setFieldValue('region_code', response.data.region_code)
					formik.setFieldValue('region_name', response.data.region_name)
					formik.setFieldValue('area_id', response.data.area_id)
					setListModalArea(false)
				})
				.catch((error: AxiosError) => {
					alert(error.message)
				})
		}
	}

	const handleDataRowIdListModalArea = (row: AreaProps) => {
		return row.area_id
	}

	const handleOnBlurArea = async () => {
		const areaData = await getAreaByCode(formik.values.sales_area_code)
		if (areaData !== null) {
			formik.setFieldValue(
				'is_active',
				areaData.is_active ? 'Active' : 'Deactive'
			)
			formik.setFieldValue('sales_area_code', areaData.sales_area_code)
			formik.setFieldValue('area_description', areaData.area_description)
			formik.setFieldValue('region_id', areaData.region_id)
			formik.setFieldValue('region_code', areaData.region_code)
			formik.setFieldValue('region_name', areaData.region_name)
			formik.setFieldValue('area_id', areaData.area_id)
		}
	}

	const handleOpenListModalRegion = async () => {
		setIsLoading(true)
		const regionData = await getAllRegion(
			regionPage,
			regionPageSize,
			regionQueryOf,
			regionQueryBy
		)
		if (regionData !== null) {
			setRegionTotalData(14)
			setDataRowModalRegion(regionData.data)
			setIsLoading(false)
			setListModalRegion(true)
		}
	}

	const handleCloseListModalRegion = () => {
		setRegionPage(0)
		setRegionPageSize(10)
		setRegionQueryBy(null)
		setRegionQueryOf(null)
		setListModalRegion(false)
	}

	const handleOnDoubleClickListModalRegion = async (row: RegionListProps) => {
		if (row !== null) {
			formik.setFieldValue('region_id', row.region_id)
			formik.setFieldValue('region_code', row.region_code)
			formik.setFieldValue('region_name', row.region_name)
			setListModalRegion(false)
		}
	}

	const handleDataRowIdListModalRegion = (row: RegionListProps) => {
		return row.region_id
	}

	const handleOnBlurRegion = async () => {
		const regionData = await getRegionByCode(formik.values.region_code)
		if (regionData !== null) {
			formik.setFieldValue(
				'is_active',
				regionData.is_active ? 'Active' : 'Deactive'
			)
			formik.setFieldValue('region_id', regionData.region_id)
			formik.setFieldValue('region_code', regionData.region_code)
			formik.setFieldValue('region_name', regionData.region_name)
			formik.setFieldValue('user_id', regionData.user_id)
			formik.setFieldValue('NIK', regionData.NIK)
			formik.setFieldValue('user_name', regionData.user_name)
		}
	}

	const activeButtonValue = () => {
		if (formik.values.area_id === null) return true
		if (formik.values.is_active === 'Active') return true

		return false
	}

	const handleActiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Active')
	}

	const deactiveButtonValue = () => {
		if (formik.values.area_id === null) return true
		if (formik.values.is_active === 'Deactive') return true

		return false
	}
	const handleDeactiveButtonListModal = () => {
		formik.setFieldValue('is_active', 'Deactive')
	}

	const handleRegionSortTable = async (data: any) => {
		setIsLoading(true)
		const dataString = JSON.stringify(data)
		// setRegionQueryBy(dataString)
		// await getAllRegion(regionPage, regionPageSize, dataString, regionQueryBy)
		// 	.then((response) => {
		// 		setRegionTotalData(14)
		// 		setDataRowModalRegion(response.data)
		// 	})
		// 	.catch((error: AxiosError) => {
		// 		alert(error.message)
		// 		setDataRowModalRegion([])
		// 	})
		setIsLoading(false)
		setListModalRegion(true)
	}

	const handleRegionSearch = async (data: any) => {
		setIsLoading(true)
		const dataQueryBy = data.map((item) => item.field)
		const dataQueryOf = data.map((item) => item.filter)
		console.log(dataQueryBy)
		setRegionQueryOf(dataQueryOf)
		setRegionQueryBy(dataQueryBy)
		// await getAllRegion(regionPage, regionPageSize, dataQueryOf, dataQueryBy)
		// 	.then((response) => {
		// 		setRegionTotalData(14)
		// 		setDataRowModalRegion(response.data)
		// 	})
		// 	.catch((error: AxiosError) => {
		// 		alert(error.message)
		// 		setDataRowModalRegion([])
		// 	})
		setIsLoading(false)
		setListModalRegion(true)
	}

	const handleRegionPage = async (data: number) => {
		setIsLoading(true)
		setRegionPage(data)
		await getAllRegion(data, regionPageSize, regionQueryOf, regionQueryBy)
			.then((response) => {
				setRegionTotalData(14)
				setDataRowModalRegion(response.data)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
				setDataRowModalRegion([])
			})
		setIsLoading(false)
		setListModalRegion(true)
	}

	const handleRegionPageSize = async (data: number) => {
		setIsLoading(true)
		setRegionPageSize(data)
		await getAllRegion(regionPage, data, regionQueryOf, regionQueryBy)
			.then((response) => {
				setRegionTotalData(14)
				setDataRowModalRegion(response.data)
			})
			.catch((error: AxiosError) => {
				alert(error.message)
				setDataRowModalRegion([])
			})
		setIsLoading(false)
		setListModalRegion(true)
	}

	return (
		<>
			<PageLoad loading={isLoading} />
			<ListModal
				open={listModalArea}
				handleClose={handleCloseListModalArea}
				dataColumn={dataColumnArea}
				dataRow={dataRowModalArea}
				handleDataRowId={handleDataRowIdListModalArea}
				handleOnDoubleClick={handleOnDoubleClickListModalArea}
			/>
			<ToolbarMaster
				DisableBackButton
				DisableNextButton
				DisableActiveButton={activeButtonValue()}
				handleActiveButton={handleActiveButtonListModal}
				DisableDeactiveButton={deactiveButtonValue()}
				handleDeactiveButton={handleDeactiveButtonListModal}
				handleSaveButton={formik.handleSubmit}
				handleListButton={handleOpenListModalArea}
				handleNewButton={store.updateUserSeed}
			/>
			<Grid
				container
				item
				alignItems='center'
				direction='column'
				sx={{ minHeight: '89.9vh' }}
			>
				<Grid
					container
					item
					sx={{
						padding: '2% 12%',
						margin: '2%',
						width: '90%',
						borderRadius: '5px',
						backgroundColor: theme.palette.background.paper,
					}}
				>
					<Grid container item maxWidth='1000px'>
						<TextFieldDMS
							disabled
							id='is_active'
							label={
								<span>
									Record Status{' '}
									<span style={{ color: theme.palette.error.main }}>*</span>
								</span>
							}
							value={formik.values.is_active}
							onChange={formik.handleChange}
							error={
								formik.touched.is_active && Boolean(formik.errors.is_active)
							}
							helperText={formik.touched.is_active && formik.errors.is_active}
						/>
						<TextFieldDMS
							id='sales_area_code'
							label={
								<span>
									Sales Area Code{' '}
									<span style={{ color: theme.palette.error.main }}>*</span>
								</span>
							}
							value={formik.values.sales_area_code}
							onChange={formik.handleChange}
							onBlur={handleOnBlurArea}
							error={
								formik.touched.sales_area_code &&
								Boolean(formik.errors.sales_area_code)
							}
							helperText={
								formik.touched.sales_area_code && formik.errors.sales_area_code
							}
						/>
						<TextFieldLookUpDMS
							descriptionValue={formik.values.region_name}
							id='region_code'
							label={
								<span>
									Regional Code{' '}
									<span style={{ color: theme.palette.error.main }}>*</span>
								</span>
							}
							value={formik.values.region_code}
							onChange={formik.handleChange}
							error={
								formik.touched.region_code && Boolean(formik.errors.region_code)
							}
							helperText={
								formik.touched.region_code && formik.errors.region_code
							}
							dataColumn={dataColumnRegion}
							dataRow={dataRowModalRegion}
							listModal={listModalRegion}
							handleDataRowId={handleDataRowIdListModalRegion}
							handleOnDoubleClick={handleOnDoubleClickListModalRegion}
							handleOnBlur={handleOnBlurRegion}
							handleOpenListModal={handleOpenListModalRegion}
							handleCloseListModal={handleCloseListModalRegion}
							totalDataRow={regionTotalData}
							page={regionPage}
							setPage={handleRegionPage}
							pageSize={regionPageSize}
							setPageSize={handleRegionPageSize}
							handleSortTable={handleRegionSortTable}
							handleSearchButton={handleRegionSearch}
						/>
						<TextFieldDMS
							id='area_description'
							label={
								<span>
									Description{' '}
									<span style={{ color: theme.palette.error.main }}>*</span>
								</span>
							}
							value={formik.values.area_description}
							onChange={formik.handleChange}
							error={
								formik.touched.area_description &&
								Boolean(formik.errors.area_description)
							}
							helperText={
								formik.touched.area_description &&
								formik.errors.area_description
							}
						/>
					</Grid>
				</Grid>
			</Grid>
		</>
	)
}

export default RegionMasterPage
