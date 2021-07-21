import { MutationTree } from "vuex";
import { HighlightRow } from "@/store/highlights/types";
export const mutations: MutationTree<HighlightRow[]> = {

  NEW_HIGHLIGHTS(state, payload: HighlightRow[]) {
    for(const item of payload) {
      state.push(item)
    }
  },
  UPDATE_HIGHLIGHTS_ROW_MIN(state, payload: { id: string; value: number }) {
    const highlightsRow: HighlightRow | undefined = state.find(
      (item) => item.id == payload.id
    );
    if (highlightsRow) {
      highlightsRow.min = payload.value;
    }
  },
  UPDATE_HIGHLIGHTS_ROW_SEC(state, payload: { id: string; value: number }) {
    const highlightsRow: HighlightRow | undefined = state.find(
      (item) => item.id == payload.id
    );
    if (highlightsRow) {
      highlightsRow.sec = payload.value;
    }
  },
  UPDATE_HIGHLIGHTS_ROW_TO_ADD(state, payload: { id: string; value: number }) {
    const highlightsRow: HighlightRow | undefined = state.find(
      (item) => item.id == payload.id
    );
    if (highlightsRow) {
      highlightsRow.toAdd = payload.value;
    }
  },
  NEW_ROW(state, editing) {
    const id = Math.floor(Math.random() * (10000 - 1 + 1)) + 1;
    state.push({
      min: null,
      sec: null,
      toAdd: null,
      id: id.toString(),
      editing: editing,
    });
  },
DELETE_ROW(state,id:number) {
  console.log(state.length)
//    const a = state.filter( item => { if(item.id != id) return item })
    state.splice(id,1)
}
};
