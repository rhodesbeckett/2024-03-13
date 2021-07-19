import {
  RouteLocationNormalized,
  NavigationGuardNext,
  createRouter,
  createWebHistory,
} from "vue-router";
import store from "../store";
const routes = [
  {
    path: "/",
    name: "Home",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Home.vue"),
  },
  {
    path: "/matchCompInfo",
    name: "matchCompInfo",
    component: import(
      /* webpackChunkName: "matchInfo" */ "../views/MatchInfo.vue"
    ),
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/editor",
    name: "Editor",
    beforeEnter(
      to: RouteLocationNormalized,
      from: RouteLocationNormalized,
      next: NavigationGuardNext
    ) {
      if (from.name == null) {
        // eslint-disable-next-line
        store.dispatch("getCompDesc");
      }
      /* else {
        console.log(router.app)
      } */
      next();
    },
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Editor.vue"),
  },
  {
    path: "/testing",
    name: "Testing",
    component: () =>
      import(/* wepbackChunkName: "about" */ "../views/Testing.vue"),
  },
  {
    path: "/cut-and-render",
    name: "CR",
    component: () =>
      import(/* wepbackChunkName: "about" */ "../views/CutAndRender.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
