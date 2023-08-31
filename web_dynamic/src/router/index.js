import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchResultView from '../views/SearchResultView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/search/:ingredient',
      name: 'search',
      component: SearchResultView,
      props: true
    },
    {
      path: '/saved_recipes',
      name: 'favourites',
      component: () => import('../views/FavouritesView.vue'),
      props: true
    }
  ]
})

export default router
