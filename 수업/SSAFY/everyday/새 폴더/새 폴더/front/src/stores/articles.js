import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import {useRouter} from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const router = useRouter()
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if( token.value === null ) {
      return false
    } else {
      return true
    }
  })
  
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
    .catch(err => console.log(err))
  }
  
  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/articles/`,
      data: {
        title,
        content,
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => router.push({name:'home'}))
  }




  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method:'post',
      url:`${API_URL}/accounts/signup/`,
      data:{
        username, password1, password2,
      }
    })
      .then((res) => {
        console.log(res)
        console.log('가입 완료')
        const password = password1
        signIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const signIn = function(payload) {
    const {username, password} = payload
    axios({
      method:'post',
      url:`${API_URL}/accounts/login/`,
      data: {
        username, password,
      }
    })
      .then((res) => {
        console.log('로그인 완료')
        token.value = res.data.key
        router.push({name: 'home'})
      })
      .catch((err) => {
        console.log(err)
      })
  }



  return { token, articles, getArticles, createArticle, signUp, API_URL, signIn, isLogin }
}, {persist: true})
