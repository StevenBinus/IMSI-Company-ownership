import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { getMenuCheck } from '@components/api/getMenuCheck.api'

export const middleware = async (req: NextRequest) => {
	const res = NextResponse.next()

	const token = req.cookies.get('token')
	const url = req.nextUrl.pathname
	const invalidToken = token === undefined || token === null
	const invalidURL = url === '/' || url.includes('/auth')

	if (invalidToken && invalidURL) {
		return res
	}
	if (invalidToken && !invalidURL) {
		return NextResponse.redirect(new URL('/auth/login', req.url))
	}
	if (!invalidToken && invalidURL) {
		return NextResponse.redirect(new URL('/dashboard', req.url))
	}

	const menu = await getMenuCheck()

	if (menu === null) {
		return NextResponse.redirect(new URL('/unauthorized', req.url))
	}

	for (let index = 0; index < menu.length; index++) {
		const element = menu[index]
		if (req.nextUrl.pathname.includes(element)) {
			return res
		}
	}

	return NextResponse.redirect(new URL('/unauthorized', req.url))
}

// configuration for path that needed middleware
export const config = {
	matcher: ['/module/:path*', '/dashboard/:path*', '/auth/:path*'],
}
