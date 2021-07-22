import { RootState } from "@/store/types";
import { Testing } from "@/store/testing/types";
import { Module } from "vuex";
import { getters } from "@/store/testing/getters";
import { actions } from "@/store/testing/actions";
import { mutations } from "@/store/testing/mutations";
const state: Testing = {
  testing: {
    halfTime: false,
    src: false,
    highlights: false,
  },
};

export const testing: Module<Testing, RootState> = {
  state,
  getters,
  actions,
  mutations,
};
