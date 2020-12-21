import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en';
import VueAspectRatio from "vue-aspect-ratio";

import ECharts from 'vue-echarts'; // refers to components/ECharts.vue in webpack

// import ECharts modules manually to reduce bundle size
import 'echarts/lib/chart/bar';

import 'echarts/lib/component/legend';
import 'echarts/lib/component/title';
import 'echarts/lib/component/toolbox';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/visualMap';

import App from './App.vue';
import router from './router'

import 'element-ui/lib/theme-chalk/index.css';

// import ECharts modules manually to reduce bundle size
import 'echarts/lib/chart/bar';
import 'echarts/lib/chart/line';
import 'echarts/lib/chart/scatter';

import 'echarts/lib/component/legend';
import 'echarts/lib/component/title';
import 'echarts/lib/component/toolbox';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/visualMap';
import 'echarts/lib/component/dataZoomSlider';

import 'zrender/lib/svg/svg';


Vue.config.productionTip = false;
Vue.prototype.log = console.log;
Vue.use(VueAxios, axios);
Vue.use(ElementUI);
Vue.use(ECharts);

// register component to use
Vue.component("vue-aspect-ratio", VueAspectRatio);
Vue.component('v-chart', ECharts);


new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
