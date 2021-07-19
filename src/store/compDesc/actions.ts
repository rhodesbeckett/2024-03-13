import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { CompDescState } from "./types";

export const actions: ActionTree<CompDescState, RootState> = {
  getTitle(): string {
    return "test";
  },
  getCompDesc(): string {
    return "test";
  },
};
