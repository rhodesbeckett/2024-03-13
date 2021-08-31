import { VueCookieNext } from "vue-cookie-next";

const cookieData = { expire: "1500d", sameSite: "" };

export function COOKIE(): string {
  return VueCookieNext.getCookie("mcID");
}
export function SET_COOKIE(ID: string): void {
  if (ID) {
    VueCookieNext.setCookie("mcID", ID, cookieData);
  } else {
    VueCookieNext.setCookie("mcID", COOKIE(), cookieData);
  }
}
