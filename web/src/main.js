import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import store from './store'

Vue.use(require('vue-cookies'))
Vue.use(require('vue-cookie'))

Vue.config.productionTip = false
Vue.config.devtools = true
Vue.use(VueRouter)

new Vue({
  router,
  store: store,
  render: h => h(App)
}).$mount('#app')
