import { Store, StoreOptions } from "vuex";
import { compDesc } from "./matchInfo/index";
import { highlights } from "@/store/editor/index";
import { testing } from "@/store/testing/index";
import { testingPicture } from "@/store/testingPicture/index";
import { RootState } from "./types";

const store: StoreOptions<RootState> = {
  state: {
    version: "0.1.0",
    canCut: false,
    canRender: false,
    cutProgress: 0,
    renderProgress: 0,
  },
  modules: { compDesc, testing, highlights, testingPicture },
};

export default new Store<RootState>(store);
