<template>
    <div class="head">
        <div class="btn">
            {{ HotelName }}
        </div>
        <div class="image">
            <el-avatar shape="square" :size="size" :src="squareUrl"></el-avatar>
        </div>
        <div class="btn">
            <el-button type="primary" @click="exit">退出</el-button>
        </div>
    </div>
</template>

<script>
export default {
    name:'MyAvatar',
    data(){
        return {
            squareUrl:require('../assets/images/undraw_decorative_friends_q2np.svg'),
            size:'large'
        }
    },
    computed: {
        adminName:function(){
            return this.$store.getters.getAdminInfo.HotelName;
        }
    },
    methods:{
        exit:function(){
            this.$store.dispatch('Exit')
            this.$router.push('/login')
        }
    }
}
</script>

<style scoped>
    .head{
        width:100%;
        height:100%;
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }
    .head div{
        height:100%;
        margin:10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .head .el-avatar{
        height:45px;
        width:45px;
    }
</style>