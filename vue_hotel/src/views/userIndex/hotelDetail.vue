<template>
    <div class="hotel-detail">
        <div class="detail-top"></div>
        <div class="detail-main" v-if="curDetail && curDetail.Remark">
            <span>{{curDetail.Hotel.HotelName}}</span>
            <span>联系电话{{curDetail.Hotel.Phone}}</span>
            <p>{{curDetail.Hotel.Address}}</p>
            <div class="detail-main-top">
                <div class="detail-main-top-left">
                    <img src="HotelPicUrl" alt="">
                </div>
                <div class="detail-main-top-right">
                    <h3>热评</h3>
                    <div class="pinglun-left">
                        <img :src="curDetail.Remark.FaceUrl" alt="">
                    </div>
                    <div class="pinglun-right">
                        <span>{{curDetail.Remark.RemarkContent}}</span>
                    </div>
                </div>
            </div>
            <h3>房间</h3>
            <div class="detail-main-bottom">
                <div v-for="(item,index) of curDetail.RoomType" :key="index" class="bottom-item">
                <div class="detail-main-bottom-left">
                    <div class="left-img">
                        <img :src="item.RoomPicUrl" alt="">
                    </div>
                    <div class="left-des">
                        <p>{{item.RoomTypeBrief}}</p>
                        <p>{{item.WindowDescription}}</p>
                        <p>{{item.Square}}分钟内免费取消</p>
                    </div>
                </div>
                <div class="detail-main-bottom-right">
                    <div class="right-left">
                        <p>{{item.Price}}元</p>
                        <p>还剩{{item.RemainRooms}}间</p>
                    </div>
                    <div class="right-right">
                        <el-button @click="orderRoom(item)">预定</el-button>
                    </div>
                </div>
            </div>
            </div>
        </div>
    </div>
</template>
<script>
import * as Api from '@/request/api.js'
export default {
    data() {
        return {
            curDetail:''
        }
    },
    mounted() {
        this.getHotelDetail()
    },
    methods:{
        async getHotelDetail() {
            const res = await Api.getHotelDetail({HotelID:this.$route.query.id})
            console.log(res)
            this.curDetail = res.data
        },
        async orderRoom(cur) {
            console.log(cur)
            this.$router.push({
                path:'orderMore',
                query:{
                    hotelId: cur.HotelID,
                    roomId:cur.RoomTypeID
                }
            }
            )
        }
    } 
}
</script>
<style lang="less" scoped>
.hotel-detail{
    .detail-top{
        height: 200px;
        background: url('https://img0.baidu.com/it/u=2905538548,1845295072&fm=253&fmt=auto&app=138&f=JPEG?w=709&h=500') no-repeat;
        background-size: 100% 100%;
    }
    .detail-main{
        width: 80vw;
        margin: 0 auto;
        .detail-main-top{
            display: flex;
            align-items: center;
            border: 1px solid #ccc;
            box-sizing: border-box;
            padding: 24px;
            border-radius: 8px;
            .detail-main-top-left{
                flex: 3;
                height: 150px;
                img{
                    width: 100%;
                    height: 100%;
                }
            }
            .detail-main-top-right{
                h3{
                    transform: translateY(-300%);
                }
                flex: 7;
                height: 150px;
                margin-left: 24px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                .pinglun-left{
                    flex: 2;
                    height: 150px;
                    img{
                    width: 100%;
                    height: 100%; 
                    }
                }
                .pinglun-right{
                    flex:8

                }
            }
        }
        .detail-main-bottom{
            border-radius: 8px;
            .bottom-item{
                box-sizing: border-box;
                padding: 24px;
                display: flex;
                border: 1px solid #ccc;
                align-items: center;
                justify-content: space-between;
                .detail-main-bottom-left{
                    width: 30%;
                    display: flex;
                    height: 100%;
                    .left-img{
                        width: 250px;
                        height: 100%;
                        img{
                            display: inline-block;
                            width: 100%;
                            height: 150px;
                        }
                    }
                    .left-des{
                        margin-left: 24px;
                        p{
                            font-weight: bolder;
                        }
                    }
                }
                .detail-main-bottom-right{
                    width: 20%;
                    display: flex;
                    align-items: center;
                    .right-left{
                        margin-right: 12PX;
                    }
                    /deep/.right-right{
                        .el-button{
                            background: orange;
                        }
                    }
                }
            }
        }
    }
}
</style>  