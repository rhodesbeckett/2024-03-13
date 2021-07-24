import { Module } from "vuex";
import { CutAndRender } from "@/store/cutAndRender/types";
import { RootState } from "@/store/types";
import { getters } from "@/store/cutAndRender/getters";
import { mutations } from "@/store/cutAndRender/mutations";
import { actions } from "@/store/cutAndRender/actions";

const state: CutAndRender = {
  cutAndRender: {
    currentProcess: "",
    canCut: false,
    canRender: false,
    cutProgress: 0,
    renderProgress: 0,
  },
};

export const cutAndRender: Module<CutAndRender, RootState> = {
  state,
  getters,
  mutations,
  actions,
};
