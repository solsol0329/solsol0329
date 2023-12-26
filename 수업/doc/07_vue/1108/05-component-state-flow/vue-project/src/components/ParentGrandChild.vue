<template>
  <div>
    <p>ParentGrandChild</p>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="updataName">이름 변경</button>
  </div>
</template>

<script setup>
defineProps({
  myMsg: String,
  dynamicProps: String,
})

const emit = defineEmits(['updataName'])
const updataName = function() {
  // emit 상위로 보내야 한다.
  emit('updataName')   
}
</script>

<style lang="scss" scoped>

</style>