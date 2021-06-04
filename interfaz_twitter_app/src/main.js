// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import HelloWorld from './components/HelloWorld'
import SideBar from './components/SideBar'
import AdministrarUsuarios from './components/AdministrarUsuarios'
import Tweets from './components/Tweets'
import CrearUsuario from './components/CrearUsuario'
import TweetTopic from './components/TweetTopic'
import Auditorias from './components/Auditorias'
import Estadisticas from './components/Estadisticas'

import VueResource from 'vue-resource'
Vue.use(VueResource);

import VueRouter from 'vue-router'
Vue.use(VueRouter);

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

const router = new VueRouter ({
  mode: 'history',
  base: __dirname ,
  routes: [
    { path: '/', component: HelloWorld },
    { path: '/administrar_usuarios', component: AdministrarUsuarios },
    { path: '/tweets', component: Tweets },
    { path: '/crear_usuario', component: CrearUsuario },
    { path: '/buscar_tweets', component: TweetTopic },
    { path: '/historial', component: Auditorias },
    { path: '/estadisticas', component: Estadisticas }
  ]
});

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  router,
  components: { App },
  template: '<App/>'
}).$mount('#app')
