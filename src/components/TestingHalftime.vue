<template>
  <h1 class="title" style="grid-area: halfTimeTest">Halftime</h1>
  <h2 class="title is-6" style="grid-area: halfTimeValue">
    {{ this.testHalftime }}
  </h2>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";
export default defineComponent({
  computed: { ...mapGetters(["testHalftime"]) },
});
</script>

<style></style>
