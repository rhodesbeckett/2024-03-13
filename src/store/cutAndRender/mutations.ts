import { MutationTree } from "vuex";
import { CutAndRender } from "@/store/cutAndRender/types";

export const mutations: MutationTree<CutAndRender> = {
  UPDATE_CUT_PROGRESS(state, payload: number) {
    state.cutAndRender.cutProgress = payload;
  },
  UPDATE_RENDER_PROGRESS(state, payload: number) {
    state.cutAndRender.renderProgress = payload;
  },
  UPDATE_CURRENT_PROCESS(state, payload: string) {
    state.cutAndRender.currentProcess = payload;
  },
  UPDATE_CAN_CUT(state, payload: boolean) {
    state.cutAndRender.canCut = payload;
  },
  UPDATE_CAN_RENDER(state, payload: boolean) {
    state.cutAndRender.canRender = payload;
  },
};
