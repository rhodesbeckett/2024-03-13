import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { Testing, TestingI } from "@/store/testing/types";
import { COOKIE } from "@/plugins/cookie";
import GET from "@/plugins/axios";

export const actions: ActionTree<Testing, RootState> = {
  getTesting({ commit }, payload: any) {
    const query = `getTesting/${COOKIE()}`;
    GET(query).then((res) => {
      commit("NEW_TESTING", JSON.parse(res.data.testing));
      payload.updateDOM();
    });
  },
};
