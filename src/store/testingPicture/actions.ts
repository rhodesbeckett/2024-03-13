import { ActionTree } from "vuex";
import { RootState } from "@/store/types";
import { TestingPicture } from "@/store/testingPicture/types";
import GET from "@/plugins/axios";

export const actions: ActionTree<TestingPicture, RootState> = {
  getTestingPictureSrc({ commit, getters }) {
    const query = `getPhoto/${getters.pictureMin}/${getters.pictureSec}`;
    GET(query).then((res) => {
      commit("UPDATE_PICTURE_SRC", res.data.imgSrc);
    });
  },
};
