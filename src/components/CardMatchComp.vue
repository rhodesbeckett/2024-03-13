<template>
  <span class="matchComp-row">
    <h1 class="title compTitle" @click="setMatchID(comp._id.$oid)">
      {{ comp.compDesc.title }}
    </h1>
    <h3 class="halfTime">Editing:</h3>
    <RadioBtnHalfTime
      class="radio1"
      :radioClick="radioClick"
      :halfTime="1"
      :matchCompID="comp._id.$oid"
    />
    <RadioBtnHalfTime
      class="radio2"
      :radioClick="radioClick"
      :halfTime="2"
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
import RadioBtnHalfTime from "../components/RadioBtnHalfTime.vue";
import { mapMutations, mapActions } from "vuex";
import axios from "axios";
import gsap from "gsap";
import { defineComponent } from "@vue/composition-api";

interface DataI {
  mergeTrue: string;
  mergeFalse: string;
}
export default defineComponent({
  props: ["comp"],
  data(): DataI {
    return {
      mergeTrue: "Merging will start..",
      mergeFalse: "One halftime is missing. Action aborted.",
    };
  },
  components: { RadioBtnHalfTime },
  methods: {
    ...mapMutations(["updateIsChosen", "updateEditing"]),
    ...mapActions(["getCompDesc", "setCompDesc"]),
    setMatchID(id: string): void {
      this.$cookie.setCookie("mcID", id, { expire: "1500d", sameSite: "Lax" });
      this.$router.push("matchCompInfo");
    },
    radioClick(halfTime: number, matchCompID: string): void {
      this.setMatchID(matchCompID);
      setTimeout(() => {
        this.updateIsChosen(true);
        if (halfTime == 1) {
          this.updateEditing("firstHalf");
        } else {
          this.updateEditing("secondHalf");
        }
        /* tslint:disable:no-empty */
        this.setCompDesc({
          showMessage: function () {
            return null;
          },
        });
      }, 1000);
    },
    mergeVideos(ID: string): void {
      axios.get(`http://localhost:5000/mergeVideos/${ID}`).then((res) => {
        if (res.data.msg == false) {
          this.showMessage(this.$refs.messageServer, this.mergeFalse);
        } else if (res.data.msg == true) {
          this.showMessage(this.$refs.messageServer, this.mergeTrue);
        }
      });
    },
    showMessage(element: Element, text: string): void {
      element.textContent = text;
      setTimeout(function () {
        let elemAnim = gsap.to(element, { duration: 1.5, opacity: 1.0 });
        setTimeout(function () {
          elemAnim.reverse();
        }, 1500);
      }, 1000);
    },
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
