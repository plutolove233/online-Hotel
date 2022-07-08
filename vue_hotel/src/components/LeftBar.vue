<template>
    <div class="bar">
        <el-menu default-active="1-4-1" class="el-menu-vertical-demo"  
            background-color="#545c64" text-color="#fff"
            active-text-color="#ffd04b" unique-opened  router>

            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-location"></i>
                    <span slot="title">房间管理</span>
                </template>
                <el-menu-item index="/home/room">基本房间信息管理</el-menu-item>
                <el-menu-item index="/home/roomtype">房间分类信息管理</el-menu-item>
            </el-submenu>

            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span slot="title">订单管理</span>
                </template>
                <el-menu-item index="/home/order">基本订单管理</el-menu-item>
            </el-submenu>

            <el-submenu index="3">
                <template slot="title">
                    <i class="el-icon-user-solid"></i>
                    <span slot="title">顾客管理</span>
                </template>
                <el-menu-item index="/home/customer">顾客信息管理</el-menu-item>
            </el-submenu>

            <!-- <el-submenu index="4">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span slot="title">运行错误页面</span>
                </template>
                <el-menu-item index="/home/notfound">404页面</el-menu-item>
                <el-menu-item index="/home/notoken">token失效页面</el-menu-item>
            </el-submenu> -->
        </el-menu>
    </div>
</template>

<script>
export default {
    name:'LeftBar',
    data(){
        return {
            isCollapse:false
        }
    }
}
</script>

<style scoped>
    .bar{
        width:100%;
        height:100%;
        background:#545c64;
    }
    .bar .el-radio-group{
        margin-top:20px;
        margin-left:20px;
        margin-bottom:20px;
    }
 
</style>