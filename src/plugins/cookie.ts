import { VueCookieNext } from "vue-cookie-next";
export function COOKIE(): string {
  return VueCookieNext.getCookie("mcID");
}
export function SET_COOKIE(ID: string): void {
  if (ID) {
    VueCookieNext.setCookie("mcID", ID, { expire: "1500d", sameSite: "" });
  } else {
    VueCookieNext.setCookie("mcID", COOKIE(), {
      expire: "1500d",
      sameSite: "",
    });
  }
}
