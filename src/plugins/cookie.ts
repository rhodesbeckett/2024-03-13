import { VueCookieNext } from "vue-cookie-next";
export function COOKIE() {
  return VueCookieNext.getCookie("mcID");
}
export function SET_COOKIE(ID: string) {
  VueCookieNext.setCookie("mcID", ID, { expire: "1500d", sameSite: "" });
}
