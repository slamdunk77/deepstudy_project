<!--
 * @FileDescription: 主页面，引用路由页面
 * @Author: 陈欣渝
 * @Date: 2020-08-22
 * @LastEditors: 陈欣渝
 * @LastEditTime: 2020-10-05
 -->
<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 30px;
  }
</style>
