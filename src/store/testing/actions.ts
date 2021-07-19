import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { TestingState } from "@/store/testing/types";

export const actions: ActionTree<TestingState, RootState> = {
  getTesting({ commit }) {
    console.log(commit);
  },
};
