import { sleep } from '@utils/test.util'

export interface StorageTypeProps {
	storage_type_id: number
	storage_type_name: string
	storage_type_description: string
	is_active: boolean
}

export async function getAllStorageType() {
	await sleep(1e3)
	return [
		{
			storage_type_id: 1,
			storage_type_name: 'string',
			storage_type_description: 'string',
			is_active: true,
		},
		{
			storage_type_id: 2,
			storage_type_name: 'strong',
			storage_type_description: 'strong',
			is_active: true,
		},
	]
}
