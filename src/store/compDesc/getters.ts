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
  firstHalfMin(state) {
    return state.time.firstHalf.min;
  },
  secondHalfMin(state) {
    return state.time.secondHalf.min;
  },
  firstHalfSec(state) {
    return state.time.firstHalf.sec;
  },
  secondHalfSec(state) {
    return state.time.secondHalf.sec;
  },
};
