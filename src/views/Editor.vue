<template>
  <div>
    <transition-group
      name="highlights"
      enter-active-class="highlights-add"
      leave-active-class="highlights-remove"
    >
      <div
        class="columns highlight-row is-centered"
        v-for="(row,index) in highlights"
        :key="(row.id,index)"
        style="align-items: center"
      >
        <EditorInputMin :ID="row.id" part="Min" />
        <EditorInputSec :ID="row.id" part="Sec" />
        <EditorInputToAdd :ID="row.id" part="ToAdd" />
        <EditorButtonDelete :ID="index" />
      </div>
    </transition-group>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import EditorInputMin from "@/components/EditorInputMin.vue";
import EditorInputSec from "@/components/EditorInputSec.vue";
import EditorInputToAdd from "@/components/EditorInputToAdd.vue";
import EditorButtonDelete from "@/components/EditorButtonDelete.vue";

import { mapGetters, mapActions, mapMutations } from "vuex";
import store from "@/store";

export default defineComponent({
  components: {
    EditorInputMin,
    EditorInputSec,
    EditorInputToAdd,
    EditorButtonDelete,
  },
  methods: {
    ...mapActions(["getHighlights"]),
    ...mapMutations(["NEW_ROW"]),
  },
  computed: { ...mapGetters(["highlights"]) },
  created() {
    this.getHighlights();
  },
  watch: {
    highlights: {
      handler: function (val: []) {
        if (val.length == 0) {
          this.NEW_ROW(store.getters.editing);
        }
      },
    },
  },
});
</script>

<style>
.editor-container {
  display: flex;
  flex-direction: column;
  max-width: 1080px;
  margin: 0 auto;
}
.editor-input-min {
  grid-column: 2 / 3;
}
.editor-input-sec {
  grid-column: 4 / 5;
}
.editor-input-to-add {
  grid-column: 6/7;
}
.editor-delete-button {
  grid-column: 7;
}
.editor-main-container--default-edit {
  max-width: none;
  margin: 0;
}
.highlights-add {
  animation: highlights-add 0.6s;
}
@keyframes highlights-add {
  0% {
    transform: rotateX(45deg);
    opacity: 0;
  }
  100% {
    transform: rotateX(0deg);
    opacity: 1;
  }
}
.highlights-remove {
  animation: highlights-remove 0.8s;
}
@keyframes highlights-remove {
  0% {
    transform: rotateX(0deg);
    opacity: 1;
  }
  100% {
    transform: rotateX(45deg);
    opacity: 0;
  }
}
.highlights-update {
  animation: highlights-update 1.8s;
}
@keyframes highlights-update {
  0% {
    transform: rotateX(0deg);
    opacity: 1;
  }
  50% {
    transform: rotateX(45deg);
    opacity: 0.5;
  }
  100% {
    transform: rotateX(0deg);
    opacity: 1;
    position: absolute;
  }
}
.highlights-move {
  transition: transform 5s;
}
</style>
