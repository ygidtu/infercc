import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en';
import VueAspectRatio from "vue-aspect-ratio";

import App from './App.vue';
import router from './router'

import 'element-ui/lib/theme-chalk/index.css';


Vue.config.productionTip = false;
Vue.prototype.log = console.log;
Vue.use(VueAxios, axios);
Vue.use(ElementUI, { locale });


// register component to use
Vue.component("vue-aspect-ratio", VueAspectRatio);



new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
