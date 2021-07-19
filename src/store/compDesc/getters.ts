import { GetterTree } from "vuex";
import { RootState } from "@/store/types";
import { CompDescState } from "./types";

export const getters: GetterTree<CompDescState, RootState> = {
  title(state) {
    return state.title;
  },
  src(state) {
    return state.src;
  },
  isChosen(state) {
    return state.time.isChosen;
  },
  editing(state) {
    return state.editing;
  },
};
