<template>
  <h1 class="title matchInfo__title">Match:</h1>
  <input
    type="text"
    :value="src"
    @input="this.updateSrc"
    placeholder="full path"
    class="input matchInfo__input--half"
  />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters, mapMutations } from "vuex";
import { EventEditor } from "@/composables/EventEditor";
export default defineComponent({
  methods: {
    ...mapMutations(["UPDATE_SRC"]),
    updateSrc(event: EventEditor) {
      this.UPDATE_SRC(event.target.value);
    },
  },
  computed: mapGetters(["src"]),
});
</script>

<style></style>
