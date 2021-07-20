import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { VueCookieNext } from "vue-cookie-next";

const app = createApp(App);
app.use(VueCookieNext);
VueCookieNext.config({ expire: "100d", sameSite: "" });
app.use(store).use(router).mount("#app");
