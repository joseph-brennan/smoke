import Vue from 'vue'
import moxios from 'moxios'

function mount (Component, options) {
  const Constructor = Vue.extend(Component)
  Object.assign(Constructor.options, options)
  return new Constructor().$mount()
}

function expectAsync (resp, cb) {
  moxios.wait(() => {
    let req = moxios.requests.mostRecent()
    req.respondWith(resp).then(cb)
  })
}

export {
  mount,
  expectAsync
}
