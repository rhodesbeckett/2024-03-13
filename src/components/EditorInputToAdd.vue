<template>
  <div class="column is-1 is-2-mobile">
    <input
      class="input highlights-input"
      min="0"
      max="999"
      size="3"
      maxlength="3"
      type="text"
      :value="this.getToAdd()"
      @input="updateToAdd"
      @keydown.tab="this.newRowTab()"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import useEditorInput from "@/composables/useEditorInput";
import useNewRow from "@/composables/useNewRow";
export default defineComponent({
  props: { ID: String, part: String },
  setup(props) {
    const { getToAdd, updateToAdd } = useEditorInput(props.ID, props.part);
    const { newRowTab } = useNewRow(props.ID);
    return { getToAdd, updateToAdd,newRowTab };
  },
});
</script>

<style></style>
