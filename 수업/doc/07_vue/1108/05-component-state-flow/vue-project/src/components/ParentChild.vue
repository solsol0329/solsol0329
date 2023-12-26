<template>
  <div>
    <p>ParentChild</p>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="emitArgs">클릭</button>
    <ParentGrandChild 
      :my-msg="myMsg"
      :dynamic-props="dynamicProps"
      @updata-name="updataName"
    />
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

// props
const props = defineProps({
  myMsg: String,
  dynamicProps: String,
})
console.log(props)
console.log(props.myMsg)

// emit
const emit = defineEmits(['someEvent', 'emitArgs', 'updataName'])

const emitArgs = function(){
  emit('emitArgs', 1, 2, 3)
}

const updataName = function() {
  emit('updataName')
}
</script>

<style lang="scss" scoped>

</style>