import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { Testing, TestingI } from "@/store/testing/types";
import { COOKIE } from "@/plugins/cookie";
import GET, { POST } from "@/plugins/axios";

export const actions: ActionTree<Testing, RootState> = {
  getTesting({ commit }, payload: any) {
    const query = `getTesting/${COOKIE()}`;
    GET(query).then((res) => {
      const parsed = JSON.parse(res.data.testing) 
      commit("NEW_TESTING", parsed );
      payload.updateDOM();
      this.dispatch('updateCanCut',canCut(parsed))
      this.dispatch('updateCanRender',canCut(parsed))
    });
  },
  updateCanCut({ commit }, payload) {
    const query = `update/${COOKIE()}/canCut`;
    POST(query, payload).then((res) => {
      console.log(res);
    });
  },
  updateCanRender({ commit }, payload) {
    const query = `update/${COOKIE()}/canRender`;
    POST(query, payload).then((res) => {
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
