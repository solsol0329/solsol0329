<template>
  <div>
    <!-- <h1>{{ $route.params.youtubeData }}</h1> -->
    <hr>
    <!-- <p>{{ $route.params.publishTime }}</p> -->
    <hr>

    <div id="player">
      <iframe
        :width="1024"
        :height="600"
        :src="`https://www.youtube.com/embed/${$route.params.id}?`"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      />
    </div>

  </div>
</template>

<script>
  // import { useRoute } from 'vue-router'
  // import {ref} from 'vue'

  // const route = useRoute()
  // const params = route.params
  // console.log(route)
  // const id = params.videoId

  // const thumbnail = ref(image.default.url)
  
import { computed, defineComponent, reactive } from "vue";
// import YoutubeIframeLoader from "youtube-iframe";

export default defineComponent({
  setup() {
    const state = reactive({
      videoId: '',
    });

    const onMounted = () => {
    };

    return {
      state,
    };
  },
});
</script>

<style scoped>

</style>

