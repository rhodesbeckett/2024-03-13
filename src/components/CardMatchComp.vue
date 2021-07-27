<template>
  <span class="matchComp-row">
    <h1 class="title compTitle" @click="setMatchID(comp._id.$oid)">
      {{ comp.compDesc.title }}
    </h1>
    <h3 class="halfTime">Editing: {{ comp.compDesc.editing }}</h3>

    <RadioButtonHalfTime
      class="radio1"
      :halftime="1"
      :matchCompID="comp._id.$oid"
    />
    <RadioButtonHalfTime
      class="radio2"
      :halftime="2"
      :matchCompID="comp._id.$oid"
    />

    <a class="button btnMerge" @click="mergeVideos(comp._id.$oid)"
      >Merge halfTime</a
    >
    <div
      class="
        message-server
        message-server--centered
        message-server--not-visible
        message-server--merge
      "
      ref="messageServer"
    ></div>
  </span>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import RadioButtonHalfTime from "@/components/RadioButtonHalfTime.vue";
import useCompHelpers from "@/composables/useCompHelpers";
import GET from "@/plugins/axios";
import { COOKIE } from "@/plugins/cookie";
import gsap from "gsap";
export default defineComponent({
  setup() {
    const { setMatchID } = useCompHelpers();
    return { setMatchID };
  },
  components: { RadioButtonHalfTime },
  methods: {
    mergeVideos(ID: string) {
      GET(`mergeVideos/${COOKIE()}`).then((res) => {
        if (res.data.msg == false) {
          this.showMessage(".message-server", this.mergeFalse);
        } else if (res.data.msg == true) {
          this.showMessage(".message-server", this.mergeTrue);
        }
      });
    },
    showMessage(element: string, text: string) {
      const domElement = document.querySelector(element);
      if (domElement) domElement.textContent = text;
      setTimeout(function () {
        let elemAnim = gsap.to(element, { duration: 1.5, opacity: 1.0 });
        setTimeout(function () {
          elemAnim.reverse();
        }, 1500);
      }, 1000);
    },
  },

  props: ["comp"],
  data() {
    return {
      mergeTrue: "Merging will start..",
      mergeFalse: "One halftime is missing. Action aborted.",
    };
  },
});
</script>
<style scoped>
.matchComp-row {
  display: grid;
  grid-template-areas:
    "compTitle compTitle compTitle"
    "halfTime radio1 radio2"
    "btnMerge . .";
  justify-content: space-between;
  background: url("~@/assets/test.svg");
  background-repeat: no-repeat;
  transition: all 0.5s;
}

#path1481:hover {
  fill: #da4567;
}
.compTitle {
  grid-area: compTitle;
}
.compTitle:hover {
  cursor: pointer;
}
.compTitle:active {
  color: rgb(141, 137, 137);
}

.halfTime {
  grid-area: halfTime;
}
.radio1 {
  grid-area: radio1;
}
.radio2 {
  grid-area: radio2;
}
.btnMerge {
  grid-area: btnMerge;
  margin-top: 0.5em;
}
</style>
