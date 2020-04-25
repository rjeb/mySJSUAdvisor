import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

Vue.use(Router);
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
            component: () => import('./views/Form.vue')
        },
        {
            path: '/schedules',
            name: 'schedules',
            component: () => import('./views/Schedules.vue')
        }
    ]
});

export default router;
