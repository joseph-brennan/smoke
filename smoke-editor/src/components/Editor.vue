<template>
  <div>
    <button :onClick="encode64Click"></button>
    <brace style="height: 500px"
      :fontsize="'12px'"
      :theme="'github'"
      :mode="'python'"
      :codefolding="'markbegin'"
      :softwrap="'free'"
      :selectionstyle="'text'"
      :highlightline="true">
    </brace>
  </div>
</template>

<script>
import Brace from 'vue-bulma-brace'
import Button from '@/components/Button'

export default {
  components: {
    Brace,
    Button 
  }
  methods: {
    encode64Click() {
        console.log('Encoding button clicked')
    }
  }
}
</script>
