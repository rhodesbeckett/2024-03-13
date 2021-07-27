import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { Testing, TestingI } from "@/store/testing/types";
import { COOKIE } from "@/plugins/cookie";
import GET, { POST } from "@/plugins/axios";

export const actions: ActionTree<Testing, RootState> = {
  getTesting({ commit }, payload: any) {
    const query = `getTesting/${COOKIE()}`;
    GET(query).then((res) => {
      const parsed = JSON.parse(res.data.testing);
      commit("NEW_TESTING", parsed);
      payload.updateDOM();
      this.dispatch("updateCanCut", canCut(parsed));
      this.dispatch("updateCanRender", canCut(parsed));
    });
  },
  updateCanCut({state},payload) {
    const query = `update/${COOKIE()}/cutAndRender.canCut`;
    POST(query, payload).then((res) => {
      console.log(res);
    });
  },
  updateCanRender({state},payload) {
    const query = `update/${COOKIE()}/cutAndRender.canRender`;
    POST(query,  payload).then((res) => {
      console.log(res);
    });
  },
  setTesting({ state }) {
    const query = `update/${COOKIE()}/testing`;
    POST(query, state.testing).then((res) => {
      console.log(res);
    });
  },
};

function canCut(data: TestingI): boolean {
  if (data.halfTime == true && data.highlights == true && data.src == true) {
    return true;
  } else {
    return false;
  }
}
