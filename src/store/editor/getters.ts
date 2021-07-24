import { GetterTree } from "vuex";
import { RootState } from "@/store/types";
import { HighlightRow } from "@/store/editor/types";
import { Editor } from "@/store/editor/types";
import store from "@/store";

export const getters: GetterTree<Editor, RootState> = {
  highlights(state): HighlightRow[] {
    return state.highlights.filter(
      (item) => item.editing == store.getters.editing
    );
  },
  highlightsRow(state) {
    return (id: string) => {
      return state.highlights.find((item) => item.id == id);
    };
  },
};
