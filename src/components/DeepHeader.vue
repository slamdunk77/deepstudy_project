<!--
 * @FileDescription: 页面头部组件
 * @Author: 陈欣渝
 * @Date: 2020-08-22
 * @LastEditors: 陈欣渝
 * @LastEditTime: 2020-10-05
 -->

<template>
  <div class="header_wrap">
    <div class="back">
      <i class="iconfont icon-wenzishibie___"></i>
      <span>基于深度学习的企业实体识别</span>
    </div>
    <div class="project"></div>
    <div class="trick">
      <el-link type="primary" class="act_login" :underline="false">欢迎来到文字识别的世界</el-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DeepHeader'
}
</script>

<style scoped rel="stylesheet">
.header_wrap{
  /*background-color: #02a774;*/
  display: flex;
  width: 95%;
  margin: 0 auto;

}
.iconfont{
  font-size: 28px;
  font-weight: bolder;
  color: cornflowerblue;
}
.back{
  flex-grow:0.5;
  line-height: 30px;
  font-size: 20px;
  text-align: center;
  /*background-color: lightsteelblue;*/
  letter-spacing: 1px;
  color: #7e8c8d;
}
.back span{
  font-size: 25px;
  font-weight: bold;
}
.project {
  flex-grow:3;
  font-size: 33px;
  font-weight: bolder;
  letter-spacing: 3px;
  text-align: left;
  /*background-color: #02a774;*/
}
.trick{
  flex-grow:0.5;
  /*background-color: #02a774;*/
  padding-top:8px ;
}
.act_login{
  font-size: 17px;
  letter-spacing: 1px;
}
</style>
