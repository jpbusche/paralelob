import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './views/Login.vue'

Vue.use(VueRouter)
const routes = [
    {path: '/', name: 'Home', component: Login}
]
const router = new VueRouter({routes, mode: 'history'})
export default router