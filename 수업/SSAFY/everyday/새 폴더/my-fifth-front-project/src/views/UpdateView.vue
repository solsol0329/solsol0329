<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ balanceInfo.name }}</p>
    <p >잔고 : {{ balanceInfo.balance }}</p>
    <button @click="addBalance">+</button>
  </div>
</template>

<script setup>
import {useRouter} from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const router = useRouter()
const balanceStore = useBalanceStore()
const balanceInfo = balanceStore.getUserByName(router.currentRoute.value.params.name)


const addBalance = function() {
  balanceInfo.balance+=1000
}



</script>


<style scoped>

</style>