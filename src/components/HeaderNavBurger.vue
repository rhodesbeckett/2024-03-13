<template>
  <a
    role="button"
    class="navbar-burger"
    @click="toggleHamburger"
    aria-label="menu"
    aria-expanded="false"
    data-target="navbarBasicExample"
  >
    <span aria-hidden="true"></span>
    <span aria-hidden="true"></span>
    <span aria-hidden="true"></span>
  </a>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {};
  },
  methods: {
    toggleHamburger(): void {
      let navbarMenu = document.querySelector(".navbar-menu");
      if (navbarMenu) {
        navbarMenu.classList.toggle("visible-hamburger");
      }
      let navbarEnd = document.querySelector(".navbar-end");
      setTimeout(function () {
        if (navbarEnd) {
          navbarEnd.classList.toggle("navbar-not-visible");
          navbarEnd.classList.toggle("navbar-visible");
        }
      }, 200);
    },
  },
});
</script>
