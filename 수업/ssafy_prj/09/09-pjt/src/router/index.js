import { createRouter, createWebHistory } from 'vue-router'
import SearchView from '@/views/SearchView.vue'
import HomeView from '@/views/HomeView.vue'
import VideoDetailView from '@/views/VideoDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/search/:id',
      name: 'videoDetail',
      component: VideoDetailView
    },
   
  ]
})

export default router
