<template>
  <section>
    <editor style="height: 500px"
      theme="github"
      :lang="selectedLanguage.tag"
      v-model="content"
      @init="editorInit">
    </editor>
    
   <b-dropdown v-model="selectedLanguage">
      <button
        slot="trigger"
        class="button is-primary">
        <span>{{ selectedLanguage.name }}</span>
        <b-icon icon="menu-down"/>
      </button>

      <b-dropdown-item
        v-for="lang in languages"
        :value="lang"
        :key="lang.name">
        {{ lang.name }}
      </b-dropdown-item>
    </b-dropdown>
    <button 
      class="button is-primary"
      @click="submit">
      Test
    </button>
  </section>
</template>

<script>
import axios from 'axios'
import { API_URL } from '@/definitions'

let languages = [
  {
    name: 'Python 2',
    tag: 'python'
  },
  {
    name: 'Python 3',
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
  }
]

export default {
  components: {
    editor: require('vue2-ace-editor')
  },
  methods: {
    editorInit () {
      require('brace/ext/language_tools')
      require('brace/theme/github')
      languages.forEach((lang) => require('brace/mode/' + lang.tag))
    },
    async submit () {
      await axios.post(API_URL + '/api/v1/test', {
        code: window.btoa(this.content)
      }, {
        headers: {
          Authorization: `Bearer ${this.$store.state.auth.access_token}`
        }
      })
    }
  },
  data: function () {
    return {
      languages: languages,
      selectedLanguage: languages[0],
      content: ''
    }
  }
}
</script>
