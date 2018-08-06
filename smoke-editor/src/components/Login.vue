<template>
  <columns>
    <column is-4 is-offset-4>
      <div id="main-login">
        <columns>
          <column is-5>
            <h2>Log In</h2>
            <h3 v-if="error !== ''">{{ geterror() }}</h3>
            <div class="form-group">
              <input
                type="text"
                class="form-control"
                placeholder="Enter your username"
                v-model="credentials.username"
              >
            </div>
            <div class="form-group">
              <input
                type="password"
                class="form-control"
                placeholder="Enter your password"
                v-model="credentials.password"
              >
            </div>
            <b-button id="submit" is-primary @click="submit()">Login</b-button>
          </column>
          <column is-8>
            <h1>
              TODO: Put social login buttons
            </h1>
          </column>
        </columns>
      </div>
    </column>
  </columns>
</template>

<style>
#main-login {
  padding: 20px;
  border: 1px solid lightgrey;
  border-radius: 4px;
}
</style>


<script>
import Auth from '@/auth'

export default {
  data () {
    return {
      credentials: {
        username: '',
        password: ''
      },
      error: ''
    }
  },

  methods: {
    submit (redir) {
      if (redir) {
        Auth.login(this, this.credentials, 'home')
      } else {
        Auth.login(this, this.credentials)
      }
    },
    geterror () {
      return this.error.msg || this.error.message || ''
    }
  }
}
</script>
