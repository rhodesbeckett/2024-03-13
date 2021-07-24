import { MutationTree } from "vuex";
import { Testing, TestingI } from "@/store/testing/types";

export const mutations: MutationTree<Testing> = {
  NEW_TESTING(state, testing: TestingI): void {
    state.testing = testing;
  },
};
