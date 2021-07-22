import { GetterTree } from "vuex";
import { RootState } from "@/store/types";
import { MatchInfo} from "./types";

export const getters: GetterTree<MatchInfo, RootState> = {
  title(state) {
    return state.compDesc.title;
  },
  src(state) {
    return state.compDesc.src;
  },
  isChosen(state) {
    return state.compDesc.time.isChosen;
  },
  editing(state) {
    return state.compDesc.editing;
  },
  firstHalfMin(state) {
    return state.compDesc.time.firstHalf.min;
  },
  secondHalfMin(state) {
    return state.compDesc.time.secondHalf.min;
  },
  firstHalfSec(state) {
    return state.compDesc.time.firstHalf.sec;
  },
  secondHalfSec(state) {
    return state.compDesc.time.secondHalf.sec;
  },
};
