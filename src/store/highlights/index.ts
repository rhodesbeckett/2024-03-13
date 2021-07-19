import { Module } from "vuex";
import { HighlightRow } from "@/store/highlights/types";
import { RootState } from "@/store/types";
import { getters } from "@/store/highlights/getters";
import { mutations } from "@/store/highlights/mutations";
import { actions } from "@/store/highlights/actions";
const state: HighlightRow[] = [];
export const highlights: Module<HighlightRow[], RootState> = {
  state,
  getters,
  actions,
  mutations,
};
