import Vue from 'vue'
import moxios from 'moxios'

export async function expectAsync (status, resp) {
  moxios.wait(() => {
    let request = moxios.requests.mostRecent()
    request.respondWith({
      status: status,
      response: resp
    })
  })
}

export function mount (Component, options = {}) {
  const Constructor = Vue.extend(Component)
  Object.assign(Constructor.options, options)
  return new Constructor().$mount()
}
