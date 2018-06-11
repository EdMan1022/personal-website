import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api'

export function fetchPages () {
  return axios.get(`${API_URL}/pages/`)
}

const pages = [
  {
    'created': '2018-06-08T18:36:23.559000+00:00',
    'page_type': 'project',
    'id': 2,
    'block': [
      {
        'id': 2,
        'content': 'Test Content 2',
        'created': '2018-06-08T18:36:39.768000+00:00',
        'last_updated': '2018-06-08T18:36:41.233000+00:00'
      }
    ],
    'published': true,
    'last_updated': '2018-06-08T18:36:28.529000+00:00'
  },
  {
    'created': '2018-06-08T18:36:26.463000+00:00',
    'page_type': 'project',
    'id': 1,
    'block': [
      {
        'id': 1,
        'content': 'Test',
        'created': '2018-06-08T18:36:38.933000+00:00',
        'last_updated': '2018-06-08T18:36:40.524000+00:00'
      }
    ],
    'published': true,
    'last_updated': '2018-06-08T18:36:27.649000+00:00'
  }
]

export function bfetchPages () {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(pages)
    }, 30)
  })
}
