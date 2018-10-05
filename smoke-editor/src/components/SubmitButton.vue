<template>
  <button @click="clicked" class = "Button">
    Submit Button
  </button>
</template>

<script>
export default {
  methods: {
    clicked: function () {
      console.log('i was clicked!!!')
      console.log(this.editorCode)
      // We can base64 encode this.editorCode and 
      // send it to the API URL via an AJAX call
    }
  },
  props: ['editorCode']
}
</script>