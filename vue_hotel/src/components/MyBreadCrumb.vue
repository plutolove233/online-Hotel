<template>
    <div class="bread">
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item v-for="item in path" :key="item.path" :to="item.path">{{ item.meta.title }}</el-breadcrumb-item>
        </el-breadcrumb>
    </div>
</template>

<script>
export default {
    name:'MyBreadCrump',
    data(){
        return {
            
        }
    },
    computed:{
        path:function(){
            return this.$store.getters.getPath;
        }
    }
}
</script>

<style scoped>
    .bread{
        width:100%;
        height:100%;
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }
</style>