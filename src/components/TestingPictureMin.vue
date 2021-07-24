<template>
  <input
    type="number"
    size="3"
    maxlength="3"
    class="user-input"
    v-bind:value="pictureMin"
    v-on:input="UPDATE_PICTURE_MIN($event.target.value)"
  />
  <span class="testing-space">:</span>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters, mapMutations } from "vuex";

export default defineComponent({
  computed: { ...mapGetters(["pictureMin"]) },
  methods: { ...mapMutations(["UPDATE_PICTURE_MIN"]) },
});
</script>

<style></style>
