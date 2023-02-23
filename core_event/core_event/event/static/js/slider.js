const output = document.querySelector('output')

const doThings = (event) => {
	const { value, min, max, step, parentElement: parent } = event.target
	const decimals = step && step.includes('.') ? step.split('.')[1] : 1
	const percent = `${((value - min)/(max - min) * 100).toFixed(decimals)}%`
	parent.style.setProperty('--p', percent)
  console.log('>>>>>>>>>>>>>', value)
	// output.value = `value: ${value} (${percent})`
}
