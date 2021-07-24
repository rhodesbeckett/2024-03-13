import { MutationTree } from "vuex";
import { HighlightRow } from "@/store/editor/types";
import { Editor } from "@/store/editor/types";

export const mutations: MutationTree<Editor> = {
  NEW_HIGHLIGHTS(state, payload: HighlightRow[]) {
    state.highlights = payload;
  },
  UPDATE_HIGHLIGHTS_ROW_MIN(state, payload: { id: string; value: number }) {
    const highlightsRow: HighlightRow | undefined = state.highlights.find(
      (item) => item.id == payload.id
    );
    if (highlightsRow) {
      highlightsRow.min = payload.value;
    }
  },
  UPDATE_HIGHLIGHTS_ROW_SEC(state, payload: { id: string; value: number }) {
    const highlightsRow: HighlightRow | undefined = state.highlights.find(
      (item) => item.id == payload.id
    );
    if (highlightsRow) {
      highlightsRow.sec = payload.value;
    }
  },
  UPDATE_HIGHLIGHTS_ROW_TO_ADD(state, payload: { id: string; value: number }) {
    const highlightsRow: HighlightRow | undefined = state.highlights.find(
      (item) => item.id == payload.id
    );
    if (highlightsRow) {
      highlightsRow.toAdd = payload.value;
    }
  },
  NEW_ROW(state, editing) {
    const id = Math.floor(Math.random() * (10000 - 1 + 1)) + 1;
    state.highlights.push({
      min: null,
      sec: null,
      toAdd: null,
      id: id.toString(),
      editing: editing,
    });
  },
  DELETE_ROW(state, id: string) {
    state.highlights = state.highlights.filter((item) => {
      if (item.id != id) return item;
    });
  },
};
