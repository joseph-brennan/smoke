<template>
  <section
    id="main-login"
    class="section">
    <h3
      v-if="error !== ''">
      {{ geterror() }}
    </h3>
    <b-field
      label="Username">
      <b-input
        v-model="credentials.username"
        type="text"/>
    </b-field>
    <b-field
      label="Password">
      <b-input
        v-model="credentials.password"
        type="password"/>
    </b-field>
    <button
      id="submit"
      class="button"
      is-primary
      @click="login">
      Login
    </button>
  </section>
</template>


<script>
import store from '@/store'

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
    async login () {
      try {
        await store.dispatch('login', {
          username: this.credentials.username,
          password: this.credentials.password
        })
        this.$emit('login', store.state.user)
        this.$router.push('/')
      } catch (err) {
        this.error = err
      }
    },
    geterror () {
      return this.error.msg || this.error.message || ''
    }
  }
}
</script>
