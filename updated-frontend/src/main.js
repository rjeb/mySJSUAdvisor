import Vue from 'vue'
import VueI18n from 'vue-i18n'
import Vuelidate from 'vuelidate';
import VueRouter from "vue-router";
import App from './App.vue'
import translations from "./resources/translations";
import Form from './components/form/Form.vue';
import HelloWorld from './components/form/HelloWorld.vue';

Vue.use(VueI18n);
Vue.use(Vuelidate);
Vue.use(VueRouter);

Vue.config.formApiUrl = process.env.FORM_API_URL;

const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "./components/form/Form.vue",
      component: Form
    },
    {
      path: "./components/form/HelloWorld.vue",
      component: HelloWorld
    },
  ]
})
const i18n = new VueI18n({
  locale: 'en',
  fallbackLocale: 'en',
  messages: translations
})

new Vue({
  el: '#app',
  router,
  i18n,
  render: h => h(App)
})
