import { GetterTree } from "vuex";
import { TestingPicture } from "@/store/testingPicture/types";
import { RootState } from "@/store/types";

export const getters: GetterTree<TestingPicture, RootState> = {
  pictureMin(state): number {
    return state.testingPicture.pictureMin;
  },

  pictureSec(state): number {
    return state.testingPicture.pictureSec;
  },

  pictureSrc(state): string {
    return state.testingPicture.pictureSrc;
  },
};
