<template>
  <div class="columns is-centered is-multiline final-container">
    <CutAndRenderCutButton/>
    <CutAndRenderCutProgress/>
    <CutAndRenderRenderButton/>
    <CutAndRenderRenderProgress/>
  </div>
</template>

<script lang="ts">
import CutAndRenderCutButton from "@/components/CutAndRenderCutButton.vue";
import CutAndRenderCutProgress from "@/components/CutAndRenderCutProgress.vue";
import CutAndRenderRenderButton from "@/components/CutAndRenderRenderButton.vue";
import CutAndRenderRenderProgress from "@/components/CutAndRenderRenderProgress.vue";
import { defineComponent } from "vue";
import { mapActions } from "vuex";

export default defineComponent({
  components: {
    CutAndRenderCutButton,
    CutAndRenderCutProgress,
    CutAndRenderRenderButton,
    CutAndRenderRenderProgress,
  },
  methods: { ...mapActions(["getCanCut","getCanRender"]) },
  created() {
    this.getCanCut();
    this.getCanRender();
  },
});
</script>

<style>
.final-container {
  max-width: 1080px;
  margin: 0 auto;
}
.cut-button {
  grid-column: 1 / 2;
}
.progress-bar {
  grid-column: 1 / 7;
  display: flex;
  background-color: gray;
  border: 2px solid black;
  border-top: 0px solid transparent;
  width: 100%;
  margin: 0.5em 0;
}
.cut-progress {
  transition: all 0.5s;
}
progress[value]::-moz-progress-bar {
  transition: value 0.5s;
}
</style>
