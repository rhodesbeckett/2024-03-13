<template>
  <img style="grid-area: picture" :src="pictureSrc()" />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";
export default defineComponent({
  methods: { ...mapGetters(["pictureSrc"]) },
});
</script>

<style></style>
