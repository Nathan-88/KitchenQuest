// Import the necessary functions from the Vue Router library
import { createRouter, createWebHistory } from 'vue-router'
// Import your component views
import HomeView from '@/views/HomeView.vue'
import SearchResultView from '@/views/SearchResultView.vue'
import RecipePageView from '@/views/RecipePageView.vue'
import ErrorView from '@/views/ErrorView.vue'
import { useRecipeStore } from '@/stores'

// Create a router instance using the createRouter function
const router = createRouter({
  // Specify the history mode and base URL for the router
  history: createWebHistory(import.meta.env.BASE_URL),
  // Define the routes for your application
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { transition: '' }
    },
    {
      path: '/recipe_page',
      name: 'RecipePage',
      component: RecipePageView,
      meta: { transition: '' }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/views/AboutView.vue'),
      meta: { transition: '' }
    },
    {
      path: '/search/:recipe',
      name: 'search',
      component: SearchResultView,
      props: true,
      meta: { transition: '' }
    },
    {
      path: '/search/error',
      name: 'error',
      component: ErrorView,
      meta: { transition: '' }
    },
    {
      path: '/saved_recipes',
      name: 'favourites',
      component: () => import('@/views/ComingSoon.vue'),
      props: true,
      meta: { transition: '' }
    }
  ]
})

router.afterEach((to, from) => {
  const toDepth = to.path.length
  const fromDepth = from.path.length
  if (to.path === from.path) to.meta.transition = ''
  else to.meta.transition = toDepth < fromDepth ? 'slide-right' : 'slide-left'
})

export default router
