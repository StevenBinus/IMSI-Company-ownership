import { sleep } from '@utils/test.util'

export async function getStorageTypeById(storage_type_name: string) {
	await sleep(1e3)
	if (storage_type_name === 'string') {
		return {
			storage_type_id: 1,
			storage_type_name: 'string',
			storage_type_description: 'string',
			is_active: false,
		}
	}

	return null
}
