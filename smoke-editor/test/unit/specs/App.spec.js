import App from '@/App'
import Router from 'vue-router'
import store from '@/store'
import moxios from 'moxios'
import { expectAsync, mount } from './utils'

describe('App.vue', () => {
  let vm

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
    vm = mount(App, {router: router, store: store})
    moxios.install()
  })

  afterEach(() => {
    moxios.uninstall()
  })

  it('should render correct contents', () => {
    expect(vm.isLoggedIn).to.be.equal(false)
  })

  it('should not logout unless logged in', (done) => {
    store.state.auth = false
    const isLoggedIn = vm.isLoggedIn
    vm.logout()
    expectAsync(200, {msg: 'Success'})

    expect(vm.user).to.equal(null)
    expect(vm.isLoggedIn).to.equal(isLoggedIn)

    done()
  })

  it('should logout if backend fails', (done) => {
    store.state.auth = { access_token: true }
    vm.logout()
    expectAsync(401, {})

    expect(vm.user).to.equal(null)

    done()
  })

  it('should logout if logged in', (done) => {
    store.state.auth = {access_token: true}
    vm.logout()
    expectAsync(200, {msg: 'Success'})

    expect(vm.user).to.equal(null)

    done()
  })

  it('should add links to navigatable routes', () => {
    expect(vm.links).to.have.length(1)
  })
})
