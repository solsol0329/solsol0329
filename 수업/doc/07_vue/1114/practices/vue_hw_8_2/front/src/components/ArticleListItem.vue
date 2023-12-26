<template>
  <div>
    <p>{{ article.id }}번째 게시글</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  article: Object,
})
</script>

<style lang="scss" scoped>

</style>