import Home from '@/pages/home'
import Router from 'vue-router'
import { mount } from '@vue/test-utils'

describe('Home.vue', () => {
  it('should render correct contents', () => {
    const vm = mount(Home, { router: new Router() }).vm
    expect(vm.$el.querySelector('section h2').textContent).contains('Welcome!')
  })
})
