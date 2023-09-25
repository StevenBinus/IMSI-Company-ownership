export const recursivelyFindKeyValueList = (key, keyValue, list, depth = 0) => {
	let results = []

	for (let i = 0; i < list.length; i++) {
		const item = list[i]

		for (const key of Object.keys(item)) {
			//check if its not an array

			if (Array.isArray(item[key])) {
				let res = recursivelyFindKeyValueList(
					key,
					keyValue,
					item[key],
					depth + 1
				)
				results = results.concat(res)
			}
			//we have found it
			else if (
				item[key] &&
				results.findIndex((data) => data.label === item['title']) === -1 &&
				item['url'] !== undefined
			) {
				//found, return the list
				results.push({ label: item['title'], id: item['url'] })
			}
		}
	}

	return results
}

export const recursivelyFindKeyValue = (key, keyValue, list) => {
	for (let i = 0; i < list.length; i++) {
		const item = list[i]

		for (const key of Object.keys(item)) {
			//check if its array of more options, search it
			if (Array.isArray(item[key])) {
				const res = recursivelyFindKeyValue(key, keyValue, item[key])
				if (res.found === true) return res
			}
			//Test the keyValue
			else if (item[key] === keyValue) {
				//found, return the list
				console.log('found ', keyValue)
				return { found: true, value: item }
			}
		}
	}

	return { found: false, value: {} }
}
