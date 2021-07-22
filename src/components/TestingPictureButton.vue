<template>
  <a
    class="button is-success checkBtn"
    @click="getTestingPictureSrc"
    style="grid-area: checkBtn"
    >Check
  </a>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions } from "vuex";
export default defineComponent({
  methods: { ...mapActions(["getTestingPictureSrc"]) },
});
</script>

<style></style>
