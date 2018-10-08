<template>
  <div class = "editor">
  </div>
</template>



<script>
import Brace from 'vue-bulma-brace'
import Vue from 'vue'
import Buefy from 'buefy'
// import 'buefy/lib/buefy.css'

Vue.use(Buefy)

export default{
  data () {
    return {
      mode: 'Python 3'
    }
  },
  components: {
    Brace
  },
  methods: {
    changeMode (newMode) {
      console.log(this.mode)
      this.mode = newMode
      console.log(this.mode)
    }
  }
}
</script>
