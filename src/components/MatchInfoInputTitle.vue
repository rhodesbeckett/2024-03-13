<template>
  <h1 class="title matchInfo__title">Title:</h1>
  <input
    type="text"
    :value="title"
    @input="this.changeTitle"
    class="input matchInfo__input"
  />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters, mapMutations } from "vuex";
import { EventEditor } from "@/composables/EventEditor";
export default defineComponent({
  methods: {
    ...mapMutations(["UPDATE_TITLE"]),
    changeTitle(event: EventEditor) {
      this.UPDATE_TITLE(event.target.value);
    },
  },
  computed: { ...mapGetters(["title"]) },
});
</script>

<style>
.matchInfo__input {
  grid-column: title-end / input-end;
}
</style>
