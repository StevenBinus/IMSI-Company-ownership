export function formatNumber(inputNumber: any) {
	if (inputNumber === undefined || inputNumber === null) {
		return 0
	}
	const removeNonNumeric = (num: any) => num.toString().replace(/[^0-9]/g, '')

	return Number(removeNonNumeric(inputNumber))
}

export default function separateNumber(inputNumber: any) {
	if (inputNumber === undefined || inputNumber === null) {
		return 0
	}
	const addCommas = (num: any) =>
		num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
	const removeNonNumeric = (num: any) => num.toString().replace(/[^0-9]/g, '')
	return addCommas(removeNonNumeric(inputNumber))
}
