<template>
  <div class="columns is-centered is-multiline message-container">
    <div class="column is-12 testing-container">
      <TestingServerMessage />
      <TestingSrc />
      <TestingHalftime />
      <TestingHighlights />
      <TestingPicture />
    </div>
  </div>
</template>

<script lang="ts">
import TestingHalftime from "@/components/TestingHalftime.vue";
import TestingHighlights from "@/components/TestingHighlights.vue";
import TestingPicture from "@/components/TestingPicture.vue";
import TestingServerMessage from "@/components/TestingServerMessage.vue";
import TestingSrc from "@/components/TestingSrc.vue";
import { defineComponent } from "vue";
export default defineComponent({
  components: {
    TestingServerMessage,
    TestingSrc,
    TestingHalftime,
    TestingHighlights,
    TestingPicture,
  },
});
</script>

<style>
.testing-container {
  display: grid;
  grid-template-columns: 5fr 5fr auto;
  grid-template-rows: auto;
  grid-template-areas:
    "matchTest matchValue picture"
    "halfTimeTest halfTimeValue picture"
    "highlightsTest highlightsValue picture"
    "testPicture testPicture picture"
    "pictureInput pictureInput picture"
    "checkBtn blankSpace picture";
  justify-content: center;
  max-width: 1080px;
  margin: 0 auto;
}
@media (max-width: 860px) {
  .testing-container {
    grid-template-columns: 1fr 2fr auto;
    grid-template-areas:
      "matchTest matchTest matchTest"
      "matchValue matchValue matchValue"
      "halfTimeTest halfTimeTest halfTimeTest"
      "halfTimeValue halfTimeValue halfTimeValue"
      "highlightsTest highlightsTest highlightsTest"
      "highlightsValue highlightsValue highlightsValue"
      "testPicture testPicture testPicture"
      "pictureInput pictureInput pictureInput"
      "checkBtn blankSpace blankSpace"
      "picture picture picture";
  }
  .checkBtn {
    margin-bottom: 0.5em;
  }
  .testing-container > h2 {
    text-decoration: underline;
  }
}
.testing-container__title {
  font-size: 1.2em;
}

.checkBtn {
  margin-top: 1.15em;
}
@media (max-width: 1024px) {
  .testing-container > h1 {
    font-size: 1.2em;
  }
  .testing-container > h2 {
    font-size: 0.8em;
  }
}
</style>
