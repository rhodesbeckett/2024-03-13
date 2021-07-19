<template>
  <label>
    {{ formated }}
    <input
      type="radio"
      class="title"
      name="halfTime"
      :value="formated"
      @click="radioClick(halfTime, matchCompID)"
    />
  </label>
</template>

<script lang="ts">
export default {
  props: ["radioClick", "halfTime", "matchCompID"],
  computed: {
    formated(): string {
      if (this.halfTime === 1) {
        return this.halfTime + "st";
      } else if (this.halfTime === 2) {
        return this.halfTime + "nd";
      }
      return "";
    },
  },
};
</script>

<style></style>
