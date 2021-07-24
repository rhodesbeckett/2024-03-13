import { VueCookieNext } from "vue-cookie-next";
export function COOKIE(): string | undefined {
  return VueCookieNext.getCookie("mcID");
}
export function SET_COOKIE(ID: string): void {
  VueCookieNext.setCookie("mcID", ID, { expire: "1500d", sameSite: "" });
}
