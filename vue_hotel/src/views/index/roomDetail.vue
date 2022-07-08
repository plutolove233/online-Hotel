<template>
    <div class="room-detail">
        <div class="room-detail-left">
            <img :src="curInfo.RoomPicUrl" alt="">
        </div>
        <div class="room-detail-right" v-if="curInfo">
            <p><span class="label">房间号：</span><span>{{curInfo.RoomNum}}</span></p>
            <p><span class="label">房间类型：</span><span>{{curInfo.RoomTypeName}}</span></p>
            <p><span class="label">面积：</span><span>{{curInfo.Square}}</span></p>
            <p><span class="label">楼层：</span><span>{{curInfo.Floor}}</span></p>
            <p><span class="label">窗户：</span><span>{{curInfo.WindowDescription}}</span></p>
            <p><span class="label">简介：</span><span>{{curInfo.RoomTypeBrief}}</span></p>
        </div>
    </div>
</template>
<script>
import * as Api from '@/request/api.js'

export default {
    data() {
        return {
            curInfo:{}
        }
    },
    mounted() {
        this.getInfo()
    },
    methods:{
        async getInfo() {
            const res = await Api.getRoomDetailInfo({'RoomID':this.$route.query.id})
            console.log(res.data)
            this.curInfo = res.data
        }
    }
}
</script> 
<style lang="less" scoped>
.room-detail{
    box-sizing: border-box;
    padding: 60px;
    display: flex;
    justify-content: center;
    .room-detail-left{
        width: 450px;
        img{
            width: 100%;
        }
    }
    .room-detail-right{
        width: 30vw;
        margin: 0 auto;
        border: 1px solid #ccc;
        box-shadow: 5px 5px 5px #ccc;
        padding: 20px;
        p{
            font-weight: bolder;
        }
    }
}
</style>