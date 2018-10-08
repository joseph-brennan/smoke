<template>
  <button @click="clicked" class = "Button">
    Submit Button
  </button>
</template>

<script>
import axios from 'axios'

export default {
  methods: {
    clicked: function () {
      axios.post('/API/v1/test', {
        data: window.btoa(this.editorCode)
      })
    }
  },
  props: ['editorCode']
}
</script>