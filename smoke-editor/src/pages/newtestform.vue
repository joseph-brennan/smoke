<template>
  <section class="container">
    <h3 v-if="error !== ''">{{ geterror() }}</h3>
    <div class="box">
    <h1 class="title is-primary">New Test Form</h1>
    <div class="form-group">
      <b-field label="Test Name*">
        <b-input v-model="test.name" type="text"/>
      </b-field>
      <b-field label="Statements*"/>
        <b-input v-model="test.statements" type="textarea"/>
      </b-field>
      <b-field label="Input Description*">
        <b-input v-model="test.input_desc" type="textarea"/>
      </b-field>
      <b-field label="Output Description*">
        <b-input v-model="test.output_desc" type="textarea"/>
      </b-field>
      <b-field label="Constraints*">
        <b-input v-model="test.constraints" type="textarea"/>
      </b-field>
      <button
        id="submit"
        class="button"
        is-primary
        @click="submit">
        Submit
      </button>
    </div>
  </div>
</section>
</template>

<script>
export default {
  data () {
    return {
      test: {
        name: '',
        statements: '',
        input_des: '',
        output_desc: '',
        constraints: ''
      },
      error: ''
    }
  },
  meta: {
    auth: {
      roles: ['ADMIN', 'STUDENT', 'TEACHER']
    }
  }
}
</script>
