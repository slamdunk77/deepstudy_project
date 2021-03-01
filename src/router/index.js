/**
 * 配置路由器
 */
import Vue from 'vue'
import Router from 'vue-router'
import DeepMain from '../pages/DeepMain/DeepMain'
//全局注入路由插件
Vue.use(Router)

export default new Router({
  //配置路由器
  routes:[
    {
      path:'/deepMain',
      component:DeepMain
    },
    {
      path: '/',
      redirect:'deepMain'
    }
  ]
})
