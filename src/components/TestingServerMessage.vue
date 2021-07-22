<template>
  <div
    class="message-server message-server--centered message-server--not-visible"
    ref="messageServer"
  >
    You can cut and render!
  </div>
</template>

<script lang="ts">
import GET from "@/plugins/axios";
import gsap from "gsap";
import { defineComponent, ref } from "vue";
import { mapActions, mapGetters } from "vuex";

export default defineComponent({
  setup() {
    const messageServer = ref(Element);

    function showMessage() {
      const element = messageServer.value;
      setTimeout(function () {
        let elemAnim = gsap.to(element, { duration: 0.5, opacity: 1.0 });
        setTimeout(function () {
          elemAnim.reverse();
        }, 700);
      }, 1000);
    }

    return { showMessage, messageServer };
  },

  methods: {
    ...mapActions(["getTesting"]),
    updateDOM() {
      if (this.updatedTesting == true) {
        this.showMessage();
      }
    },
  },
  computed: { ...mapGetters(["updatedTesting"]) },

  created() {
    const parameters = { updateDOM: this.updateDOM };
    this.getTesting(parameters);
  },
});
</script>

<style></style>
