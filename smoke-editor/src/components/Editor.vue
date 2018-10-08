<template>
  <div class = "editor">
    <b-dropdown v-model="selectedLanguage">
      <button slot="trigger" class="button is-primary">
        <span>{{ selectedLanguage.name }}</span>
        <b-icon icon="arrow-down"/>
      </button>

      <b-dropdown-item v-for="lang in languages"
                       v-bind:data="lang"
                       v-bind:key="lang.name"
                       v-bind:value="lang.value">
                       {{ lang.name }}
      </b-dropdown-item>
    </b-dropdown>
  </div>
</template>



<script>
import Brace from 'vue-bulma-brace'
import Vue from 'vue'
import Buefy from 'buefy'
// import 'buefy/lib/buefy.css'

Vue.use(Buefy)

export default{
  components: {
    Brace
  },
  data: function () {
      let languages: [
        {
          name: 'Python 3',
          tag: 'python'
        },
        {
          name: 'Python 2',
          tag: 'python'
        },
        {
          name: 'Ruby',
          tag: 'ruby'
        },
        {
          name: 'Java',
          tag: 'java'
        },
        {
          name: 'JavaScript',
          tag: 'javascript'
        },
        {
          name: 'C++',
          tag: 'cpp'
        },
        {
          name: 'Erlang',
          tag: 'erlang'
        }
      ]
    return {
      languages: languages
      selectedLanguage: languages[0]
    }
  }
}
</script>
