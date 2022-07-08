<template>
    <div class="header">
        <div class="left">
            <logo></logo>
        </div>
        <div class="right">
            <my-avatar></my-avatar>
        </div>
    </div>
</template>

<script>
import Logo from './Logo.vue'
import MyAvatar from './MyAvatar.vue'
export default {
    name:'Header',
    components:{
        Logo,
        MyAvatar
    }
}
</script>

<style scoped>
    .header{
        width:100%;
        height:100%;
        display: flex;
        align-items: center;
    }
    .header .left,
    .header .right{
        flex:1;
        height:100%;
    }
</style>