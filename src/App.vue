<template>
  <div id="app">
    <el-container :height="windowHeight">
      <el-header style="overflow: hidden; width: 100%; background-color: #545c64; height:60px">
        <el-row>
          <el-col :span="12"><h1 style="color: white; background-color: #545c64; padding-top: 15px">{{name}}</h1></el-col>
          <el-col :span="12">
            <el-menu
              default-active="/home"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              router mode="horizontal"
            >
              <el-menu-item index="/home">
                <i class="el-icon-s-home" />
                <span slot="title">Home</span>
              </el-menu-item>
              <el-menu-item index="/browse">
                <i class="el-icon-folder-opened" />
                <span slot="title">Web service</span>
              </el-menu-item>
              <el-menu-item index="/docs">
                <i class="el-icon-s-data" />
                <span slot="title">Statistics</span>
              </el-menu-item>
              <el-menu-item index="/contact">
                  <i class="el-icon-user" />
                  <span slot="title">Contact</span>
              </el-menu-item>
              <el-menu-item index="/help">
                <i class="el-icon-help" />
                <span slot="title">Help</span>
              </el-menu-item>
              <el-menu-item @click="open">
                <i class="el-icon-notebook-2" />
                <span slot="title">Github</span>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>

      </el-header>

      <el-container>
        <el-main id="main">
          <el-row type="flex" justify="center">
            <el-col :sm="24" :lg="20" :md="22">
              <router-view />
              <el-backtop target="#main" :visibility-height="100" />
            </el-col>
          </el-row>

        </el-main>
      </el-container>
      <el-footer>
          Sichuan University at Chengdu, Sichuan, China. - 蜀ICP备20009228号 - Copyright@2020
      </el-footer>
    </el-container>

  </div>
</template>

<script>
  import urls from "./utils/const";
    export default {
        data() {
            return {
                name: "Infer cell compositions",
                windowHeight: "600px",
            }
        },
        methods: {
          open() {
            window.location.replace("https://github.com/ygidtu/infercc")
          }
        },
        mounted() {
            this.height = window.innerHeight;
        }
    };
</script>

<style>
  html, body {
    height: 100%;
  }
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    display: flex;
    height: 100%;
    overflow-y: scroll;
  }

  .el-footer {
    font-size: 13px;
    text-align: right;
    align-items: center;
    background-color: #F2F6FC;
    line-height: 60px;
  }

  .el-menu--horizontal {float: right}

  * { margin:0; padding:0; }
</style>
