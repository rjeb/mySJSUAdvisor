import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import store from '@/store.js';
import VueLocalStorage from 'vue-localstorage'

Vue.use(Router);
Vue.use(VueLocalStorage);


const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/form',
            name: 'form',
            component: () => import('./views/FormTemp.vue')
        }
    ]
});

export default router;
