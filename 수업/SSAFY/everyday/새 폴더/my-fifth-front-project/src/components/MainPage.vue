<template>
  <div>
    <p>이름 : {{ balanceInfo.name }}</p>
    <p>잔고 : {{ balanceInfo.balance }}</p>
    <button @click="goUpdate(balanceInfo)">updateBalance</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

defineProps({
  balanceInfo : Object,
})


const router = useRouter()

const goUpdate = function(balanceInfo) {[
  router.push({
    name:'update',
    params: {
      balance: balanceInfo.balance,
      name: balanceInfo.name,
    },
  })
]}



</script>

<style scoped>

</style>