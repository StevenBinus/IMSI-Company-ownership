// auth.setup.ts
import { expect, test as setup } from '@playwright/test'

const authFile = 'playwright/tests/user.json'

setup('authenticate', async ({ page }) => {
	// Perform authentication steps.
	await page.goto('/')
	await page.locator('#user_id').click()
	await page.locator('#user_id').fill('50637')
	await page.locator('#password').click()
	await page.locator('#password').fill('Img50637')
	await page.getByRole('button', { name: 'Login' }).click()

	// Wait until the page receives the cookies.
	// Wait for the final URL to ensure that the cookies are actually set.
	await expect(page).toHaveURL('/dashboard')

	// End of authentication steps.
	await page.context().storageState({ path: authFile })
})
