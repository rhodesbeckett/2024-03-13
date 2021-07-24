<template>
  <div class="columns is-centered is-multiline">
    <div class="column is-12 matchInfo-container">
      <MatchInfoInputTitle />
      <MatchInfoInputSrc />
      <MatchInfoEditing />
      <div
        class="matchInfo__input--half matchInfo__radio-btns"
        v-if="isChosen == false"
      >
        <RadioButtonHalfTime :halftime="1" />
        <RadioButtonHalfTime :halftime="2" />
      </div>
      <h1 class="title matchInfo__title">1st:</h1>
      <MatchInfoInputHalftime
        v-if="editing == 'firstHalf'"
        editing="first_half"
      />
      <h1 class="title matchInfo__title">2nd:</h1>
      <MatchInfoInputHalftime
        v-if="editing == 'secondHalf'"
        editing="second_half"
      />
      <MatchInfoSaveButton />
    </div>
  </div>
</template>

<script lang="ts">
import MatchInfoEditing from "@/components/MatchInfoEditing.vue";
import MatchInfoInputHalftime from "@/components/MatchInfoInputHalftime.vue";
import MatchInfoInputSrc from "@/components/MatchInfoInputSrc.vue";
import MatchInfoInputTitle from "@/components/MatchInfoInputTitle.vue";
import MatchInfoSaveButton from "@/components/MatchInfoSaveButton.vue";
import RadioButtonHalfTime from "@/components/RadioButtonHalfTime.vue";

import { defineComponent } from "vue";
import { mapActions, mapGetters } from "vuex";
export default defineComponent({
  components: {
    MatchInfoInputTitle,
    MatchInfoInputSrc,
    MatchInfoInputHalftime,
    MatchInfoEditing,
    MatchInfoSaveButton,
    RadioButtonHalfTime,
  },
  methods: { ...mapActions(["getCompDesc", "setCompDesc"]) },
  computed: { ...mapGetters(["isChosen", "editing"]) },
  created() {
    this.getCompDesc();
  },
});
</script>

<style>
.matchInfo-container {
  display: grid;
  grid-template-columns:
    [title-start] 1fr
    [title-end] 2fr
    [input-start] 2fr
    [half-of-input] 4fr
    [input-end];
  grid-template-rows: repeat(6, 1fr);
  justify-content: center;
  max-width: 1080px;
  margin: 0 auto;
}
.matchInfo__title {
  grid-column: title;
}
@media (max-width: 1027px) {
  .matchInfo__title {
    font-size: 1.8em;
  }
}
.matchInfo__input {
  grid-column: title-end / input-end;
}
.matchInfo__editing-response {
  grid-column: title-end / input-start;
  justify-self: center;
}
.matchInfo__input--half {
  grid-column: title-end / half-of-input;
}
.matchInfo__radio-btns,
.matchInfo__halfTimeInput {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
@media (max-width: 1027px) {
  .matchInfo__radio-btns,
  .matchInfo__halfTimeInput {
    align-items: flex-start;
  }
}
@media (max-width: 768px) {
  .matchInfo__halfTimeInput {
    grid-column: title-start / input-end;
    justify-content: start;
  }
}
.matchInfo__saveBtn {
  grid-column: title-start / input-start;
}
</style>
