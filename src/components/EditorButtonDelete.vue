<template>
  <div class="column is-1 is-2-mobile">
    <a
      class="button is-danger is-large is-2"
      @click="
        DELETE_ROW(ID);
        setHighlights();
      "
      >Delete</a
    >
  </div>
  >
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions, mapMutations } from "vuex";
export default defineComponent({
  props: { ID: String},
  methods: {
    ...mapMutations(["DELETE_ROW"]),
    ...mapActions(["setHighlights"]),
  },
});
</script>

<style></style>
