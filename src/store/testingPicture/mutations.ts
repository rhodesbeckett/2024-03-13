import { MutationTree } from "vuex";
import { TestingPicture } from "@/store/testingPicture/types";

export const mutations: MutationTree<TestingPicture> = {
  UPDATE_PICTURE_MIN(state, payload: number) {
    state.testingPicture.pictureMin = payload;
  },
  UPDATE_PICTURE_SEC(state, payload: number) {
    state.testingPicture.pictureSec = payload;
  },
  UPDATE_PICTURE_SRC(state, payload: string) {
    state.testingPicture.pictureSrc = payload;
  },
};
