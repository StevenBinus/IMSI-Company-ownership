import React, { Dispatch, SetStateAction } from 'react'

interface StepOneProps {
	refresh: () => void
	setStep: Dispatch<SetStateAction<number>>
}
export const StepOne = (props: StepOneProps) => {
	return <div>StepOne</div>
}
