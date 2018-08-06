<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<style lang="sass">
@import '../node_modules/bulma/bulma.sass'
</style>


<script>
import Navbar from '@/components/Navbar'
import Auth from '@/auth'

export default {
  name: 'app',
  components: {
    Navbar
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
  }
}
</script>
