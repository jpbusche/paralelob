import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './views/Login.vue'
import Index from './views/Index.vue'

Vue.use(VueRouter)
const routes = [
    {path: '/', name: 'Home', component: Login},
    {path: '/index', name: 'Index', component: Index},
]
const router = new VueRouter({routes, mode: 'history'})
export default router