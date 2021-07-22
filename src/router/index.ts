import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import store from "@/store/index";
import { RouteLocationNormalized, NavigationGuardNext } from "vue-router";
import { COOKIE } from "@/plugins/cookie";
import { NEXT_PAGE } from "@/plugins/routerGuard";
const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
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
    path: "/matchInfo",
    name: "matchInfo",
    component: () =>
      import(/* webpackChunkName: "Editor" */ "@/views/MatchInfo.vue"),
    beforeEnter: (
      to: RouteLocationNormalized,
      from: RouteLocationNormalized,
      next: NavigationGuardNext
    ) => {
      NEXT_PAGE(next);
    },
  },
  {
    path: "/editor",
    name: "Editor",
    component: () =>
      import(/* webpackChunkName: "Editor" */ "@/views/Editor.vue"),
    beforeEnter: (
      to: RouteLocationNormalized,
      from: RouteLocationNormalized,
      next: NavigationGuardNext
    ) => {
      NEXT_PAGE(next);
    },
  },
  {
    path: "/testing",
    name: "Testing",
    component: () =>
      import(/* wepbackChunkName: "Testing" */ "@/views/Testing.vue"),
    beforeEnter: (
      to: RouteLocationNormalized,
      from: RouteLocationNormalized,
      next: NavigationGuardNext
    ) => {
      NEXT_PAGE(next);
    },
  },
  {
    path: "/cut-and-render",
    name: "CR",
    component: () =>
      import(/* wepbackChunkName: "CutAndRender" */ "@/views/CutAndRender.vue"),

    beforeEnter: (
      to: RouteLocationNormalized,
      from: RouteLocationNormalized,
      next: NavigationGuardNext
    ) => {
      NEXT_PAGE(next);
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
