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
    <submit-button/>
  </div>
</template>

<script>
import Brace from 'vue-bulma-brace'
import SubmitButton from '@/components/SubmitButton'

export default {
  components: {
    Brace,
    SubmitButton
  }
}
</script>
