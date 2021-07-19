<template>
  <div class="matchInfo__halfTimeInput">
    <div>
      <input
        type="number"
        size="3"
        maxlength="3"
        class="input"
        :value="getMinute"
        @input="changeMinute"
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
        @input="changeSecond"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: ["editing"],
  computed: {
    getMinute() {
      switch (this.editing) {
        case "firstHalf":
          return this.$store.state.compDesc.time.firstHalf.min;
        case "secondHalf":
          return this.$store.state.compDesc.time.secondHalf.min;
        default:
          return 0;
      }
    },
    getSecond() {
      switch (this.editing) {
        case "firstHalf":
          return this.$store.state.compDesc.time.firstHalf.sec;
        case "secondHalf":
          return this.$store.state.compDesc.time.secondHalf.sec;
        default:
          return 0;
      }
    },
    getHalfTime() {
      return this.editing[0].toUpperCase() + this.editing.substring(1);
    },
  },
  methods: {
    changeMinute(event) {
      this.$store.commit(
        `update${this.getHalfTime}Min`,
        parseInt(event.target.value)
      );
    },
    changeSecond(event) {
      this.$store.commit(
        `update${this.getHalfTime}Sec`,
        parseInt(event.target.value)
      );
    },
  },
};
</script>

<style></style>
