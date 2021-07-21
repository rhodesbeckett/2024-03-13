import { MutationTree } from "vuex";
import { CompDescState, Halftime } from "./types";
export const mutations: MutationTree<CompDescState> = {
  NEW_COMP_DESC(state, payload: CompDescState) {
    state = payload;
  },
  UPDATE_TITLE(state, payload: string) {
    state.title = payload;
  },
  UPDATE_EDITING(state, payload: string) {
    state.editing = payload;
  },
  UPDATE_SRC(state, payload: string) {
    state.src = payload;
  },
  UPDATE_IS_CHOSEN(state, payload: boolean) {
    state.time.isChosen = payload;
  },
  UPDATE_START_FIRST_HALF(state, payload: Halftime) {
    state.time.firstHalf = payload;
  },
  UPDATE_START_SECOND_HALF(state, payload: Halftime) {
    state.time.secondHalf = payload;
  },
  UPDATE_FIRST_HALF_MIN(state, payload: null | number) {
    state.time.firstHalf.min = payload;
  },
  UPDATE_FIRST_HALF_SEC(state, payload: null | number) {
    state.time.firstHalf.sec = payload;
  },
  UPDATE_SECOND_HALF_SEC(state, payload: null | number) {
    state.time.secondHalf.sec = payload;
  },
  UPDATE_SECOND_HALF_MIN(state, payload: null | number) {
    state.time.secondHalf.min = payload;
  },
};
