<template>
  <h1 class="title" style="grid-area: highlightsTest">Highlights</h1>
  <h2 class="title is-6" style="grid-area: highlightsValue">
    {{ this.testHighlights }}
  </h2>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";
export default defineComponent({
  computed: { ...mapGetters(["testHighlights"]) },
});
</script>

<style></style>
