<template>
  <div class="navbar-item">
    <router-link :to="url" class="button">
      <span class="icon">
        <i :class="iconClass" aria-hidden="true"></i>
      </span>
      <span>{{ text }}</span>
    </router-link>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: { url: String, iconClass: String, text: String },
});
</script>

<style></style>
