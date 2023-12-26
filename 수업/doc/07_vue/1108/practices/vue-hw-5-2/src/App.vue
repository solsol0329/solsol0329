<template>
  <div class="border">
    <ParentPage />
  </div>
</template>

<script setup>
  import ParentPage from '@/components/ParentPage.vue';
</script>

<style >
  .border {
    border: 1px solid black;
    margin: 5px;
  }
</style>