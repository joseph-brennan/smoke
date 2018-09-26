<template>
  <div id="Home" class="col-sm-6 col-sm-offset-3">
    <h1 v-if="vm.response.access_token == 'Admin'">Welcome, Administrator!</h1>
    <h1 v-else>401: Not Authorized</h1>
  </div>
</template>