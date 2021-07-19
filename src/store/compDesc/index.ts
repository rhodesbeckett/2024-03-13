import { Module } from "vuex";
import { RootState } from "../types";
import { CompDescState } from "./types";
import { mutations } from "@/store/compDesc/mutations";
import { getters } from "@/store/compDesc/getters";
import { actions } from "@/store/compDesc/actions";

const state: CompDescState = {
  title: "",
  src: "",
  editing: "firstHalf",
  time: {
    isChosen: false,
    firstHalf: { min: null, sec: null },
    secondHalf: { min: null, sec: null },
  },
};

export const compDesc: Module<CompDescState, RootState> = {
  state: state,
  mutations,
  actions,
  getters,
};
