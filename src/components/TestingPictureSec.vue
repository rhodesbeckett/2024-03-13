<template>
  <input
    type="number"
    size="3"
    maxlength="3"
    class="user-input"
    v-bind:value="pictureSec"
    v-on:input="UPDATE_PICTURE_SEC($event.target.value)"
  />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters, mapMutations } from "vuex";

export default defineComponent({
  computed: { ...mapGetters(["pictureSec"]) },
  methods: { ...mapMutations(["UPDATE_PICTURE_SEC"]) },
});
</script>

<style></style>
