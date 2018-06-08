const pages = [
  {}
]

export function fetchPages () {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(pages)
    }, 30)
  })
}
