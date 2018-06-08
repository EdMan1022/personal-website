const pages = [
  {id: 1},
  {id: 2},
  {id: 3}
]

export function fetchPages () {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(pages)
    }, 30)
  })
}
