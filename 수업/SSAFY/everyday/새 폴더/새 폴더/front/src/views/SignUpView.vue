<template>
  <div>
    <h1>회원 가입 페이지</h1>
    <form @submit.prevent="signUp">
      <label>
        username : 
        <input type="text" v-model.trim="username">
      </label><br>
      <label>
        password : 
        <input type="password" v-model.trim="password1">
      </label><br>
      <label>
        password Confirmation: 
        <input type="password" v-model.trim="password2">
      </label><br>
      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useArticleStore } from '@/stores/articles'



const store = useArticleStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)


const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}



</script>

<style scoped>

</style>