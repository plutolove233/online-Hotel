<template>
  <div class="user">
    <el-card class="box-card">
      <el-row :gutter="20">
        <el-col :span="20">
          <el-button icon="el-icon-circle-plus-outline" type="primary" @click="openAddRoom">添加房间</el-button>
          <el-button icon="el-icon-circle-plus-outline" type="primary" @click="getAllRoom">所有房间</el-button>
          <el-select v-model="type" placeholder="请选择房型" @change="chooseRoomType" style="margin-left:20px">
            <el-option v-for="item in roomTypeList" :key="item" :label="item" :value="item"></el-option>
          </el-select>
          <el-select placeholder="请选择房间状态" @change="chooseRoomStatus" class="selectStyle">
            <el-option v-for="item in roomStatus" :key="item" :label="item" :value="item"></el-option>
          </el-select>
        </el-col>
       
      </el-row>
      <el-table :data="roomList" border style="width: 100%">
        <el-table-column prop="roomNumber" label="房间号" align="center" width="50px"></el-table-column>
        <el-table-column prop="type" label="房型" align="center" width="100px"></el-table-column>
        <el-table-column prop="roomStatus" label="房间状态" align="center" width="100px"></el-table-column>
        <el-table-column prop="remarks" label="备注信息" align="center"></el-table-column>
        <el-table-column prop="roomType.price" label="房价" align="center" width="100px"></el-table-column>
        <el-table-column label="操作" align="center">
          <template slot-scope="scope">
            <el-button
              type="info"
              icon="el-icon-more"
              size="mini"
              @click="openEditRoom(scope.row)"
            >修改</el-button>
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="delRoom(scope.row)"
            >删除</el-button>
            <el-button
              type="success"
              icon="el-icon-s-home"
              size="mini"
              v-if="scope.row.roomStatus=='未入住'"
              @click="addOrder(scope.row)"
            >入住</el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-dialog title="添加房间" :visible.sync="addRoomDialog" width="25%">
        <el-form
          :model="addRoomInfo"
          status-icon
          :rules="addRoomRules"
          ref="addRoomInfo"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="房间号" prop="roomNumber">
            <el-input v-model="addRoomInfo.roomNumber" autocomplete="off" clearable></el-input>
          </el-form-item>
          <el-form-item label="房型" prop="type">
            <el-select v-model="addRoomInfo.type" placeholder="请选择">
              <el-option v-for="item in roomTypeList" :key="item" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="房间状态" prop="roomStatus">
            <el-select v-model="addRoomInfo.roomStatus" placeholder="请选择">
              <el-option v-for="item in roomStatus" :key="item" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="备注" prop="remarks">
            <el-input v-model="addRoomInfo.remarks" autocomplete="off" clearable></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="cancelAddRoom">取 消</el-button>
          <el-button type="primary" @click="sureAddRoom">确 定</el-button>
        </span>
      </el-dialog>

      <el-dialog title="编辑房型" :visible.sync="editRoomDialog" width="30%">
        <el-form
          :model="editRoomInfo"
          status-icon
          :rules="addRoomRules"
          ref="editRoomInfo"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="房号" prop="roomNumber">
            <el-input v-model="editRoomInfo.roomNumber" autocomplete="off" disabled></el-input>
          </el-form-item>
          <el-form-item label="房型" prop="type">
            <el-select v-model="editRoomInfo.type" placeholder="请选择">
              <el-option v-for="item in roomTypeList" :key="item" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="状态" prop="roomStatus">
            <el-select v-model="editRoomInfo.roomStatus" placeholder="请选择">
              <el-option v-for="item in roomStatus" :key="item" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="备注" prop="remarks">
            <el-input v-model="editRoomInfo.remarks" autocomplete="off" clearable></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="cancelEditRoom">取 消</el-button>
          <el-button type="primary" @click="sureEditRoom">确 定</el-button>
        </span>
      </el-dialog>

      <el-dialog title="顾客入住" :visible.sync="addOrderDialog" width="30%">
        <el-form
          :model="addOrderInfo"
          status-icon
          ref="addOrderInfo"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="订单号" prop="orderNumber">
            <el-input v-model="addOrderInfo.orderNumber" autocomplete="off" disabled></el-input>
          </el-form-item>
          <el-form-item label="订单状态" prop="orderStatus">
            <el-select v-model="addOrderInfo.orderStatus" placeholder="请选择订单状态">
              <el-option v-for="item in orderStatus" :key="item" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="身份证号" prop="customerIdCard">
            <el-input v-model="addOrderInfo.customerIdCard" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="房间号" prop="roomNumber">
            <el-input v-model="addOrderInfo.roomNumber" autocomplete="off" disabled></el-input>
          </el-form-item>
          <el-form-item label="入住时间" prop="checkInTime">
              <el-date-picker
                  v-model="addOrderInfo.checkInTime"
                  type="date"
                  placeholder="入住时间">
              </el-date-picker>
            <!-- <el-input v-model="addOrderInfo.checkInTime" autocomplete="off"></el-input> -->
          </el-form-item>
          <el-form-item label="退房时间" prop="checkOutTime">
              <el-date-picker
                  v-model="addOrderInfo.checkOutTime"
                  type="date"
                  placeholder="退房时间">
              </el-date-picker>
            <!-- <el-input v-model="addOrderInfo.checkOutTime" autocomplete="off"></el-input> -->
          </el-form-item>
          <el-form-item label="备注" prop="remarks">
            <el-input v-model="addOrderInfo.remarks" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="cancelAddOrder">取 消</el-button>
          <el-button type="primary" @click="sureAddOrder">确 定</el-button>
        </span>
      </el-dialog>
    </el-card>
  </div>
</template>


<script>
export default {
  name: "roomAdmin",
  data() {
    return {
      addOrderInfo: {
        orderNumber: 0,
        roomNumber: "",
        orderStatus: "未支付",
        customerIdCard: "",
        checkInTime: "",
        checkOutTime: "",
        totalMoney: 0,
        remarks: "",
      },
      orderStatus: ["已支付", "未支付"],
      addOrderDialog: false,//添加订单对话框控制器
      editRoomDialog: false, //编辑房间信息对话框控制器
      addRoomDialog: false, //添加房间信息对话框控制器
      roomList: [], //房间信息列表
      roomTypeList: [], //房型列表
      count: 0, //房间数量
      type: "", //当前房型
      roomStatus: ["已入住", "未入住"], //房间状态
      editRoomInfo: {
        //编辑房间信息
        roomNumber: "",
        type: "",
        roomStatus: "",
        remarks: "",
      },
      addRoomInfo: {
        //添加房间信息
        roomNumber: "",
        type: "",
        roomStatus: "",
        remarks: "",
      },
      addRoomRules: {
        //添加房型规则
        roomNumber: [
          { required: true, message: "请输入房间类型", trigger: "blur" },
        ],
        type: [{ required: true, message: "请输入房间价格", trigger: "blur" }],
        roomStatus: [
          { required: true, message: "请输入描述", trigger: "blur" },
        ],
        remarks: [
          { required: true, message: "请输入备注信息", trigger: "blur" },
        ],
      }
    }
  },
  methods: {
    checkOUtHome:function(scope){//退房

    },
    addOrder: function (scope) {  //打开添加订单对话框
      this.addOrderDialog = true;
      this.addOrderInfo.roomNumber = scope.roomNumber;
    },
    cancelAddOrder: function () { //取消订单对话框
      this.addOrderDialog = false;
      this.$refs.addOrderInfo.resetFields();
    },
    sureAddOrder: function () { //确认添加数据
      let empty =
        this.addOrderInfo.orderStatus == "" ||
        this.addOrderInfo.customerIdCard == "" ||
        this.addOrderInfo.roomNumber == "" ||
        this.addOrderInfo.checkInTime == "" ||
        this.addOrderInfo.checkOutTime == "" ||
        this.addOrderInfo.remarks == "";
      if (empty) {
        this.$message({
          type: "error",
          message: "所填项不能为空!",
        });
      } else {
        this.$axios
          .post("/order/add", this.addOrderInfo)
          .then((res) => {
            if (res.data.success) {
              this.$message({
                type: "success",
                message: `${res.data.msg}`,
              });
              this.getAllOrder();
              this.getAllRoom();
              this.getAllRoomType();
              this.$refs.addOrderInfo.resetFields();
              this.addOrderDialog = false;
            } else {
              this.$message({
                type: "error",
                message: `${res.data.msg}`,
              });
            }
          })
          .catch((err) => {
            this.$message({
              type: "error",
              message: "网络错误！",
            });
          });
      }
    },
    delRoom: function (scope) {//删除房间
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$axios
            .delete("/room/del", {
              data: {
                roomNumber: scope.roomNumber,
              },
            })
            .then((res) => {
              if (res.data.success) {
                this.$message({
                  type: "success",
                  message: `${res.data.msg}`,
                });
                this.getAllRoom();
              } else {
                this.$message({
                  type: "error",
                  message: `${res.data.msg}`,
                });
              }
            })
            .catch((err) => {
              this.$message({
                type: "error",
                message: `${res.data.msg}`,
              });
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
    cancelEditRoom: function () {//取消编辑对话框
      this.editRoomDialog = false;
      this.$refs.editRoomInfo.resetFields();
    },
    sureEditRoom: function () {//确定编辑对话框
      let empty =
        this.editRoomInfo.roomNumber == "" ||
        this.editRoomInfo.type == "" ||
        this.editRoomInfo.roomStatus == "" ||
        this.editRoomInfo.remarks == "";
      if (empty) {
        this.$message({
          type: "error",
          message: "修改项不能为空！",
        });
      } else {
        this.$axios
          .put("/room/update", this.editRoomInfo)
          .then((res) => {
            if (res.data.success) {
              this.$message({
                type: "success",
                message: `${res.data.msg}`,
              });
              this.getAllRoom();
              this.editRoomDialog = false;
            } else {
              this.$message({
                type: "error",
                message: `${res.data.msg}`,
              });
            }
          })
          .catch((err) => {
            this.$message({
              type: "error",
              message: "网络错误！",
            });
          });
      }
    },
    openEditRoom: function (scope) {//打开编辑房间对话框
      this.editRoomDialog = true;
      this.editRoomInfo.roomNumber = scope.roomNumber;
      this.editRoomInfo.type = scope.type;
      this.editRoomInfo.roomStatus = scope.roomStatus;
      this.editRoomInfo.remarks = scope.remarks;
    },
    chooseRoomStatus: function (status) {//请求房间状态信息
      if (status == "") {
        this.getAllRoom();
      } else {
        this.$axios
          .get("/room/getAllStatusRoom", {
            params: {
              roomStatus: status,
            },
          })
          .then((res) => {
            if (res.data.success) {
              this.$message({
                type: "success",
                message: `${res.data.msg}`,
              });
              this.roomList = res.data.roomList;
              this.count = res.data.count;
            } else {
              this.$message({
                type: "error",
                message: `${res.data.msg}`,
              });
            }
          })
          .catch((err) => {
            this.$message({
              type: "error",
              message: "网络错误！",
            });
          });
      }
    },
    chooseRoomType: function (roomtype) {//选择房间类型
      this.type = roomtype;
      if (this.type == "") {
        this.getAllRoom();
      } else {
        this.$axios
          .get("/room/getAllRoomTypePrice", {
            params: {
              type: this.type,
            },
          })
          .then((res) => {
            if (res.data.success) {
              console.log(res.data.roomList);
              this.$message({
                type: "success",
                message: `${res.data.msg}`,
              });
              this.roomList = res.data.roomList;
              this.count = res.data.count;
            } else {
              this.$message({
                type: "error",
                message: `${res.data.msg}`,
              });
            }
          })
          .catch((err) => {
            this.$message({
              type: "error",
              message: "网络错误！",
            });
          });
      }
    },
    openAddRoom: function () { //打开添加房价对话框
      this.addRoomDialog = true;
    },
    cancelAddRoom: function () {//取消添加房间
      this.addRoomDialog = false;
      this.$refs.addRoomInfo.resetFields();
    },
    sureAddRoom: function () {//确定添加房间
      this.addRoomDialog = false;
      let empty =
        this.addRoomInfo.roomNumber == "" ||
        this.addRoomInfo.type == "" ||
        this.addRoomInfo.roomStatus == "" ||
        this.addRoomInfo.remarks == "";
      if (empty) {
        this.$message({
          type: "error",
          message: "添加房间信息不能为空！",
        });
      } else {
        this.$axios
          .post("/room/add", this.addRoomInfo)
          .then((res) => {
            if (res.data.success) {
              this.$message({
                type: "success",
                message: `${res.data.msg}`,
              });
              this.getAllRoom();
              this.$refs.addRoomInfo.resetFields();
            } else {
              this.$message({
                type: "error",
                message: `${res.data.msg}`,
              });
            }
          })
          .catch((err) => {
            this.$message({
              type: "error",
              message: "网络错误！",
            });
          });
      }
    },
    getAllRoom: function () {  //查询所有房间信息
      this.$axios
        .get("/room/getAllRoomPrice", {
          params: {},
        })
        .then((res) => {
          if (res.data.success) {
            this.roomList = res.data.roomList;
            this.count = res.data.count;
            // this.$message({
            //   type: "success",
            //   message: `${res.data.msg}`,
            // });
          } else {
            this.$message({
              type: "error",
              message: `${res.data.msg}`,
            });
          }
        })
        .catch((err) => {
          // this.$message({
          //   type: "warning",
          //   message: "网络出错！",
          // });
        });
    },
    getAllRoomType: function () { //查询所有房屋类型信息
      this.$axios
        .get("/roomtype/getAllTypes", {
          params: {},
        })
        .then((res) => {
          if (res.data.success) {
            // this.$message({
            //   type: "success",
            //   message: `${res.data.msg}`,
            // });
            this.roomTypeList = res.data.typeList;
          } else {
            this.$message({
              type: "error",
              message: `${res.data.msg}`,
            });
          }
        })
        .catch((err) => {
          // this.$message({
          //   type: "error",
          //   message: "网络错误！",
          // });
        });
    },
    getAllOrder: function () {//获取所有订单
      this.$axios
        .get("/order/getAllOrder", {
          params: {},
        })
        .then((res) => {
          if (res.data.success) {
            this.addOrderInfo.orderNumber = parseInt(res.data.orderList[res.data.orderList.length-1].orderNumber) + 1;
          } else {
            this.$message({
              type: "error",
              message: `${res.data.msg}`,
            });
          }
        })
        .catch((err) => {
          this.$message({
            type: "error",
            message: "网络错误！",
          });
        });
    },
  },
  mounted() {
    this.getAllRoom();
    this.getAllRoomType();
    this.getAllOrder();
  },
};
</script>

<style scope>
.user {
  width: 100%;
  height: 100%;
  overflow-y: auto;
}
.user .el-table {
  margin-top: 20px;
}
.user .el-card .el-pagination {
  margin-top: 20px;
}
.selectStyle {
  margin-left: 20px;
}
</style>