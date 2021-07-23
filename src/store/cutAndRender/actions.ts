import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { COOKIE } from "@/plugins/cookie";
import GET, { POST } from "@/plugins/axios";
import { CutAndRender } from "./types";

export const actions: ActionTree<CutAndRender, RootState> = {
  getCanCut({ commit, state }) {
    const query = `getCanCut/${COOKIE()}`;
    GET(query).then((res) => {
      commit("UPDATE_CAN_CUT", res.data.canCut);
    });
  },
  getCanRender({ commit, state }) {
    const query = `getCanRender/${COOKIE()}`;
    GET(query).then((res) => {
      commit("UPDATE_CAN_RENDER", res.data.canRender);
    });
  },
  getCutProgress({ commit, state }) {
    const cutInterval = setInterval(() => {
      GET(`getCutProgress/${COOKIE()}`).then((res) => {
        commit("UPDATE_CUT_PROGRESS", res.data.cutProgress);
        if (res.data.cutProgress == 100.0) {
          clearInterval(cutInterval);
          commit("UPDATE_CURRENT_PROCESS", "");
        }
      });
    }, 1000);
  },

  cut({ commit, state }) {
    if (
      state.cutAndRender.canCut == true &&
      state.cutAndRender.currentProcess == ""
    ) {
      const query = `cut/${COOKIE()}`;
      GET(query).then((res) => {
        if (res.data.msg) {
          commit("UPDATE_CURRENT_PROCESS", "cut");
        }
      });
    }
    console.log(commit, state);
  },
  getRenderProgress({ commit, state }) {
    const cutInterval = setInterval(() => {
      GET(`getRenderProgress/${COOKIE()}`).then((res) => {
        commit("UPDATE_RENDER_PROGRESS", res.data.renderProgress);
        if (res.data.cutProgress == 100.0) {
          clearInterval(cutInterval);
          commit("UPDTE_CURRENT_PROCESS", "");
        }
      });
    }, 1000);
  },
  render({ commit, state }) {
    if (
      state.cutAndRender.canRender == true &&
      state.cutAndRender.currentProcess == ""
    ) {
      const query = `render/${COOKIE()}`;
      GET(query).then((res) => {
        if (res.data.msg) {
          commit("UPDATE_CURRENT_PROCESS", "render");
        }
      });
    }
    console.log(commit, state);
  },
};
