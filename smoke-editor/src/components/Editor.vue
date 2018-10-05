<template>
  <div class = "editor">
    <b-dropdown v-model="mode">
      <button class="button is-primary" type="button" slot="trigger">
        <template v-if="'Python 3'">
          <span>Python 3</span>
        </template>
        <template v-else-if="'Python 2'">
          <span>Python 2</span>
        </template>
      </button>

      <b-dropdown-item :value="'Python 3'">
        <div class="dropdown-content" @click="changeMode('Python 3')">
          <div class="dropdown-item">
            <h3>Python 3</h3>
          </div>
        </div>
      </b-dropdown-item>

      <b-dropdown-item :value="'Python 2'">
        <div class="dropdown-content" @click="changeMode('Python 2')">
          <div class="dropdown-item">
            <h3>Python 2</h3>
          </div>
        </div>
      </b-dropdown-item>
    </b-dropdown>

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
