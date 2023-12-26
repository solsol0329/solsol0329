import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('main', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
    ])
  return {
    balances,
    getUserByName: (name) => {
      return balances.value.find((user) => user.name === name)
    },
  }
})