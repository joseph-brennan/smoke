import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Editor from '@/components/Editor'
import TestForm from '@/components/TestForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/edit',
      name: 'Editor',
      component: Editor
    },
    {
      path: '/newtest',
      name: 'TestForm',
      component: TestForm
    }
  ]
})
