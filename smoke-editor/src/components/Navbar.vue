<template>
  <navbar is-dark role="navigation" aria-label="main navigation">
    <navbar-brand>
      <router-link 
            v-for="link in links"
            :key="link.path"
            :to="link.path"
            class="navbar-item">
        {{ link.name }}
      </router-link>
    </navbar-brand>
  </navbar>
</template>

<style scoped>
.navbar {
  margin-bottom: 1em;
}
</style>


<script>
export default {
  created () {
    this.$router.options.routes.forEach(route => {
      if (!/:/.test(route.path)) {
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
  }
}
</script>
