import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { HighlightRow } from "@/store/highlights/types";
import { COOKIE } from "@/plugins/cookie";
import GET, { POST } from "@/plugins/axios";

export const actions: ActionTree<HighlightRow[], RootState> = {
  getHighlights({ commit, state, rootState }) {
    const query = `getHighlights/${COOKIE()}`;
    GET(query).then((res) => {
      const highlightRows = JSON.parse(res.data.highlights);
      if (highlightRows.length > 0) {
        commit("NEW_HIGHLIGHTS", highlightRows);
      } else if (highlightRows.length == 0 && state.length == 0) {
        commit("NEW_ROW", rootState);
      }
    });
  },

  setHighlights({ getters }) {
    const query = `update/${COOKIE()}/highlights`;
    POST(query, getters.highlights).then((res) => {
      if (res.data.msg == "success") {
        return 'hello world';
      }
    });
  },
};
