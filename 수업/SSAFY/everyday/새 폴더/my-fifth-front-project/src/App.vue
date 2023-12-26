<template>
  <div>
    <h1>pina + router 연습하기</h1>
    <nav>
      <RouterLink :to="{name:'main'}">main</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>

</script>

<style scoped>

</style>