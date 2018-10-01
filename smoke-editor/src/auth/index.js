import axios from 'axios'
import Router from '@/router'

const API_URL = 'http://localhost:8000/'
const LOGIN_URL = API_URL + 'auth/login'

export default {
  user: {
    authenticated: false,
    username: null,
    email: '',
    permission: ''
  },

  login (context, creds, redirect) {
    axios({
      method: 'POST',
      url: LOGIN_URL,
      withCredentials: false,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      data: creds
    }).then(
      resp => {
        localStorage.setItem('access_token', resp.data.access_token)

        this.user.authenticated = true
        this.user.username = resp.data.user.username
        this.user.email = resp.data.user.email
        this.user.permission = resp.data.user.permission

        if (redirect) {
          Router.go(redirect)
        }
      },
      err => {
        context.error = err.message
      }
    )
  },

  logout () {
    localStorage.removeItem('access_token')
    this.user.authenticated = false
  },

  checkAuth () {
    var jwt = localStorage.getItem('access_token')
    if (jwt) {
      this.user.authenticated = true
    } else {
      this.user.authenticated = false
    }
  }
}
