<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
    <button :onClick="encode64Click"></button>
  </div>
</template>

<style>
@import '../node_modules/bulma/css/bulma.css'
</style>


<script>
import Navbar from '@/components/Navbar'
import Auth from '@/auth'
import Button from '@/components/Button'

export default {
  name: 'app',
  components: {
    Navbar,
    Button 
  },

  data () {
    return {
      user: Auth.user
    }
  },

  methods: {
    logout () {
      Auth.logout()
    }
    encode64Click() {
        console.log('Encoding button clicked')
    }
  }
}
</script>
