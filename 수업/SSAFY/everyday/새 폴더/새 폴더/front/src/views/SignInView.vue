<template>
  <div>
    <h1>로그인 페이지</h1>
    <form @submit.prevent="signIn">
      <label>
        username : 
        <input type="text" v-model.trim="username">
      </label><br>
      <label>
        password : 
        <input type="password" v-model.trim="password">
      </label><br>
      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useArticleStore } from '@/stores/articles'


const store = useArticleStore()
const username = ref('')
const password = ref('')


const signIn= function() {
  const payload = {
    username:username.value,
    password:password.value
  }
  store.signIn(payload)
}



</script>

<style scoped>

</style>