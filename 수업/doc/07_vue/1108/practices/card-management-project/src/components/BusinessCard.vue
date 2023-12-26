<template>
  <div>
    <h3>보유 명함 목록</h3>
    <div v-if="lengthOfBusinessCards">
      <p>현재 보유중인 명함수 : {{ lengthOfBusinessCards }}</p>
      <div class="card-container">
        <BusinessCardDetail 
          v-for="businessCard in businessCards"
          :key="businessCard.name"
          :business-card="businessCard"
          @delete-card-event="deleteCard"
        />
      </div>
    </div>
    <div v-else>
      <p>명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, watch, toRefs } from 'vue'
  import BusinessCardDetail from '@/components/BusinessCardDetail.vue'
  const props = defineProps({
    newCard: Object,
  })

  const businessCards = ref([
    { name: '일론머스크', title: '테슬라 테크노킹'},
    { name: '래리엘리슨', title: '오라클창업주'},
    { name: '빌게이츠', title: 'MS 공동창업주'},
    { name: '래리페이지', title: '구글 공동창업주'},
    { name: '세르게이브린', title: '구글 공동창업주'},
  ])

  const lengthOfBusinessCards = computed(()=>{
    return businessCards.value.length
  })
  
  const deleteCard = function(targetCard) {
    businessCards.value = businessCards.value.filter((item) => item !== targetCard )
  }


  watch(() => props.newCard, (card) => businessCards.value.push(card))

  // const nnewCard = toRefs(props).newCard
  // watch(nnewCard, (card) => businessCards.value.push(card))

</script>

<style  scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;

}
</style>