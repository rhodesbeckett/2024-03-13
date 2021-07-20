import { useRouter } from "vue-router";
import { SET_COOKIE } from "@/plugins/cookie";
import store from "@/store/index";

export default function useCompHelpers(page: string): any {
  const router = useRouter();

  function radioClick(halfTime: number, matchCompID: string) {
    setMatchID(matchCompID);
    setTimeout(() => {
      store.commit("UPDATE_IS_CHOSEN", true);
      if (halfTime == 1) {
        store.commit("UPDATE_EDITING", "firstHalf");
      } else {
        store.commit("UPDATE_EDITING", "secondHalf");
      }
      store.dispatch("setCompDesc", {
        showMessage: function () {
          return null;
        },
      });
    }, 1000);
  }
  function setMatchID(ID: string) {
    SET_COOKIE(ID);
    router.push("matchInfo");
  }
  return { radioClick, setMatchID };
}
