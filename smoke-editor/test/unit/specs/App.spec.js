import App from '@/App'
import Router from 'vue-router'
import { mount } from '@vue/test-utils'
import store from '@/store'
import { stubAsync } from './utils'


describe('App.vue', () => {
  let wrapper, vm = undefined, undefined

  beforeEach(() => {
    let router = new Router({
      routes: [
        {
          path: '/',
          name: 'Home',
          meta: {
            navigate: true
          }
        },
        {
          path: '/:id',
          name: 'Should not exist'
        }
      ]
    })
    wrapper = mount(App, {router: router, store: store})
    vm = wrapper.vm
  })

  it('should render correct contents', () => {
    expect(vm.isLoggedIn).to.be.equal(false)
  })

  it('should not logout unless logged in', (done) => {
    const loggedIn = vm.isLoggedIn
    stubAsync('/auth/logout', {
      status: 200,
      response: {
        success: true
      }
    })
    vm.logout().then(() => {
      expect(vm.isLoggedIn).to.equal(loggedIn)
      expect(vm.user).to.equal(null)
    }).then(done, done)
  })

  it('should logout if backend fails', (done) => {
    store.state.auth = { access_token: true }
    stubAsync('/auth/logout', {
      status: 401
    })
    vm.logout().then(() => {
      expect(vm.user).to.equal(null)
    }).then(done, done)
  })

  it('should logout if logged in', (done) => {
    store.state.user = 42
    const isLoggedIn = vm.isLoggedIn
    stubAsync('/auth/logout', {
      status: 200,
      response: {
        msg: 'Success'
      }
    })
    vm.logout().then(() => {
      expect(vm.user).to.equal(null)
      expect(vm.isLoggedIn).to.not.equal(isLoggedIn)
    }).then(done, done)
  })

  it('should add links to navigatable routes', () => {
    expect(vm.links).to.have.length(1)
  }
)
})
