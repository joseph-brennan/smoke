import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import {API_URL} from '@/definitions'
import store from '@/store'

Vue.use(Vuex)

const state = () => ({
  auth: null,
  user: null
})

const mutations = {
  SET_AUTH: function (state, tokens) {
    state.auth = tokens
  },
  SET_USER: function (state, user) {
    state.user = user
  }
}

const actions = {
  async login ({ commit }, { username, password }) {
    let resp = await axios.post(API_URL + '/auth/login', {
      username,
      password
    })

    commit('SET_AUTH', resp.data)
    resp = await axios.get(API_URL + '/api/v1/me', {
      headers: {
        Authorization: `Bearer ${resp.data.access_token}`
      }
    })
    if (resp.status >= 200 && resp.status < 300) {
      commit('SET_USER', resp.data.user)
    }
  },

  async logout ({ commit }) {
    if (store.state.auth && store.state.auth.access_token) {
      await axios.delete(API_URL + '/auth/logout', {
        headers: {
          Authorization: `Bearer ${store.state.auth.access_token}`
        }
      })
    }
    commit('SET_USER', null)
    commit('SET_AUTH', null)
  }
}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  plugins: [
    createPersistedState({key: 'smoke'})
  ]
})
