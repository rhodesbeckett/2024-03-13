<template>
  <nav
    class="navbar navbar--routing"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <HeaderNavBrand />
      <HeaderNavBurger />
    </div>

    <div class="navbar-menu" ref="navbarMenu">
      <div class="navbar-start">
        <!-- navbar items -->
      </div>

      <div class="navbar-end navbar-yes navbar-not-visible" ref="navbarEnd">
        <HeaderNavItem
          v-for="item in items"
          :key="item.url"
          :url="item.url"
          :iconClass="item.iconClass"
          :text="item.text"
        />
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import HeaderNavBrand from "@/components/HeaderNavBrand.vue";
import HeaderNavBurger from "@/components/HeaderNavBurger.vue";
import HeaderNavItem from "@/components/HeaderNavItem.vue";

export default defineComponent({
  components: { HeaderNavBrand, HeaderNavBurger, HeaderNavItem },
  data() {
    return {
      items: [
        {
          url: "/matchInfo",
          iconClass: "fas fa-info-circle",
          text: "Match information",
        },
        {
          url: "/editor",
          iconClass: "fas fa-chalkboard-teacher",
          text: "Highlights",
        },
        { url: "/testing", iconClass: "fas fa-border-style", text: "Testing" },
        {
          url: "/cut-and-render",
          iconClass: "fas fa-video",
          text: "Cut and render",
        },
      ],
    };
  },
});
</script>
