import { Module } from "vuex";
import { mutations } from "../testingPicture/mutations";
import { getters } from "../testingPicture/getters";
import { RootState } from "../types";
import { TestingPicture } from "./types";
const state: TestingPicture = {
  testingPicture: {
    pictureMin: 0,
    pictureSec: 0,
    pictureSrc: "https://via.placeholder.com/600x300",
  },
};

export const testingPicture: Module<TestingPicture, RootState> = {
  state,
  mutations,
  getters,
};
