import { NavigationGuardNext } from "vue-router";
import { COOKIE } from "@/plugins/cookie";

export function NEXT_PAGE(next: NavigationGuardNext): void {
  if (COOKIE() == "" || COOKIE() == null) {
    next("/");
  } else {
    next();
  }
}
