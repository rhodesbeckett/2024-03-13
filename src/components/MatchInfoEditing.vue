<template>
  <h1 class="title matchInfo__title">Editing</h1>
  <h2 class="matchInfo__editing-response" v-if="isChosen == true">
    {{ editing }}
  </h2>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";

export default defineComponent({
  computed: { ...mapGetters(["isChosen", "editing"]) },
});
</script>

<style></style>
