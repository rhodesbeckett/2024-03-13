import { GetterTree } from "vuex";
import { TestingState } from "@/store/testing/types";
import { RootState } from "@/store/types";

export const getters: GetterTree<TestingState, RootState> = {
  testSrc(state): boolean {
    return state.src;
  },
  testHalftime(state): boolean {
    return state.halfTime;
  },
  testHighlights(state): boolean {
    return state.highlights;
  },
  updatedTesting(state): boolean {
    if (
      state.src == true &&
      state.halfTime == true &&
      state.highlights == true
    ) {
      return true;
    } else {
      return false;
    }
  },
};
