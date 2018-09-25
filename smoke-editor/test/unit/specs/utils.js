import Vue from 'vue'
import moxios from 'moxios'
import axios from 'axios'
import sinon from 'sinon'
import { equal } from 'assert'

describe('user authentication', function(){
    beforeEach((function) {
        moxios.install(http)
    })

    afterEach(function() {
        moxios.uninstall(http)
    })
    
    it('fetches the appropriate page for the user', (done) {
        moxios.stubRequest('localhost:8080/auth/login', {
            status: 200,
            responseText: 'Passed Test' 
            })
    })
})

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
