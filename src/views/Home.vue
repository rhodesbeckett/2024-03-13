<template>
  <div>
    <div class="columns is-centered is-multiline">
      <div class="column" style="align-self: center; flex: none">
        <a class="add-btn" @click="createMC()"
          ><i class="fas fa-plus-circle"></i
        ></a>
      </div>
    </div>

    <transition-group
      class="columns is-centered is-multiline"
      tag="div"
      name="matchComp"
    >
      <div v-for="comp in matchComps" :key="comp._id.$oid" class="column is-7">
        <CardMatchComp :comp="comp" />
      </div>
    </transition-group>
  </div>
</template>

<script lang="ts">
import CardMatchComp from "@/components/CardMatchComp.vue";
import { defineComponent } from "vue";
import GET from "@/plugins/axios";
import useCompHelpers from "@/composables/useCompHelpers";

export default defineComponent({
  name: "Home",
  setup() {
    const { setMatchID } = useCompHelpers();
    return { setMatchID };
  },
  data() {
    return { matchComps: [] };
  },
  components: { CardMatchComp },
  methods: {
    getAllComps() {
      const query = "getAll";
      GET(query).then((res) => {
        this.matchComps = JSON.parse(res.data.allComps);
      });
    },
    createMC() {
      const query = "insert";
      GET(query).then((res) => {
        this.setMatchID(res.data.mcID);
      });
    },
  },
  mounted() {
    this.getAllComps();
  },
});
</script>

<style scoped>
@keyframes matchComp {
  0% {
    transform: skewX(60deg) rotate(-5deg);
    opacity: 0.7;
  }
  100% {
    transform: skewX(0deg) rotate(0deg);
    opacity: 1;
  }
}
.matchComp-enter-active {
  animation: matchComp 0.5s;
}
.matchComp-leave-active {
  animation: matchComp 0.5s;
}
</style>
