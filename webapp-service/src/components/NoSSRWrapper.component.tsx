import dynamic from 'next/dynamic'
import { Fragment } from 'react'

const NoSSRWrapper = (props) => <Fragment>{props.children}</Fragment>
export default dynamic(() => Promise.resolve(NoSSRWrapper), {
	ssr: false,
})
