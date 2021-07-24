import { Module } from "vuex";
import { RootState } from "../types";
import { MatchInfo } from "./types";
import { mutations } from "@/store/matchInfo/mutations";
import { getters } from "@/store/matchInfo/getters";
import { actions } from "@/store/matchInfo/actions";
const state: MatchInfo = {
  compDesc: {
    title: "",
    src: "",
    editing: "firstHalf",
    time: {
      isChosen: false,
      firstHalf: { min: null, sec: null },
      secondHalf: { min: null, sec: null },
    },
  },
};

export const compDesc: Module<MatchInfo, RootState> = {
  state: state,
  mutations,
  actions,
  getters,
};
