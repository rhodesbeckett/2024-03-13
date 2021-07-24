import { GetterTree } from "vuex";
import { RootState } from "@/store/types";
import { CutAndRender } from "@/store/cutAndRender/types";

export const getters: GetterTree<CutAndRender, RootState> = {
  cutProgress(state) {
    return state.cutAndRender.cutProgress;
  },
  renderProgress(state) {
    return state.cutAndRender.renderProgress;
  },
  canCut(state) {
    return state.cutAndRender.canCut;
  },
  canRender(state) {
    return state.cutAndRender.canRender;
  },
  currentProcess(state) {
    return state.cutAndRender.currentProcess;
  },
};
