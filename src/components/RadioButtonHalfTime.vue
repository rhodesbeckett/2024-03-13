<template>
  <label>
    {{ formated }}
    <input
      type="radio"
      class="title"
      name="halftime"
      :value="formated"
      @click="radioClick(halftime, matchCompID)"
    />
  </label>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import useCompHelpers from "@/composables/useCompHelpers";

export default defineComponent({
  props: { halftime: Number, matchCompID: String },
  setup() {
    const { radioClick, setMatchID } = useCompHelpers();
    return { radioClick, setMatchID };
  },
  computed: {
    formated(): string {
      if (this.halftime == 1) {
        return this.halftime + "st";
      } else if (this.halftime == 2) {
        return this.halftime + "nd";
      } else {
        return "";
      }
    },
  },
});
</script>

<style scoped></style>
