<template>
  <div id="app">
    <nav
      class="navbar header has-shadow is-dark"
      role="navigation"
      aria-label="main navigation">
      <div class="navbar-brand">
        <router-link
          v-for="link in links"
          :key="link.path"
          :to="link.path"
          class="navbar-item">
          {{ link.name }}
        </router-link>
      </div>
      <div class="navbar-menu navbar-end">
        <a
          v-if="isLoggedIn"
          class="navbar-item navbar-item"
          @click="logout">
          Logout
        </a>
        <router-link
          v-else
          class="navbar-item navbar-item"
          to="/login">
          Login
        </router-link>
      </div>
    </nav>
    <section class="main-content columns">
      <router-view />
    </section>
  </div>
</template>

<script>
import store from '@/store'

export default {
  name: 'app',
  created () {
    this.$router.options.routes.forEach(route => {
      if (!!route.meta && route.meta.navigate) {
        this.links.push({
          name: route.name,
          path: route.path
        })
      }
    })
  },

  data () {
    return {
      links: []
    }
  },
  computed: {
    user () {
      return store.state.user
    },
    isLoggedIn () {
      return !!store.state.user
    }
  },
  methods: {
    async logout () {
      try {
        await store.dispatch('logout')
        this.$router.push('/login')
      } catch (err) {
        // uncomment below whenever user priveleges are implemented
        // store.state.user = '0'
      }
    }
  }
}
</script>
