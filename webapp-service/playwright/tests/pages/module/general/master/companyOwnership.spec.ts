import { test, expect } from '@playwright/test'

test('deactivateCompanyOwnership', async ({ page }) => {
	await page.goto('/module/general/master/company-ownership')
	await page.getByRole('button', { name: 'List' }).click()
	await page.getByRole('cell', { name: 'string' }).first().dblclick()
	await page.getByRole('button', { name: 'Deactivate', exact: true }).click()

	const textfieldLocation = page.getByRole('textbox', {
		name: 'textfield-dms-is-active',
	})
	await expect(textfieldLocation).toHaveValue('Deactive')

	await page.getByRole('button', { name: 'Save' }).click()

	page.on('dialog', async (dialog) => {
		console.log(`Dialog message: ${dialog.message()}`)
		expect(dialog.type()).toContain('alert')
		dialog.dismiss().catch(() => {})
	})
})

test('activateCompanyOwnership', async ({ page }) => {
	await page.goto('/module/general/master/company-ownership')
	await page.getByRole('button', { name: 'List' }).click()
	await page.getByRole('cell', { name: 'strong' }).first().dblclick()
	await page.getByRole('button', { name: 'Activate', exact: true }).click()

	const textfieldLocation = page.getByRole('textbox', {
		name: 'textfield-dms-is-active',
	})
	await expect(textfieldLocation).toHaveValue('Active')

	await page.getByRole('button', { name: 'Save' }).click()

	page.on('dialog', async (dialog) => {
		console.log(`Dialog message: ${dialog.message()}`)
		expect(dialog.type()).toContain('alert')
		dialog.dismiss().catch(() => {})
	})
})
