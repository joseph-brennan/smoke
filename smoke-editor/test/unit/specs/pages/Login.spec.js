import Login from '@/pages/login'
import store from '@/store'
import moxios from 'moxios'
import { expectAsync, mount } from '../utils'

describe('Login.vue', () => {
  let vm

  it('should render correct contents', () => {
    vm = mount(Login)
    expect(vm.$el.querySelector('#submit').textContent)
      .contains('Login')
  })

  describe('Auth', () => {
    beforeEach(() => {
      window.onbeforeunload = () => {}
      vm = mount(Login, {store: store})
      moxios.install()
    })

    afterEach(() => {
      moxios.uninstall()
    })

    it('should not set user on 401', (done) => {
      vm.$data.credentials.username = 'bogus'
      vm.$data.credentials.password = 'bogus'

      vm.user = null

      vm.login()
      expectAsync(401, {message: 'Unauthorized'})

      expect(vm.user).to.equal(null)

      done()
    })

    it('should set user on 200', (done) => {
      vm.$data.credentials.username = 'bogus'
      vm.$data.credentials.password = 'bogus'
      vm.login()
      expectAsync(200, { access_token: 'Hooray!' })
      expectAsync(200, { user: 42 })

      expect(vm.user).to.not.equal(null)

      done()
    })
  })
})
