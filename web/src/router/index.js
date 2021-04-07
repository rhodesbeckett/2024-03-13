import Vue from 'vue'
import VueRouter from 'vue-router'
import MatchInfo from '../views/MatchInfo.vue'
import store from '../store'



/* import Vuex from 'vuex'

Vue.use(Vuex) */
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue'),
  },
  {
    path: '/matchCompInfo',
    name: 'matchCompInfo',
    component: MatchInfo,
    
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/editor',
    name: 'Editor',
    beforeEnter(to,from,next) {
      if (from.name == null) {
        store.dispatch('getCompDesc')
      }
      /* else {
        console.log(router.app)
      } */
      next()
    },
    component: () => import(/* webpackChunkName: "about" */ '../views/Editor.vue')
  },
  {
    path: '/testing',
    name: 'Testing',
    component: () => import(/* wepbackChunkName: "about" */ '../views/Testing.vue')
  },
  {
    path: '/cut-and-render',
    name: 'CR',
    component: () => import(/* wepbackChunkName: "about" */ '../views/CutAndRender.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
