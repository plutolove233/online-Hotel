<template>
    <div class="order">
        <li v-for="(item,index) of hotelList" :key="index">
            <div class="left">
                <div class="left-img">
                    <img :src="item.HotelPicUrl" alt="加载失败">
                </div>
                <div class="left-des">
                    <p>{{item.HotelName}}</p>
                    <el-tag >{{item.HotelLabels || '空' }}</el-tag>
                </div>
            </div>
            <div class="right">
                <p>300-500</p>
                <p style="color:blue;cursor:pointer" @click="toDetail(item)">查看详情</p>
            </div>
        </li>
    </div>
</template>
<script>
import * as Api from '@/request/api.js'
export default {
    data() {
        return {
            hotelList: []
        }
    },
    mounted() {
        this.getHotel()
    },
    methods:{
        async getHotel() {
            const res = await Api.getHotel({
                Province:'北京市',
                City:'北京市',
                Area:'昌平区'
            })
            console.log(res)
            this.hotelList = res.data
        },
        toDetail(item) {
            this.$router.push({
                path:'hotelDetail',
                query:{
                    id: item.HotelID
                }
            })
        }
    }
}
</script>
<style lang="less">
ul,li{
    list-style: none;
}
.order{
    width: 50vw;
    margin: 0 auto;
    li{
        box-sizing: border-box;
        padding: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 200px;
        border: 1px solid #ccc;
        .left{
            flex:7;
            display: flex;
            // justify-content: space-between;
            align-items: center;
            margin-right: 24px;
            height: 100%;
            .left-img{
                width: 60%;
                height: 100%;
                img{
                    width: 100%;
                    height: 100%;
                }
            }
            border-right: 1px solid #ccc;
        }
        .right{
            flex: 3;
        }
    }
}
</style>