<template>
  <div>
    <h1 class="singer-list">가수 목록</h1>
    <SingerDetail 
      v-for="singer in singers"
      :key="singer.name"
    />

  </div>
</template>

<script setup>
  import SingerDetail from '@/components/singers/SingerDetail.vue'
  import {ref} from 'vue'
  const singers = ref([
    {name: 'adele'},
    {name: 'b'},
    {name: 'c'},
  ])
</script>

<style  scoped>
  card {
    display: inline-block;
    width: 40%;
    margin: 20px;
  }
  h1 {
    color: orangered
  }
  .singer-list{
    text-align: center;
  }
</style>