<template>
  <h1 class="title" style="grid-area: matchTest">Match</h1>
  <h2 class="title is-6" style="grid-area: matchValue">{{ this.testSrc }}</h2>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";

export default defineComponent({
  computed: { ...mapGetters(["testSrc"]) },
});
</script>

<style></style>
