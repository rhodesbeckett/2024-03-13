<template>
  <div class="column is-1 is-2-mobile">
    <input
      class="input highlights-input"
      min="0"
      max="999"
      size="3"
      maxlength="3"
      type="text"
      :value="this.getMin()"
      @input="updateMin"
    />
  </div>
  <div class="column is-1 is-2-mobile center-dot">:</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import useEditorInput from "@/composables/useEditorInput";
export default defineComponent({
  props: { ID: String, part: String },
  setup(props) {
    const { getMin, updateMin } = useEditorInput(props.ID, props.part);
    return { getMin, updateMin };
  },
  computed: {
    test(): number {
      return this.getMin();
    },
  },
});
</script>

<style></style>
