import { GetterTree } from "vuex";
import { Testing, TestingI } from "@/store/testing/types";
import { RootState } from "@/store/types";

export const getters: GetterTree<Testing, RootState> = {
  testSrc(state): boolean {
    return state.testing.src;
  },
  testHalftime(state): boolean {
    return state.testing.halfTime;
  },
  testHighlights(state): boolean {
    return state.testing.highlights;
  },
  updatedTesting(state): boolean {
    if (
      state.testing.src == true &&
      state.testing.halfTime == true &&
      state.testing.highlights == true
    ) {
      return true;
    } else {
      return false;
    }
  },
};
