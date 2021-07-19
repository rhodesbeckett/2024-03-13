<template>
  <div class="column is-1 is-2-mobile">
    <input
      class="input highlights-input"
      min="0"
      max="999"
      size="3"
      maxlength="3"
      type="text"
      :value="getValue"
      @input="this.updateValue"
      @keydown.tab="newRowTab()"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "@vue/composition-api";
import { mapMutations, mapActions, mapGetters } from "vuex";
interface eventValue<T> {
  target: { value: string };
  test?: string;
}
export default defineComponent({
  props: ["id", "part"],
  methods: {
    ...mapMutations(["newRow"]),
    ...mapActions(["setHighlights"]),
    updateValue(event: eventValue<Event>): void {
      this.$store.commit(`updateHighlightsRow${this.part}`, {
        id: this.id,
        value: this.toInt(event.target.value),
      });
    },
    checkRow(id: string): boolean | undefined {
      let row = this.highlightsRow(id);
      if (
        Number.isInteger(row.min) &&
        Number.isInteger(row.sec) &&
        Number.isInteger(row.toAdd)
      ) {
        return true;
      }
    },
    checkAllRows(): boolean {
      let row = this.highlights;
      for (let i = 0; i < row.length; i++) {
        if (this.checkRow(row[i].id) == true) {
          continue;
        } else {
          return false;
        }
      }
      return true;
    },
    newRowTab(): void {
      if (this.part == "ToAdd") {
        if (this.checkRow(this.id) == true) {
          if (this.checkAllRows()) {
            this.highlightsRow(this.id).editing = this.editing;
            this.newRow();
            this.setHighlights();
          }
        }
      }
    },
    toInt(value: string): null | number {
      if (value == "") {
        return null;
      } else {
        return parseInt(value);
      }
    },
  },
  computed: {
    ...mapGetters(["highlightsRow", "highlights", "editing"]),
    getValue(): any {
      if (this.part == "Min") {
        return this.highlightsRow(this.id).min;
      } else if (this.part == "Sec") {
        return this.highlightsRow(this.id).sec;
      } else {
        return this.highlightsRow(this.id).toAdd;
      }
    },
  },
});
</script>

<style></style>
