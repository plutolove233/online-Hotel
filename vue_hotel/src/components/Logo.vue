<template>
    <div class="logo">
        <div class="image fa fa-home"></div>
        <div class="text">酒店管理系统</div>
    </div>
</template>

<script>
export default {
    naem:'Logo'
}
</script>

<style scoped>
    .logo{
        width:100%;
        height:100%;
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }
    .logo .image{
        width:50px;
        height:50px;
        font-size:40px;
        display: flex;
        justify-content: center;
        align-items: center;
        color:#409EFF;
    }
    .logo .text{
        font-size:18px;
        color:#409EFF;
    }
</style>