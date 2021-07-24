<template>
  <h1 class="title" style="grid-area: testPicture">Test match</h1>
  <div style="grid-area: pictureInput">
    <TestingPictureMin />
    <TestingPictureSec />
  </div>
  <TestingPictureButton />
  <TestingPictureFile />
</template>

<script lang="ts">
import TestingPictureMin from "@/components/TestingPictureMin.vue";
import TestingPictureSec from "@/components/TestingPictureSec.vue";
import TestingPictureButton from "@/components/TestingPictureButton.vue";
import TestingPictureFile from "@/components/TestingPictureFile.vue";

import { defineComponent } from "vue";

export default defineComponent({
  components: {
    TestingPictureMin,
    TestingPictureSec,
    TestingPictureButton,
    TestingPictureFile,
  },
});
</script>

<style></style>
