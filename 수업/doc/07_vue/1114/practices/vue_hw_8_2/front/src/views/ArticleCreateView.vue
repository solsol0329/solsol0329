<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="onSubmit">
      <input type="text" v-model="title">
      <textarea v-model="content"></textarea>
      <input type="submit">
  </form>
    
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore} from '@/stores/articles.js'

const store = useArticleStore()
const title = ref('')
const content = ref('')

const onSubmit = function() {
  const payload = {
    title: title.value,
    content: content.value,
  }
  store.createArticle(payload)
  title.value = ''
  content.value = ''

}
</script>

<style lang="scss" scoped>

</style>