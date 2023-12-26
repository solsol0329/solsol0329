<template>
  <div>
    <h1>비디오 검색</h1>
    <form class="d-flex" @submit.prevent="searchWords">
      <input v-model="words" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">찾기</button>
    </form>

    
    <div 
      v-for="video in youtubeData" :key="video.id.videoId" class="card" style="width: 18rem;"
      @click="goDetail(video.id.videoId)"
      >
      <img :src="getThumbnail(video.snippet.thumbnails)" alt="Video Thumbnail">
      <div class="card-body">
        <p class="card-text">{{ video.snippet.title }}</p>
      </div>
    </div>


  </div>
</template>

<script setup>

import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const words = ref('')
const YOUTUBE_API_KEY = 'AIzaSyD1ZG0YHGrQQB-QCqwCxUoCvf16oZNHTOQ' // 본인의 YouTube API 키로 교체
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

const youtubeData = ref([])

const searchWords = function () {
  const config = {
    params: {
      part: 'snippet',
      type: 'video',
      q: words.value,
      key: YOUTUBE_API_KEY,
    },
  }

  axios.get(YOUTUBE_API_URL, config)
    .then((res) => youtubeData.value = res.data.items)
    .catch((err) => console.log(err))
}

const getThumbnail = function (thumbnails) {
  // 여기에서 원하는 썸네일 크기를 선택
  return thumbnails.default.url
}

const router = useRouter()

const goDetail = function(id) {
  router.push({
    name:'videoDetail',
    params:{
      id:id,
      // title: video.title,
      // publishTime:video.publishTime,
      // description:video.description
    },
  })
}

</script>

<style scoped>



</style>