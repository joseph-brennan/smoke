import Login from '@/pages/login'
import moxios from 'moxios'
import { stubAsync } from '../utils'
import { mount } from '@vue/test-utils'

describe('Login.vue', () => {
  let wrapper, vm = undefined, undefined

  it('should render correct contents', () => {
    vm = mount(Login).vm
    expect(vm.$el.querySelector('#submit').textContent)
      .contains('Login')
  })

  describe('Auth', () => {
    beforeEach(() => {
      window.onbeforeunload = () => {}
      moxios.install()
      wrapper = mount(Login)
      vm = wrapper.vm
    })

    afterEach(() => {
      moxios.uninstall()
    })

    it('should set error message on 401', (done) => {
      vm.$data.credentials.username = 'bogus'
      vm.$data.credentials.password = 'bogus'
      stubAsync('/auth/login', {
        status: 401,
        response: {
          message: 'Unauthorized'
        }
      })

      wrapper.vm.login().then(() => {
        expect(vm.geterror()).contains('401')
        expect(vm.geterror()).contains('401')
      }).then(done, done)
    })

    it('should not set error message on 200', (done) => {
      vm.$data.credentials.username = 'bogus'
      vm.$data.credentials.password = 'bogus'
      stubAsync('/auth/login', {
        status: 200,
        response: {
          access_token: 'Hooray!'
        }
      })

      stubAsync('/api/v1/me', {
        status: 200,
        response: {
          user: 42
        }
      })

      wrapper.vm.login().then(() => {
        expect(vm.user).to.not.equal(null)
        expect(vm.geterror()).to.equal('')
      }).then(done, done)
    })
  })
})
