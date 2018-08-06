import Navbar from '@/components/Navbar'
import { mount } from './utils'
import Router from 'vue-router'

describe('Navbar.vue', () => {
  it('should render correct contents', () => {
    const vm = mount(Navbar, { router: new Router() })
    expect(vm.$el.querySelector('.navbar-brand')).to.not.equal(null)
  })
  it('should render correct provided routes', () => {
    let router = new Router({
      routes: [
        {
          path: '/',
          name: 'Home'
        },
        {
          path: '/login',
          name: 'Login'
        },
        {
          path: '/edit',
          name: 'Editor'
        }
      ]
    })
    const vm = mount(Navbar, {router: router})
    expect(vm.$el.querySelector('.navbar-brand').children).to.not.equal([])
    expect(vm.$el.querySelector('.navbar-brand').children.length).to.equal(3)
  })
})
