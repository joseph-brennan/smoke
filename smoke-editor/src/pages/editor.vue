<template>
  <section class="section">
    <editor/>
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
