import Vue from 'vue'
import Router from 'vue-router'
// import Home from '@/components/Home'
// import Login from '@/components/Login'
// import Editor from '@/components/Editor'
// import TestForm from '@/components/TestForm'
import Home from '@/pages/home'
import Login from '@/pages/login'
import Editor from '@/pages/editor'
import TestForm from '@/pages/newtestform'
import routerBefore from './before'

Vue.use(Router)

export default new Router({
  beforeEach: routerBefore,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        navigate: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        navigate: false
      }
    },
    {
      path: '/edit',
      name: 'Editor',

      component: Editor,
      meta: {
        navigate: true
      }
    },
    {
      path: '/newtest',
      name: 'New Test',

      component: TestForm,
      meta: {
        navigate: true
      }
    }
  ]
})
