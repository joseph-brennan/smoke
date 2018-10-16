import moxios from 'moxios'

function stubAsync (resource, resp) {
  const API_URL = process.env.API_URL || 'http://localhost:8000'
  moxios.stubRequest(API_URL + resource, resp)
}

export {
  stubAsync
}
