import App from '@/App'
import Router from 'vue-router'
import { mount } from './utils'

describe('App.vue', () => {
  it('should render correct contents', () => {
    const vm = mount(App, { router: new Router() })
    expect(vm.user.authenticated).to.be.equal(false)
  })

  it('should not logout unless logged in', () => {
    let router = new Router({
      routes: [
        {
          path: '/',
          name: 'Home'
        },
        {
          path: '/:id',
          name: 'Should not exist'
        }
      ]
    })
    const vm = mount(App, {router: router})
    const loggedIn = vm.user.authenticated
    vm.logout()
    expect(vm.user.authenticated).to.equal(loggedIn)
  })
})
