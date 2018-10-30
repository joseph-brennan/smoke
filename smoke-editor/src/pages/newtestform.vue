<template>
  <section class="container">
    <h1 class="title is-primary">New Test Form</h1>
    <div class="form-group">
      <div class="box">
        <label class="label">Test Name*</label>
        <input class="input" type="text" placeholder="User's First Test"/>
      </div>
      <div class="box">
        <label class="label">Statements*</label>
        <textarea class="textarea" rows="5" cols="80"></textarea>
      </div>
      <div class="box">
        <label class="label">Tags (max 5 tags)</label>
        <textarea class="textarea" rows="5" cols="80"></textarea>
      </div>
      <div class="box">
        <label class="label">Difficulty</label>
        <div class="select">
          <select>
            <option>Select Difficulty</option>
            <option>Easy</option>
            <option>Medium</option>
            <option>Hard</option>
            <option>Luke-sanity</option>
          </select>
        </div>
      </div>
      <div class="box">
        <label class="label">Input Description*</label>
        <textarea class="textarea" rows="7" cols="80"></textarea>
      </div>
      <div class="box">
        <label class="label">Output Description*</label>
        <textarea class="textarea" rows="7" cols="80"></textarea>
      </div>
      <div class="box">
        <label class="label">Input Description*</label>
        <textarea class="textarea" rows="7" cols="80"></textarea>
      </div>
      <div class="box">
        <label class="label">Constraints*</label>
        <textarea class="textarea" rows="7" cols="80"></textarea>
      </div>
      <div class="box">
        <label class="label">Test Cases*</label>
        <label class="label">Test 1</label>
        <div class="columns">
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Input"></textarea>
          </div>
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Output"></textarea>
          </div>
        </div>
        <label class="label">Validator 1</label>
        <div class="columns">
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Input"></textarea>
          </div>
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Output"></textarea>
          </div>
        </div>
      </div>
      <div class="box">
        <label class="label">Test Cases*</label>
        <label class="label">Test 2</label>
        <div class="columns">
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Input"></textarea>
          </div>
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Output"></textarea>
          </div>
        </div>
        <label class="label">Validator 2</label>
        <div class="columns">
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Input"></textarea>
          </div>
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Output"></textarea>
          </div>
        </div>
      </div>
      <div class="box">
        <label class="label">Test Cases*</label>
        <label class="label">Test 3</label>
        <div class="columns">
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Input"></textarea>
          </div>
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Output"></textarea>
          </div>
        </div>
        <label class="label">Validator 3</label>
        <div class="columns">
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Input"></textarea>
          </div>
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Output"></textarea>
          </div>
        </div>
      </div>
      <div class="box">
        <label class="label">Test Cases*</label>
        <label class="label">Test 4</label>
        <div class="columns">
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Input"></textarea>
          </div>
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Output"></textarea>
          </div>
        </div>
        <label class="label">Validator 4</label>
        <div class="columns">
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Input"></textarea>
          </div>
          <div class="column">
            <textarea class="textarea" rows="5" placeholder="Output"></textarea>
          </div>
        </div>
        <div>
          <editor/>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import editor from '@/components/Editor'

export default {
  components: {
    editor
  },
  meta: {
    auth: {
      roles: ['ADMIN', 'STUDENT', 'TEACHER']
    }
  }
}
</script>
