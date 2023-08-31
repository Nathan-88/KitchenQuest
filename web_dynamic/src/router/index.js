// Import the necessary functions from the Vue Router library
import { createRouter, createWebHistory } from 'vue-router'
// Import your component views
import HomeView from '../views/HomeView.vue'
import SearchResultView from '../views/SearchResultView.vue'
import RecipePage from '../views/RecipePage.vue'

// Create a router instance using the createRouter function
const router = createRouter({
  // Specify the history mode and base URL for the router
  history: createWebHistory(import.meta.env.BASE_URL),
  // Define the routes for your application
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/Recipepage',
      name: 'RecipePage',
      component: RecipePage
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
