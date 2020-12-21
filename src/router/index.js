import Vue from 'vue'
import Router from 'vue-router'

import Browse from '../components/Browse'
import Contact from '../components/Contact'
import Home from '../components/Home'
import Help from '../components/Help'
import Docs from '../components/Docs'


Vue.use(Router);


const routes = [
    { path: '/', component: Home },
    { path: '/home', redirect: "/" },
    { path: '/browse', component: Browse },
    { path: '/contact', component: Contact },
    { path: '/help', component: Help },
    { path: '/docs', component: Docs },
      // Always leave this as last one,
      // but you can also remove it
    { path: '*',  component: () => import('../components/404.vue') }
];

const originalPush = Router.prototype.push;
   Router.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
};


const router = new Router({
    routes: routes,
});


window.router = router;

export default router

