<template>
    <div class="user-main">
        <div class="main-top">
            <img src="" alt="">
        </div>
        <div class="main">
            <h3>用户订单信息</h3>
            <div class="user-order">
                <li v-for="(item,index) of orderList" :key="index">
                    <div class="left">
                        <div class="top">
                            {{ item.HotelName}}
                        </div>
                        <div class="bottom">
                            <div class="bottom-left">
                               <img :src="item.HotelPicUrl" alt="显示失败">
                            </div>
                            <div class="bottom-right">
                                <p>
                                    套房{{ item.totalCount}}间
                                </p>
                                <p>
                                    预计到店时间{{ item.ArrivalTime}}
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="right">
                        <p>
                            {{ item.price}}元
                        </p>
                        <p>
                            {{
                                item.OrderFormStatus == 1 ? '去评价':'待评价'
                            }}
                        </p>
                        <p @click="toOrderDetail(item)">
                            查看订单详情
                        </p>
                        <p  @click="toComment(item)">
                            {{
                                item.OrderFormStatus == 1 ? '取消订单':'去评价'
                            }}
                        </p>
                    </div>
                </li>
            </div>
        </div>
        <div class="footer">
            <el-button @click="toOrder">去预定</el-button>
        </div>


        
        <Dialog :dialogVisible="dialogVisible"
            @close="close" @confirm="confirm"
        >
        <h3>订单详情:{{curOrderInfo.OrderFormID}}</h3>
        <p>{{curOrderInfo && curOrderInfo.EACH_ROOM_INFO && curOrderInfo.EACH_ROOM_INFO.length}}间</p>
        <div class="order-item" v-for="(item,index) of curOrderInfo.EACH_ROOM_INFO" :key="index">
            <p><span class="label">住客姓名</span><span>{{item.GuestName}}</span></p>
            <p><span class="label">身份证</span><span>{{item.GuestID}}</span></p>
            <p><span class="label">房间号</span><span>{{item.RoomID}}</span></p>
        </div>
        <div class="dialog-footer">
            <p>预计到店时间{{curOrderInfo.ArrivalTime}}</p>
            <p>预计离店时间{{curOrderInfo.CheckOutTime}}</p>
        </div>
        <p>{{curOrderInfo.Price}}元</p>
        </Dialog>
    </div>
</template>
<script>
import * as Api from '@/request/api.js'
import Dialog from './dialog.vue'
export default {
    components:{
        Dialog
    },
    data() {
        return {
            orderList:[],
            dialogVisible:false,
            curOrderInfo:[]
        }
    },
    created() {
        this.getOrderList()
    },
    methods:{
        async getOrderList() {
            const res = await Api.getOrderByUser()
            console.log(res)
            if(res.code == 2000) {
                this.orderList = res.data
            }
        },
        toOrder() {
            this.$router.push({
                path:'order'
            })
        },
        async toOrderDetail(cur) {
            console.log(cur)
            this.dialogVisible = true
            const res = await Api.getOrderInfo({OrderFormID:cur.OrderFormID})
            console.log(res)
            this.curOrderInfo = res.data

        },
        close() {
            this.dialogVisible = false
        },
        confirm() {
            this.dialogVisible = false
        },
        toComment(cur) {
            console.log(cur)
            if(cur.OrderFormStatus == 2 ) {
                this.$router.push({
                    path:'comment',
                    query:{
                       id:cur.HotelID
                    }
                })
            } else {

            }
            // console.log(cur)
        }
    }
}
</script>
<style lang="less" scoped>
*{
    list-style: none;
}
.user-main{
        width: 50vw;
        margin: 0 auto;
    .main-top{
        height: 200px;
        background: url('https://img0.baidu.com/it/u=2905538548,1845295072&fm=253&fmt=auto&app=138&f=JPEG?w=709&h=500') no-repeat;
        background-size: 100% 100%;
    }
    .main{
        .user-order{
            li{
                box-sizing: border-box;
                border: 1px solid #ccc;
                padding: 24px;
                display: flex;
                justify-content: space-between;
                .left{
                    border-right: 1px solid #ccc;

                    .top{
                        height: 60px;
                        line-height: 60px;
                    }
                    .bottom{
                        height: 150px;
                        display: flex;
                        justify-content: space-evenly;
                        .bottom-left{
                            flex: 5;
                            img{
                                display: inline-block;
                                width: 100%;
                                height: 100%;
                            }
                        }
                        .bottom-right{
                            flex: 5;
                        }
                    }
                }
                .right{
                    p{
                        &:nth-child(1) {
                            color: orange;
                        }
                        &:nth-child(2) {
                            color: black;
                        }
                        &:nth-child(3) {
                            color: rgb(62, 84, 175);
                        }
                        &:nth-child(4) {
                            color: rgb(222, 57, 7);
                        }
                    }
                }
            }
        }
    }
    /deep/.el-dialog__wrapper{
        .el-dialog{
            .el-dialog__body{
                p{
                    text-align: right;
                }
                .order-item{
                    // display: flex;
                    // justify-content: center;
                    // align-items: center;
                    border: 1px solid #ccc;
                    margin-bottom: 12px;
                    p{
                        text-align: left;
                        margin-left: 50px;
                        .label{
                            display: inline-block;
                            width: 100px;
                        }
                    }
                }
            }
        }
    }
}
</style>