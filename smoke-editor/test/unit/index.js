import Vue from 'vue'
import Buefy from 'buefy'
import Resource from 'vue-resource'
import Router from 'vue-router'
import Vuex from 'vuex'

Vue.use(Router)
Vue.use(Resource)
Vue.use(Buefy)
Vue.use(Vuex)
Vue.config.productionTip = false

// require all test files (files that ends with .spec.js)
const testsContext = require.context('./specs', true, /\.spec$/)
testsContext.keys().forEach(testsContext)

// require all src files except main.js for coverage.
// you can also change this to match only the subset of files that
// you want coverage for.
const srcContext = require.context('../../src', true, /^(?!main)\.(js|vue)$/)
srcContext.keys().forEach(srcContext)
