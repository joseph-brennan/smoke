import Login from '@/components/Login'
import moxios from 'moxios'
import { expectAsync, mount } from './utils'

describe('Login.vue', () => {
  it('should render correct contents', () => {
    const vm = mount(Login)
    expect(vm.$el.querySelector('div h2').textContent)
      .to.equal('Log In')
  })

  describe('Auth', () => {

    beforeEach(() => {
      window.onbeforeunload = () => {}
      moxios.install()
    })

    afterEach(() => {
      moxios.uninstall()
    })

    it('should set error message on 401', done => {
      const vm = mount(Login)
      vm.$data.credentials.username = 'bogus'
      vm.$data.credentials.password = 'bogus'
      vm.submit()
      expectAsync({
        status: 401,
        response: {
          message: 'Unauthorized'
        }
      }, () => {
        expect(vm.$data.error).contains('401')
        done()
      })
    })

    it('should set localStorage on 200', done => {
      const vm = mount(Login)
      vm.$data.credentials.username = 'bogus'
      vm.$data.credentials.password = 'bogus'
      vm.submit()
      expectAsync({
        status: 200,
        response: {
          access_token: 'Hooray!'
        }
      }, () => {
        expect(localStorage.getItem('access_token')).contains('Hooray!')
        done()
      })
    })
  })
})
