<template>
  <button @click="clicked" class = "Button">
    Submit Button
  </button>
</template>

<script>
export default {
  data: function () {
    return {
      clicked: function () {
        console.log('i was clicked!!!')
      }
    }
  }
}
</script>