<template>
    <el-container class="home">
        <el-header height="50px" class="header">
            <my-header></my-header>
        </el-header>
        <el-container class="main">
            <el-aside width="190px" class="nav">
                <left-bar></left-bar>
            </el-aside>
            <el-container>
                <el-header class="title" height="40px">
                    <my-bread-crump></my-bread-crump>
                </el-header>
                <el-main class="content">
                    <keep-alive>
                        <router-view></router-view>
                    </keep-alive>
                </el-main>
            </el-container>
        </el-container>
    </el-container>
</template>

<script>
import Header from '../components/Header.vue'
import LeftBar from '../components/LeftBar.vue'
import MyBreadCrump from '../components/MyBreadCrumb.vue'
export default {
    name:'Home',
    components:{
        MyHeader: Header,
        LeftBar,
        MyBreadCrump
    }
}
</script>

<style scoped>
   .home{
       width:100%;
       height:100%;
   }
   .home .header{
       background:#D3DCE6;
   }
    .home .main .content{
        background:#D3DCE6;
    }
</style>