import { Store, StoreOptions } from "vuex";
import { compDesc } from "./matchInfo/index";
import { highlights } from "@/store/editor/index";
import { testing } from "@/store/testing/index";
import { testingPicture } from "@/store/testingPicture/index";
import { cutAndRender } from "@/store/cutAndRender/index";

import { RootState } from "./types";

const store: StoreOptions<RootState> = {
  state: {
    version: "0.1.0",
  },
  modules: { compDesc, testing, highlights, testingPicture, cutAndRender },
};

export default new Store<RootState>(store);
