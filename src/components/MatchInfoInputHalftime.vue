<template>
  <div class="matchInfo__halfTimeInput">
    <div>
      <input
        type="number"
        size="3"
        maxlength="3"
        class="input"
        :value="getMinute"
        @input="updateMinute"
      />
    </div>
    <span style="margin: 0 1.5em">:</span>
    <div>
      <input
        type="number"
        size="3"
        maxlength="3"
        class="input"
        :value="getSecond"
        @input="updateSecond"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { mapGetters } from "vuex";
import store from "@/store";
import { defineComponent } from "vue";
import { EventEditor } from "@/composables/EventEditor";

export default defineComponent({
  props: { editing: String },
  computed: {
    ...mapGetters([
      "firstHalfMin",
      "secondHalfMin",
      "firstHalfSec",
      "secondHalfSec",
    ]),
    getMinute(): number {
      switch (this.editing) {
        case "first_half":
          return this.firstHalfMin;
        case "second_half":
          return this.secondHalfMin;
        default:
          return 0;
      }
    },
    getSecond(): number {
      switch (this.editing) {
        case "first_half":
          return this.firstHalfSec;
        case "second_half":
          return this.secondHalfSec;
        default:
          return 0;
      }
    },
    getHalftime(): string | undefined {
      return this.editing?.toUpperCase();
    },
  },
  methods: {
    updateMinute(event: EventEditor) {
      store.commit(
        `UPDATE_${this.getHalftime}_MIN`,
        parseInt(event.target.value)
      );
    },
    updateSecond(event: EventEditor) {
      store.commit(
        `UPDATE_${this.getHalftime}_SEC`,
        parseInt(event.target.value)
      );
    },
  },
});
</script>

<style></style>
