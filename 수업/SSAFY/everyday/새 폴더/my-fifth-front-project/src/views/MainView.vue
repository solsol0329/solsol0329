<template>
  <div>
    <h2>메인 페이지</h2>
    <div>
      <MainPage 
        v-for="balanceInfo in balanceStore.balances"
        :key="balanceInfo.id"
        :balanceInfo="balanceInfo"
      />
      <hr>
    </div>

  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance'
import MainPage from '@/components/MainPage.vue'

const balanceStore = useBalanceStore()


</script>

<style scoped>

</style>