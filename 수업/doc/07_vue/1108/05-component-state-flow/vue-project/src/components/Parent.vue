<template>
  <div>
    Parent
    <ParentChild 
      my-msg="안녕"
      :dynamic-props="name"
      @some-event="someCallback"
      @emit-args="getNumbers"
      @updata-name="updataName"
    />
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue';
import { ref } from 'vue'

const name = ref('Alice')
const someCallback = function(){
  console.log('ParentChild가 발신한 이벤트를 수신1')
}
const getNumbers = function(...args) {
  console.log(args)
}

const updataName = function() {
  name.value = '김한욱'
}
</script>

<style lang="scss" scoped>

</style>