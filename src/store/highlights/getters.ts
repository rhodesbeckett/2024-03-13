import { GetterTree } from "vuex";
import { RootState } from "@/store/types";
import { HighlightRow } from "@/store/highlights/types";
import store from '@/store'

export const getters: GetterTree<HighlightRow[], RootState> = {
  highlights(state, rootState) {
    return state.filter((item) => item.editing == store.getters.editing);
  },
  highlightsRow(state) {
    return (id: string) => {
      return state.find((item) => item.id == id);
    };
  },
};
