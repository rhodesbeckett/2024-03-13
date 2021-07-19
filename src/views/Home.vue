<template>
  <div>
    <div class="columns is-centered is-multiline">
      <div class="column" style="align-self: center; flex: none">
        <a class="add-btn" @click="setMatchID()"
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
import axios from "axios";
import CardMatchComp from "../components/CardMatchComp.vue";

export default {
  name: "Home",
  components: { CardMatchComp },
  data(): any {
    return {
      matchComps: [],
    };
  },
  methods: {
    setMatchID(): void {
      this.createMC();
    },
    getAllComps(): void {
      const path = "http://localhost:5000/getAll";
      axios.get(path).then((res) => {
        this.matchComps = JSON.parse(res.data.allComps);
      });
    },
    createMC(): void {
      const path = "http://localhost:5000/insert";
      axios.get(path).then((res) => {
        console.log(res);
        this.$cookies.set("mcID", res.data.mcID, "1500d", true);
        this.$router.push("matchCompInfo");
      });
    },
  },
  created(): void {
    this.getAllComps();
  },
};
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
