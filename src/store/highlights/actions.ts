import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { HighlightRow } from "@/store/highlights/types";

export const actions: ActionTree<HighlightRow[], RootState> = {
  getHighlights({ commit }) {
    console.log(commit);
  },
  setHighlights({ commit, state }) {
    console.log(commit, state);
  },
};
