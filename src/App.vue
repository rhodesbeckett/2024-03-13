<template>
  <section class="section">
    <div class="container">
      <HeaderNav />
      <router-view v-slot="{ Component }">
        <transition name="zoom" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import HeaderNav from "./components/HeaderNav.vue";
export default defineComponent({
  components: { HeaderNav },
});
</script>

<style>
@import "./assets/bulma.min.css";
@import "./assets/main.css";

.visible-hamburger {
  display: initial;
}

.zoom-enter-active,
.zoom-leave-active {
  animation-duration: 0.3s;
  animation-fill-mode: both;
  animation-name: zoom;
}

.zoom-leave-active {
  animation-direction: reverse;
}

.navbar-yes {
  transition: all 0.5s;
}

@media (max-width: 1023px) {
  .navbar-not-visible {
    opacity: 0;
    transition: all 0.5s;
  }

  .navbar-visible {
    opacity: 1;
    width: 100%;
    background: white;
    transition: all 0.5s;
  }
}

@keyframes zoom {
  from {
    opacity: 0;
    transform: scale3d(0.4, 0.4, 0.4);
  }
  100% {
    opacity: 1;
  }
}
</style>
