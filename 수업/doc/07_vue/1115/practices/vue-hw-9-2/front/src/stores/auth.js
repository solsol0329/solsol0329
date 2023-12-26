import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()
  const token = ref('')
  const isAuthenticated = ref(false)
  const signUp = function (username, password1, password2) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username,
        password1,
        password2
      }
    })
    .then(res => {
        token.value = res.data.key
        isAuthenticated.value = true
        router.push({name: 'home'})
      })
  }

  const logIn = function (username, password) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username,
        password
      }
    })
    .then(res => {
      token.value = res.data.key
      isAuthenticated.value = true
      router.push({name: 'home'})
    })
  }

  return { signUp, logIn, token, isAuthenticated }
}, { persist: true }
)
