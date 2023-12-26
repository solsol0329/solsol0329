<template></template>
  <div>
      <input type="text" @keyup.enter="onKeywordEnter">
  </div>
</template>

<script>
// axios 패키지에서 axios 를 꺼낸다.
// 사용안하면 에러뜹니다.
import axios from 'axios'


const YOUTUBE_API_KEY = 'AIzaSyD1ZG0YHGrQQB-QCqwCxUoCvf16oZNHTOQ'
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'


export default {
    name: 'SearchBar',
    methods:{
        async onKeywordEnter(event) {
            const keyword = event.target.value
            const config = {
                params: {
                    part: 'snippet',
                    type: 'video',
                    q: keyword,
                    key: YOUTUBE_API_KEY,
                },
            }
            //console.log(keyword)

            //axios.get(YOUTUBE_API_URL, config)

            const response = await axios.get(YOUTUBE_API_URL, config)
            //console.log(response)
            const videoList = response.data.items
            // 부모한테 올리기 케밥케이스 비디오리스트를 app.vue methods 에넘긴다.
            this.$emit('on-keyword-enter', videoList)
        },
    },
}
</script>

<style>

</style>