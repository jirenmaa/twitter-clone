import router from '@/routes'

/**
 * stop any default behavior of event
 */
export function stopEvent (event: Event): void {
  event.cancelBubble = true
  if (event.stopPropagation) {
    event.stopPropagation()
    event.preventDefault()
  }
}

/**
 * replace dash string to camel case string
 */
export function dashToCamelCase (str: string): string {
  return str.replace(/-([a-z])/g, (g) => g[1].toUpperCase())
}

/**
 * replace camel case string to dash string
 */
export function camelToDashCase (str: string): string {
  return str.replace(/([A-Z])/g, (g) => `-${g[0].toLowerCase()}`)
}

export function formatNumWithAbbreviation (count: number): string {
  if (count < 1 || count === undefined) {
    return ''
  }

  const abbreviation = 'kmb'
  const base = Math.floor(Math.log(Math.abs(count)) / Math.log(1000))
  const suffix = abbreviation[Math.min(2, base - 1)]
  const basedNumber = abbreviation.indexOf(suffix) + 1

  const setPrecisionNumber = count / Math.pow(1000, basedNumber)
  const precision = Math.pow(10, 2)
  const precisionRounded = Math.round(setPrecisionNumber * precision) / precision

  return suffix ? (precisionRounded + suffix) : ('' + count)
}

/**
 * push route to given url and parameter
 */
// eslint-disable-next-line
export function redirect (event: any, url: string, parameters: any) {
  // get event click by user and check if link does have attribute `data-event`
  const target = event.currentTarget.attributes['data-event']
  // set route to given url and parameter
  const routed = { name: url, params: parameters }

  if (target?.specified) {
    // prevent user to double click on tweet that will
    // redirect user to :detail and then :user-profile
    router.push(routed)
    stopEvent(event)
  } else {
    router.push(routed)
  }
}

const helper = { stopEvent, redirect, formatNumWithAbbreviation }
export default helper
