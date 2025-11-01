import { createRouter, createWebHistory } from 'vue-router'
import Categories from '@/components/Category.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
     { path: '/', component: Categories },

  ],
})

export default router
