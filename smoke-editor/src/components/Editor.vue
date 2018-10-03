<template>
  <div>
    <brace style="height: 500px"
      :fontsize="'12px'"
      :theme="'github'"
      :mode="'python'"
      :codefolding="'markbegin'"
      :softwrap="'free'"
      :selectionstyle="'text'"
      :highlightline="true">
    </brace>
  
    <button v-on:click="EncodeBase64 ()">Submit</button>
  
  </div>
</template>

<script>
import Brace from 'vue-bulma-brace'

export default {
  components: {
    Brace
  }
}
</script>
