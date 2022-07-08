<template>
    <div class="check">
        <div class="search">
            <el-input v-model="OrderFormID"  placeholder="请输入订单号"></el-input>
            <span @click="search">搜索</span>
        </div>
        <div class="list">
            <li v-for="(item,index) of orderList" :key="index">
                <div class="left">
                    <img :src="item.FaceUrl" alt="">
                    <p>
                        <span>订单ID:{{item.OrderFormID}}</span>
                        <span>订单用户:{{item.UserName}}</span>
                        <span>电话号码:{{item.Phone}}</span>
                    </p>
                </div>
                <div class="right">
                    <span v-if="item.OrderFormStatus == 0" @click="ruzhu(item)">入住</span>
                    <span v-if="item.OrderFormStatus == 1" @click="cancel(item)">取消订单</span>
                    <span v-if="item.OrderFormStatus == 1" @click="tuifang(item)">退房</span>
                </div>
            </li>
        </div>
    </div>
</template>


<script>
import * as Api from '@/request/api.js'
export default {
    name:'check',
    data() {
        return {
            orderList:[],
            OrderFormID:null
        }
    },
    created() {
        this.$nextTick(() => {
            this.getOrder()
        })
    },
    methods:{
        async getOrder() {
            const res = await Api.getOrder({
                OrderFormID:this.OrderFormID
            })
            console.log(res)
            this.orderList = res.data
        },
        async search() {
            if(this.OrderFormID == ''){
                this.OrderFormID = null
            }
            this.getOrder()
        },
        async ruzhu(cur) {
            const res = await Api.checkin({OrderFormID:cur.OrderFormID})
            console.log(res)
            if(res.code == 2000) {
                 this.getOrder() 
            } else {
                this.$message.error('操作失败');
            }
        },
        async cancel(cur) {
            const res = await Api.cancelOrder({OrderFormID:cur.OrderFormID})
            console.log(res)
            if(res.code == 2000) {
                 this.getOrder() 
            } else {
                this.$message.error(res.message);
            }
        },
        async tuifang(cur) {
            const res = await Api.checkout({OrderFormID:cur.OrderFormID})
            console.log(res)
            console.log(res)
            if(res.code == 2000) {
                 this.getOrder() 
            } else {
                this.$message.error('操作失败');
            }
        },
    }
}
</script> 

<style lang="less" scoped>
.check{
    width: calc(100vw - 200px);
    box-sizing: border-box;
    padding: 200px;
    .search{
        height: 60px;
        width: 200px;
        display: flex;
        align-items: center;
        .el-input{
            width: 80%;
        }
        span{
            cursor: pointer;
        }
    }
    .list{
        border: 1px solid #ccc;
        box-sizing: border-box;
        padding: 24px;
        border-radius: 8px;
        ul,li{
            list-style: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px dashed #ccc;
            .left{
                display: flex;
                justify-content: space-between;
                align-items: center;
                img{
                    height: 40px;
                }
                p{
                    span{
                        margin-right: 24px;
                        &:nth-child(1){
                            font-weight: bolder;
                            color: black;
                        }
                    }
                }
            }
            .right{
                display: flex;
                justify-content: space-between;
                align-items: center;
                span{
                    color: blue;
                    margin-left: 24px;
                }
            }
        }
    }
}
</style>