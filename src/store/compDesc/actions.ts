import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { CompDescState } from "./types";
import GET from "@/plugins/axios";
import { POST } from "@/plugins/axios";
import { COOKIE } from "@/plugins/cookie";

export const actions: ActionTree<CompDescState, RootState> = {
  setCompDesc(state, payload) {
    const query = `update/${COOKIE()}/compDesc`;
    POST(query, state.state).then((res) => {
      if (res.data.msg) {
        payload.showMessage();
        return null;
      }
    });
  },
  getCompDesc() {
    const query = `getMC/${COOKIE()}`;
    GET(query).then((res) => {
      const compDesc = JSON.parse(`${res.data.compDesc}`);
      this.commit("NEW_COMP_DESC", compDesc);
      this.commit("UPDATE_TITLE", compDesc.title);
      this.commit("UPDATE_SRC", compDesc.src);
      this.commit("UPDATE_EDITING", compDesc.editing);
      this.commit("UPDATE_IS_CHOSEN", compDesc.time.isChosen);
      this.commit("UPDATE_FIRST_HALF_MIN", compDesc.time.firstHalf.min);
      this.commit("UPDATE_SECOND_HALF_MIN", compDesc.time.secondHalf.min);
      this.commit("UPDATE_FIRST_HALF_SEC", compDesc.time.firstHalf.sec);
      this.commit("UPDATE_SECOND_HALF_SEC", compDesc.time.secondHalf.sec);
    });
  },
  getTitle(): string {
    return "test";
  },
};
