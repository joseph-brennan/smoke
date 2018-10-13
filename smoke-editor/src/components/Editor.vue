<template>
  <div>
    <brace style="height: 500px"
      :fontsize="'12px'"
      :theme="'github'"
      :mode="'python'"
      :codefolding="'markbegin'"
      :softwrap="'free'"
      :selectionstyle="'text'"
      :highlightline="true" v-on:code-change="editorCodeChanged">
    </brace>
    <submit-button :editorCode="editorCodeString" />
  </div>
</template>

<script>
import Brace from 'vue-bulma-brace'
import SubmitButton from '@/components/SubmitButton'

export default {
  components: {
    Brace,
    SubmitButton
  },
  methods: {
    editorCodeChanged: function (newCodeString) {
      this.editorCodeString = newCodeString
    }
  },
  data: function () {
    return {
      editorCodeString: null
    }
  }
}
</script>
