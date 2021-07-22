import { MutationTree } from "vuex";
import { MatchInfo, CompDesc, Halftime } from "./types";
export const mutations: MutationTree<MatchInfo> = {
  NEW_COMP_DESC(state, payload: CompDesc) {
    state.compDesc = payload;
  },
  UPDATE_TITLE(state, payload: string) {
    state.compDesc.title = payload;
  },
  UPDATE_EDITING(state, payload: string) {
    state.compDesc.editing = payload;
  },
  UPDATE_SRC(state, payload: string) {
    state.compDesc.src = payload;
  },
  UPDATE_IS_CHOSEN(state, payload: boolean) {
    state.compDesc.time.isChosen = payload;
  },
  UPDATE_START_FIRST_HALF(state, payload: Halftime) {
    state.compDesc.time.firstHalf = payload;
  },
  UPDATE_START_SECOND_HALF(state, payload: Halftime) {
    state.compDesc.time.secondHalf = payload;
  },
  UPDATE_FIRST_HALF_MIN(state, payload: null | number) {
    state.compDesc.time.firstHalf.min = payload;
  },
  UPDATE_FIRST_HALF_SEC(state, payload: null | number) {
    state.compDesc.time.firstHalf.sec = payload;
  },
  UPDATE_SECOND_HALF_SEC(state, payload: null | number) {
    state.compDesc.time.secondHalf.sec = payload;
  },
  UPDATE_SECOND_HALF_MIN(state, payload: null | number) {
    state.compDesc.time.secondHalf.min = payload;
  },
};
