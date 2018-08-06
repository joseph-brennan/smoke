// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Resource from 'vue-resource'
import Bulma from 'vue-bulma-components'
import App from './App'
import Auth from './auth'
import router from './router'

Vue.use(Resource)
Vue.use(Bulma)
Vue.config.productionTip = false

Vue.http.headers.common['Authorization'] = `Bearer ${localStorage.getItem('id_token')}`

// Check the user's auth status when the app starts
Auth.checkAuth()

/* eslint-disable no-new */
const app = new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

export default app
