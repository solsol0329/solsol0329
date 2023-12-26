<template>
  <div>
    <h2>부모 컴포넌트</h2>
    {{ family.father }}
    {{ family.mother }}
    <ChildPage 
      v-for="child in family.children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';

defineProps({
  family: Object,
})
</script>

<style lang="scss" scoped>

</style>