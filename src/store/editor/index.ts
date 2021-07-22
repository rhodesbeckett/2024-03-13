import { Module } from "vuex";
import { Editor } from '@/store/editor/types'
import { RootState } from "@/store/types";
import { getters } from "@/store/editor/getters";
import { mutations } from "@/store/editor/mutations";
import { actions } from "@/store/editor/actions";

const state: Editor = {highlights: []}
export const highlights: Module<Editor, RootState> = {
  state,
  getters,
  actions,
  mutations,
};
