<template>
    <newtestform/>
</template>


<script>
import newtestform from '@/components/TestForm'

export default {
  components: {
    newtestform
  },
  meta: {
    auth: {
      roles: ['ADMIN', 'STUDENT', 'TEACHER']
    }
  }
}
</script>
