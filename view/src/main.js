import Vue from 'vue'
import Vuex from 'vuex'
import FlashMessage from '@smartweb/vue-flash-message';

import router from './routes'
import App from './App.vue'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(FlashMessage)

const store = new Vuex.Store({
  state: {
    config: null,
    is_admin: false
  }
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
