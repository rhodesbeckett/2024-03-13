<template>
  <a
    class="matchInfo__title button is-success"
    @click="saveBtn"
    style="margin-top: 0.75em"
    >SAVE
    <div class="message-server" ref="messageServer">MatchInfo saved!</div>
  </a>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import gsap from "gsap";
import { mapActions } from "vuex";

export default defineComponent({
  methods: {
    ...mapActions(["setCompDesc"]),
    saveBtn() {
      this.setCompDesc(this);
    },
    showMessage() {
      let elemAnim = gsap.to(".message-server", { duration: 0.3, scale: 1.0 });
      setTimeout(function () {
        elemAnim.reverse();
      }, 500);
    },
  },
});
</script>

<style></style>
