import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { Editor } from "@/store/editor/types";
import { COOKIE } from "@/plugins/cookie";
import GET, { POST } from "@/plugins/axios";

export const actions: ActionTree<Editor, RootState> = {
  getHighlights({ commit, state, rootGetters }) {
    const query = `getHighlights/${COOKIE()}`;
    GET(query).then((res) => {
      const highlightRows = JSON.parse(res.data.highlights);
      if (highlightRows.length > 0) {
        commit("NEW_HIGHLIGHTS", highlightRows);
      } else if (highlightRows.length == 0 && state.highlights.length == 0) {
        commit("NEW_ROW", rootGetters.editing);
      }
    });
  },

  setHighlights({ state }) {
    const query = `update/${COOKIE()}/highlights`;
    POST(query, state.highlights).then((res) => {
      if (res.data.msg == "success") {
        return "hello world";
      }
    });
  },
};
