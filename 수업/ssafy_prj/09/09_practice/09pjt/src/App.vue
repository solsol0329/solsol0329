<template>
  <div id="app">
    <!-- 자식한테 받을거 -->
    <header>
    <SearchBar
      @on-keyword-enter="onKeywordEnter"
    />
    </header>
    <section>
      <VideoListItemDetail
        :video="video"
      />
      <VideoList 
        :videoList="videoList"
        @on-select-video="onSelectVideo"
      />
    </section>

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
section, header {
  width: 80%;
  margin: 0 auto;
  padding: 1rem 0;
}
section {
  display: flex;
}
</style>