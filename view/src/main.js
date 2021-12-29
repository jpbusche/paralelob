import Vue from 'vue'
import Vuex from 'vuex'

import router from './routes'
import App from './App.vue'

Vue.config.productionTip = false
Vue.use(Vuex)

const store = new Vuex.Store({})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
