<template>
  <section>
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

    <brace
      :fontsize="'12px'"
      :theme="'github'"
      :mode="selectedLanguage.tag"
      :codefolding="'markbegin'"
      :softwrap="'free'"
      :selectionstyle="'text'"
      :highlightline="true"
      style="height: 500px"/>
  </section>
</template>

<script>
import Brace from 'vue-bulma-brace'

export default {
  components: {
    Brace
  },
  data: function () {
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
    return {
      languages: languages,
      selectedLanguage: languages[0]
    }
  }
}
</script>
