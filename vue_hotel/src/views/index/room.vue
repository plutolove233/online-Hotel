<template>
  <div class="room">
    <div class="top">
      <div class="filter-item">
        <div class="label">房间号</div>
        <el-input v-model="filterData.RoomNum"></el-input>
      </div>
      <div class="filter-item">
        <div class="label">房间状态</div>
        <el-select v-model="filterData.RoomStatus" @change="handleSelectRoomStatus">
          <el-option
            v-for="item in roomStatusList"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option
        ></el-select>
      </div>
      <div class="filter-item">
        <div class="label">房间类型</div>
        <el-select v-model="filterData.RoomTypeName" @change="handleSelectRoomType">
          <el-option
            v-for="item in roomTypeList"
            :key="item.AutoID"
            :label="item.RoomTypeBrief"
            :value="item.RoomTypeName"
          >
          </el-option
        ></el-select>
      </div>
      <div>
        <el-button type="primary" @click="search">搜索</el-button>
      </div>
    </div>
    <div class="bottom">
        <div class="roomItem" v-for="(item,index) of allRoom" :key="index" @click="handleDetail(item)">
            <p>{{ item.RoomNum}}</p>
            <p>房间类型:{{ item.RoomTypeName}}</p>
            <p>房间介绍:{{ item.RoomTypeBrief}}</p>
            <p>房间状态:{{ item.RoomStatus == 1 ? '空闲' : '占用'}}<el-tag v-if="item.RoomStatus == 1" @click.stop="order(item)">预定</el-tag></p>
        </div>
    </div>
  </div>
</template>
<script>
import * as Api from '@/request/api.js'
export default {
  data() {
    return {
      filterData: {
        RoomTypeName: null,
        RoomStatus: null,
        RoomNum:null,
      },
      roomTypeList:[],
      roomStatusList:[
        {
            label:'空闲',
            value:1
        },
        {
            label:'占用',
            value:0
        }
      ],
      allRoom:[]
    };
  },
  mounted() {
    this.getRoomTypeList()
    this.getALlRoom()
  },
  methods:{
    async getRoomTypeList() {
        const res = await Api.getRoomType()
        console.log(res)
        this.roomTypeList = res.data
    },
    handleSelectRoomType(e) {
        console.log(e)
        this.filterData.RoomTypeName = e
    },
    handleSelectRoomStatus(e) {
        this.filterData.RoomStatus = e
    },
    search() {
        console.log(this.filterData)
        this.getALlRoom()
    },
    async getALlRoom() {
        const res = await Api.getAllRoom(this.filterData)
        console.log(res)
        this.allRoom = res.data
    },
    order(cur) {
        console.log(cur)
        this.$router.push({
            path:'orderMore',
            query:{
                roomId:cur.RoomID
            }
        })
    },
    handleDetail(cur) {
        console.log(cur)
        this.$router.push({
            path:'roomDetail',
            query:{
                id:cur.RoomID
            }
        })
    }
  }
};
</script>
<style lang="less" scoped>
.room {
    width: 100%;
  .top {
    box-sizing: border-box;
    padding: 48px;
    /deep/.filter-item {
      display: flex;
      margin-bottom: 12px;
      .label {
        width: 100px;
      }
      .el-input {
        width: 200px;
      }
      .el-select {
        width: 200px;
        .el-input {
          width: 100%;
        }
      }
    }
  }
  .bottom{
    // border: 1px dashed #ccc;
    display: flex;
    flex-wrap: wrap;
    .roomItem{
        border-radius: 4px;
        width: 33%;
        border: 1px dashed #ccc;
        box-sizing: border-box;
        padding: 12px;
    }
  }
}
</style>