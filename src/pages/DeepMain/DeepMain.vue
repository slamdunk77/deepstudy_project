<!--
 * @FileDescription: 页面主体部分
 * @Author: 陈欣渝
 * @Date: 2020-08-22
 * @LastEditors: 陈欣渝
 * @LastEditTime: 2020-10-05
 -->

<template>
  <div>
    <!-- 引入头部组件 -->
    <DeepHeader />
    <el-divider></el-divider>
    <div class="main_wrap">
      <div class="main_left">
        <div class="box1">
          <img src="../img/img4.png" alt="">
        </div>
        <div class="box2">
          <img src="../img/img5.png" alt="">
        </div>
        <div class="box3">
          <img src="../img/img6.png" alt="">
        </div>
        <div class="box4">
          <img src="../img/img7.png" alt="">
        </div>
        <div class="box5">
          <img src="../img/img8.png" alt="">
        </div>
        <div class="box6">
          <img src="../img/img9.png" alt="">
        </div>
      </div>
      <div class="main_line"></div>
      <div class="main_right">
        <div class="swiper-container">
          <div class="swiper-wrapper">
            <div class="swiper-slide">
              <img src="../img/img1.png" alt="" style="width: 590px;border-radius: 10px">
            </div>
            <div class="swiper-slide">
              <img src="../img/img2.png" alt="" style="width: 600px;border-radius: 10px">
            </div>
            <div class="swiper-slide">
              <img src="../img/img3.png" alt="" style="width: 600px;border-radius: 10px">
            </div>
          </div>
          <!-- 如果需要分页器 -->
          <div class="swiper-pagination"></div>
        </div>
      </div>
    </div>
    <el-divider></el-divider>
    <div class="funcl_title">
      <span class="iconfont icon-qiye"></span>
      <span class="title">企业实体文字识别</span>
    </div>
    <div class="function_wrap">
      <div class="func_left">
        <div class="funcl_up_wrap">
          <div class="funcl_up1">
            <span class="iconfont icon-shangchuan2"></span>
            <span class="iconfont1">上传单张图片</span>
          </div>
          <div class="funcl_up2">
            <el-upload action="https://jsonplaceholder.typicode.com/posts/" list-type="picture-card" :limit="1"
             :before-upload="beforeUploadL" @click="handleBtn">
              <i slot="default" class="el-icon-plus avatar-uploader-icon"></i>
              <div slot="file" slot-scope="{file}">
                <img class="el-upload-list__item-thumbnail" :src="file.url" alt="">
                <span class="el-upload-list__item-actions">
                  <span class="el-upload-list__item-preview" @click="handlePictureCardPreview(file)">
                    <i class="el-icon-zoom-in"></i>
                  </span>
                </span>
              </div>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
          </div>
        </div>
        <el-divider></el-divider>
        <div class="funcl_up_wrap1">
          <div class="funcl_up1">
            <span class="iconfont icon-shangchuan2"></span>
            <span class="iconfont1">上传多张图片</span>
          </div>
          <div class="funcl_up2">
            <el-upload class="upload-demo" action="https://jsonplaceholder.typicode.com/posts/" multiple
              :file-list="fileList" :before-upload="beforeUploadM">
              <el-button size="small" type="primary" style="width: 120px;">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">只能上传zip文件</div>
            </el-upload>
          </div>
        </div>
      </div>
      <div class="func_right">
        <div class="funcr_title">
          <span class="iconfont icon-gongkaijieguo"></span>
          <span class="iconfont1">识别结果</span>
        </div>
        <el-divider></el-divider>
        <div class="funcr_res">
          <el-table v-loading="loading"
          element-loading-text="多图上传时可能需要几分钟，请耐心等待"
          element-loading-spinner="el-icon-loading"
          element-loading-background="rgba(0, 0, 0, 0.8)"
          v-loading.fullscreen="loading"
            :data="isL?pictures:tableData" height="250" border style="width:100%;text-align: center">
            <el-table-column prop="date" label="图片" width="250">
              <template slot-scope="scope">
                <span >{{ scope.row.name }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="name" label="企业" width="308">
              <template slot-scope="scope">
                <span>{{ scope.row.words[0] }}</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="excel_warp" style="margin-top: 40px">
          <el-link :href="downLoadUrl" :underline="false">
            <el-button type="primary" round>点击导出结果</el-button>
          </el-link>
        </div>
      </div>
    </div>
    <footer
      style=" background-color: #86B8E3; color: rgb(255, 255, 255); padding: 30px 50px;font-family:Consolas, 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', Monaco, 'Courier New', 'monospace';height: auto">
      <div style="display: flex; flex-direction: column; align-items: center;">
        <div style="margin: 12px 0;margin-bottom: 17px;">
          <table>
            <tr style="height: 35px;">
              <td>
<!--                <img src="../vab_img/logo.jpg.png" alt="logo" style="width: auto; height:35px;">-->
              </td>
              <td style="height: 35px;line-height: 35px;color: #014F91;font-weight: bold;font-size: 19px;letter-spacing: 1px">
                &nbsp;基于深度学习的企业实体识别
              </td>
            </tr>
          </table>
        </div>
        <div style="margin: 8px 0;">Copyright &copy;2020 by 你们的代码都不队
        </div>
        <div style="margin: 8px 0;">若本站收录内容无意侵犯了贵公司版权，请给网页底部微信或邮箱地址来信，我们会及时处理和回复，谢谢合作</div>
        <div style="margin: 8px 0;">Email：920855608@qq.com</div>
        <div style="width: 300px;height: 1px; background-color: #FFFFFF;margin-top: 20px;"></div>
        <div style="margin: 8px 0; margin-top: 13px;height: auto;">
          <a href="#" class="wechat">
            <div class="wechat-img iconfont icon-weixin" style="font-size: 28px;color: #ffffff">

<!--              <img src="//piccache.cnki.net/kdn/index/kns7/nimages/logo_wx.png" alt="微信" style="position: center">-->
            </div>
            <div style="border-radius: 10px; border-radius: 10px;color: #B2D0EE;">
              <img class="qrcode" src="../img/qrcode.jpg" alt="微信二维码">
            </div>
          </a>
        </div>

      </div>
    </footer>
  </div>
</template>

<script>
/**
 * 引入头部组件
 */
import DeepHeader from '../../components/DeepHeader'
/**
 * 轮播图
 */
import Swiper from 'swiper'
/**
 * 轮播图css文件
 */
import 'swiper/dist/css/swiper.min.css'
/**
 * 引入调用的接口函数
 */
import {reqUploadPicture,reqUploadZip} from '../../api'
export default {
  name: 'DeepMain',
  mounted () {
    /**
     * 创建轮播图对象，并设置相关属性
     */
    new Swiper('.swiper-container',{
     loop:true,
     // 设置分页器
     pagination: {
       el: '.swiper-pagination',//开启分页器
     },
     // 设置自动播放
     autoplay:{
       delay:2000,
       autoplayDisableOnInteraction: false
     }
   });
  },
  data() {
    return {
      dialogImageUrl: '', //上传图片的地址
      dialogVisible: false, //上传图片是否放大
      tableData: [], //识别文字和语义后输出在表格中的数组内容
      fileList: [], //上传的图片文件列表
      file:{}, //通过组件获取的图片文件对象
      picture:{}, //单张图片对象
      pictures:[], //多张图片对象
      isL:true, //用于判断是单图还是多图
      downLoadUrl:'', //导出表格地址
      loading: false //是否出现导出按钮
    }
  },
  methods: {
    /**
     * @description: 点击放大图片
     * @param {Object} file
     * @return void
     */
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },

    /**
     * @description: 获取并处理上传的单张图片文件
     * @param {Object} file
     * @return void
     */
    beforeUploadL(file){
      this.loading=true;
      this.picture=file
      this.isL=true
      setTimeout(async () => {
        //图片文件获取成功
        if(this.picture){
          let formData=new FormData()
          formData.append("picture",this.picture)
          const res=await reqUploadPicture(formData)
          //调用接口成功
          if(res.code===200){
            this.pictures.push(res.datas)
            this.downLoadUrl=res.excelUrl
            this.loading=false;
          }
          //调用接口出现错误
          else{
            this.$message({
              message: '服务器开了一点小差~',
              type: 'warning'
            });
            this.loading=false;
          }
        }
      },200)
    },

    /**
     * @description: 获取并处理上传的多张图片文件列表
     * @param {Object} file
     * @return void
     */
    beforeUploadM(file){
      this.loading=true;
      this.file=file
      this.isL=false
      //图片文件获取成功
      if(this.file){
        setTimeout(async () => {
          let formData=new FormData()
          formData.append("file",this.file)
          const res=await reqUploadZip(formData)
          //调用接口成功
          if(res.code===200){
            this.fileList=res.datas
            this.tableData=res.datas
            this.downLoadUrl=res.excelUrl
            this.loading=false;
          }
          //调用接口出现错误
          else{
            this.$message({
              message: '服务器开了一点小差~',
              type: 'warning'
            });
            this.loading=false;
          }
        },200)
      }
    },
  },
  components:{DeepHeader}
}
</script>

<style scoped rel="stylesheet">
  .main_wrap{
    /*background-color: #007aff;*/
    display: flex;
    justify-content: space-evenly;
  }
  .main_left{
    /*background-color: cornflowerblue;*/
    width: 370px;
    margin-top: 50px;
    margin-left: 30px;
    transform-style: preserve-3d;
    animation: my3d linear infinite 20s;
  }
  .main_line{
    width: 0.7px;
    height: 290px;
    margin-top: 40px;
    margin-left: 20px;
    background-color: lightsteelblue;
  }
  .main_right{
    /*background-color: lightsteelblue;*/
    width: 650px;
  }
  .main_left > div{
    width: 200px;
    height: 200px;
    /* 设置透明 */
    opacity:.8;
    /* 让图片重合到一起 */
    position: absolute;
  }
  .main_left img{
    height: 200px;
    vertical-align: top;
  }
  .main_left .box1{
    transform:rotateY(90deg) translateZ(-100px);
  }
  .main_left .box2{
    transform:rotateY(-90deg) translateZ(-100px);
  }
  .main_left .box3{
    transform:rotateX(90deg) translateZ(-100px);
  }
  .main_left .box4{
    transform:rotateX(-90deg) translateZ(-100px);
  }
  .main_left .box5{
    transform:rotateY(180deg) translateZ(100px);
  }
  .main_left .box6{
    transform:rotateY(0deg) translateZ(100px);
  }
  @keyframes my3d {
    from{
      transform: rotateX(0deg) rotateZ(0deg);
    }
    to{
      transform: rotateX(360deg) rotateZ(360deg);
    }
  }
  .function_wrap{
    /*background-color: #02a774;*/
    /*height: 400px;*/
    display: flex;
    justify-content: space-evenly;
    margin: 40px auto 100px;
  }
  .function_wrap .func_left{
    width: 500px;
    /*background-color: #42b983;*/
    padding-top: 80px;
    padding-left: 20px;
    /*border: lightblue 3px solid;*/
    margin-top: 20px;
    border-radius: 20px;
  }
  .function_wrap .func_right{
    width: 560px;
    /*background-color: lightgray;*/
  }
  /*.avatar-uploader-icon {*/
  /*  font-size: 28px;*/
  /*  color: #8c939d;*/
  /*  width: 178px;*/
  /*  height: 178px;*/
  /*  line-height: 168px;*/
  /*  text-align: center;*/
  /*  !*background-color: slateblue;*!*/
  /*}*/
  .swiper-container{
    width: 100%;
    height: 100%;
    /*border-radius: 10px;*/
  }
  .swiper-wrapper{
    width: 100%;
    height: 100%;
  }
  .funcl_title{
    /*background-color: yellowgreen;*/
    margin-top: 60px;
    padding-bottom: 30px;
    padding-top: 10px;
  }
  .funcl_title .iconfont{
    font-size: 25px;
    font-weight: bold;
    color: lightsteelblue;
    letter-spacing: 1px;
  }
  .funcl_title .title{
    font-size: 23px;
    font-weight: bold;
    color: lightsteelblue;
    letter-spacing: 1px;
  }
  .function_wrap .funcl_up_wrap,.function_wrap .funcl_up_wrap1{
    /*background-color: bisque;*/
    display: flex;
    justify-content: space-evenly;
    margin-bottom: 20px;
  }
  .function_wrap .funcl_up_wrap .funcl_up1,.function_wrap .funcl_up_wrap1 .funcl_up1{
    width: 180px;
    /*background-color: blueviolet;*/
    margin-right: 20px;
  }
  .funcl_up_wrap .funcl_up1 .iconfont{
    font-size: 19px;
    font-weight: bold;
    color: cornflowerblue;
  }
  .funcl_up_wrap1 .funcl_up1 .iconfont{
    font-size: 19px;
    font-weight: bold;
    color: slateblue;
  }
  .funcl_up_wrap .funcl_up1 .iconfont1,.funcl_up_wrap1 .funcl_up1 .iconfont1{
    font-size: 15px;
    color: darkslateblue;
    letter-spacing: .7px;
  }
  .function_wrap .funcl_up_wrap .funcl_up2,.function_wrap .funcl_up_wrap1 .funcl_up2{
    width: 360px;
    /*background-color: orange;*/
    /*text-align: left;*/
  }
  .func_right .funcr_title{
    padding-top: 10px;
  }
  .func_right .funcr_title .iconfont{
    font-size: 22px;
    font-weight: bold;
    color: #67C23A;
  }
  .func_right .funcr_title .iconfont1{
    font-size: 18px;
    font-weight: bold;
    color: dimgray;
  }


  .wechat:hover .qrcode {
    width: 120px;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 0 15px;
    background-color: slateblue;
    margin-top: 10px;
  }

  .qrcode {
    width: 0;
  }

  /*.wechat:hover .wechat-img {*/
  /*  padding-left: 40px;*/
  /*}*/
</style>
