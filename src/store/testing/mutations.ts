import { MutationTree } from "vuex";
import { TestingState } from "@/store/testing/types";

export const mutations: MutationTree<TestingState> = {
  NEW_TESTING(state, testing: TestingState): void {
    state = testing;
    console.log(state);
  },
};
