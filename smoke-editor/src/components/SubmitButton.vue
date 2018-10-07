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
      console.log('i was clicked!!!')
      console.log(this.editorCode)
      // We can base64 encode this.editorCode and
      // send it to the API URL via an AJAX call

      var encodedObject = window.btoa(this.editorCode)

      axios.post('API/v1/test', {
        data: encodedObject
      })
    }
  },
  props: ['editorCode']
}
</script>