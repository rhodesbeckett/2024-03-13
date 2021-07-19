import { RootState } from "@/store/types";
import { TestingState } from "@/store/testing/types";
import { Module } from "vuex";
import { getters } from "@/store/testing/getters";
import { actions } from "@/store/testing/actions";
import { mutations } from "@/store/testing/mutations";
const state: TestingState = {
  halfTime: false,
  src: false,
  highlights: false,
};

export const testing: Module<TestingState, RootState> = {
  state,
  getters,
  actions,
  mutations,
};
