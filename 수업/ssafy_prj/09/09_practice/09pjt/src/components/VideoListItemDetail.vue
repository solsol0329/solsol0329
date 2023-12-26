<template>
  <div id="app">
    <!-- 자식한테 받을거 -->
    <SearchBar
      @on-keyword-enter="onKeywordEnter"
    />
    <VideoListItemDetail
      :video="video"
    />
    <VideoList 
    :videoList="videoList"
    @on-select-video="onSelectVideo"
    />
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoListItemDetail from '@/components/VideoListItemDetail'


export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoListItemDetail,
  },
  data() {
    return {
      videoList: [],
      video: {},
    }
  },
  methods: {
    onKeywordEnter(videoList) {
      //console.log('부모에서찍음', videoList)
      this.videoList = videoList
      console.log(videoList)
    },
    onSelectVideo(video) {
      this.video = video

    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>