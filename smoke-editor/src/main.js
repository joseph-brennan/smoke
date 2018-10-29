// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Resource from 'vue-resource'
import Buefy from 'buefy'
import { abilitiesPlugin } from '@casl/vue'

import App from './App'
import router from './router'
import store from './store'
import auth from './auth'

import 'buefy/dist/buefy.css'

Vue.use(Resource)
Vue.use(Buefy)
Vue.use(abilitiesPlugin)

Vue.config.productionTip = false

/* eslint-disable no-new */
const vm = new Vue({
  el: '#app',
  router,
  store,
  auth,
  template: '<App/>',
  components: { App }
})

export default vm
