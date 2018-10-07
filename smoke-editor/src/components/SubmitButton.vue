<template>
  <button @click="clicked" class = "Button">
    Submit Button
  </button>
</template>

<script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">
</script>

export default {
  methods: {
    clicked: function () {
      console.log('i was clicked!!!')
      console.log(this.editorCode)
      // We can base64 encode this.editorCode and
      // send it to the API URL via an AJAX call

      var encodedObject = window.btoa(this.editorCode)

      $(document).ready(function () {
        $('button').click(function () {
          $.post('API_v1_test',
            {
              data: encodedObject
            })
        })
      })
    }
  },
  props: ['editorCode']
}
</script>