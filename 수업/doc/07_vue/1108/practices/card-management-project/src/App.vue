<template>
  <div class="app">
    <header class="header">
      <h1>명함 관리 페이지</h1>
    </header>
    <main class="main">
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </main>
    <article class="article">
      <CreateCardForm
        @create-card-event="updateCard"
      />
      <BusinessCard 
        :newCard="newCard"
      />
    </article>
    <footer class="footer">
      <p>&copy; 2023 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>
  import BusinessCard from '@/components/BusinessCard.vue';
  import CreateCardForm from '@/components/CreateCardForm.vue';
  import { ref } from 'vue'

  const newCard = ref({})
  const updateCard = function(cardInfo) {
    newCard.value = cardInfo
  }
</script>

<style scoped>
  .app {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    text-align: center;
  }
  .header {
    background-color: blue;
    color: white;
    padding: 20px;
  }
  .main{

    padding: 20px;

  }
  .article {
    padding: 20px;
    flex-grow: 1;
  }

  .footer {
    background-color: lightgrey;
    width: 100%;
  }
</style>