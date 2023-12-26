<template>
  <div>
    <h1>학생 상세 정보 목록입니다.</h1>
    <div v-for="student in studentInfo" :key="student.name">
      <p >{{ student.name }}</p>
    </div>  
  </div>
</template>



<script setup>
import {ref} from 'vue'


const studentInfo = ref([
  {name: '김하나'},
  {name: '김두리'},
  {name: '김서이'},
])



</script>


<style scoped>

</style>