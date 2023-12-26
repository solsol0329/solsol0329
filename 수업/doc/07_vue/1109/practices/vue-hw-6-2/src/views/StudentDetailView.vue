<template>
  <div>
    <h1>학생 상세 정보 페이지 입니다.</h1>
    <p>이름: {{ $route.params.name }}</p>
    <p>이름: {{ name }}</p>
  </div>
</template>

<script setup>
  import { useRoute } from 'vue-router'

  const route = useRoute()
  const name = route.params.name
</script>

<style lang="scss" scoped>

</style>