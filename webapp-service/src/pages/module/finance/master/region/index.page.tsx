import Layout from '@components/Layout.component'
import { eraseCookie } from '@utils/cookies.util'
import useUserStore from '@utils/store.util'
import { useRouter } from 'next/router'
import { useState } from 'react'
import { StepOne } from './component/StepOne.component'

interface ProvinceMasterProps {
	refresh: () => void
}

const ProvinceMaster = (props: ProvinceMasterProps) => {
	const [counter, setCounter] = useState(0)
	const router = useRouter()
	const logout = () => {
		useUserStore.persist.clearStorage()
		eraseCookie('')
		router.push('/')
	}
	return (
		<>
			Region Master {counter}{' '}
			<button onClick={() => setCounter(counter + 1)}>Add Point</button>{' '}
			<button onClick={props.refresh}>Reload</button>{' '}
			<button onClick={logout}>Logout</button>{' '}
		</>
	)
}

const ProvinceMasterPage = () => {
	const [seed, setSeed] = useState(1)
	const reset = () => {
		setSeed(Math.random())
	}

	const [step, setStep] = useState(0)

	switch (step) {
		case 0:
			return (
				<Layout>
					<ProvinceMaster key={seed} refresh={reset} />
				</Layout>
			)

		case 1:
			return (
				<Layout>
					<StepOne key={seed} refresh={reset} setStep={setStep} />
				</Layout>
			)

		default:
			return (
				<Layout>
					<ProvinceMaster key={seed} refresh={reset} />
				</Layout>
			)
	}
}

export default ProvinceMasterPage
