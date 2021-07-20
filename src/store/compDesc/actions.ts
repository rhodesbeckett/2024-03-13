import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { CompDescState } from "./types";
import GET from "@/plugins/axios";
import { POST } from "@/plugins/axios";
import { COOKIE } from "@/plugins/cookie";

export const actions: ActionTree<CompDescState, RootState> = {
  setCompDesc(state, payload) {
    const query = `update/${COOKIE()}/compDesc`;
    POST(query, state).then((res) => {
      if (res.data.msg) {
        console.log(res.data.msg);
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
    });
  },
  getTitle(): string {
    return "test";
  },
};
