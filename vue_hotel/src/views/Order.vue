<template>
  <div class="user">
    <el-card class="box-card">
      <el-row :gutter="20">
        <el-col :span="20">
          <el-button icon="el-icon-circle-plus-outline" type="primary" @click="addOrder" >添加订单</el-button>
          <el-button icon="el-icon-circle-plus-outline" type="primary" @click="getAllOrder">所有订单</el-button>
          <el-select placeholder="请选择订单状态" v-model="status" @change="chooseOrderStatus" class="selectStyle">
            <el-option v-for="item in orderStatus" :key="item" :label="item" :value="item"></el-option>
          </el-select>
        </el-col>
      </el-row>
        <el-table :data="orderList" border style="margin-top:20px">
            <el-table-column prop="orderNumber" label="订单号" align="center" width="100px"></el-table-column>
            <el-table-column prop="roomNumber" label="房间编号" align="center" width="50px"></el-table-column>
            <el-table-column prop="customerIdCard" label="身份证" align="center"></el-table-column>
            <el-table-column prop="orderStatus" label="订单状态" align="center"></el-table-column>
            <el-table-column prop="checkInTime" label="入住时间" align="center">
                <template slot-scope="scope">
                    <el-date-picker
                        disabled
                        v-model="scope.row.checkInTime"
                        type="date"
                        placeholder="入住时间">
                    </el-date-picker>
               </template>
            </el-table-column>
            <el-table-column prop="checkOutTime" label="退房时间" align="center">
                <template slot-scope="scope">
                    <el-date-picker
                        disabled
                        v-model="scope.row.checkOutTime"
                        type="date"
                        placeholder="退房时间">
                    </el-date-picker>
               </template>
            </el-table-column>
            <el-table-column label="操作" align="center" width="200px">
                <template slot-scope="scope">
                    <el-button type="primary" size="mini" @click="OpenEditOrder(scope.row)">编辑</el-button>
                    <el-button type="primary"  size="mini" v-if="scope.row.orderStatus=='未支付'" @click="finishOrder(scope.row)">完成</el-button>
                    <el-button type="danger" icon="el-icon-delete" size="mini" @click="delOrder(scope.row)"></el-button>
                </template>
            </el-table-column>
        </el-table>

         <el-dialog title="添加订单" :visible.sync="addOrderDialog" width="30%">
            <el-form
            :model="addOrderInfo"
            status-icon
            ref="addOrderInfo"
            label-width="100px"
            class="demo-ruleForm"
            >
                <el-form-item label="订单号" prop="orderNumber">
                    <el-input v-model="addOrderInfo.orderNumber" autocomplete="off" ></el-input>
                </el-form-item>
                 <el-form-item label="订单状态" prop="orderStatus">
                     <el-select v-model="addOrderInfo.orderStatus" placeholder="请选择订单状态">
                        <el-option v-for="item in orderStatus" :key="item" :label="item" :value="item"></el-option>
                    </el-select>
                </el-form-item>
                 <el-form-item label="身份证号" prop="customerIdCard">
                    <el-input v-model="addOrderInfo.customerIdCard" autocomplete="off" ></el-input>
                </el-form-item>
                <el-form-item label="房间号" prop="roomNumber">
                    <el-input v-model="addOrderInfo.roomNumber" autocomplete="off" ></el-input>
                </el-form-item>
                <el-form-item label="入住时间" prop="checkInTime">
                        <el-date-picker
                            v-model="addOrderInfo.checkInTime"
                            type="date"
                            placeholder="入住时间">
                        </el-date-picker>
                </el-form-item>
                <el-form-item label="退房时间" prop="checkOutTime">
                     <el-date-picker
                            v-model="addOrderInfo.checkOutTime"
                            type="date"
                            placeholder="退房时间">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="备注" prop="remarks">
                    <el-input v-model="addOrderInfo.remarks" autocomplete="off" ></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="cancelAddOrder">取 消</el-button>
                <el-button type="primary" @click="sureAddOrder">确 定</el-button>
            </span>
        </el-dialog>

        
      <el-dialog title="订单详情" :visible.sync="editOrderDialog" width="30%">
        <el-form
          :model="editOrderInfo"
          status-icon
          ref="editOrderInfo"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="订单号" prop="orderNumber">
            <el-input v-model="editOrderInfo.orderNumber" autocomplete="off" ></el-input>
          </el-form-item>
          <el-form-item label="房号" prop="roomNumber">
            <el-input v-model="editOrderInfo.roomNumber" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="房型" prop="type">
            <el-input v-model="editOrderInfo.room.type" autocomplete="off"></el-input>
          </el-form-item>
           <el-form-item label="入住时间" prop="type">
                <el-date-picker
                    v-model="editOrderInfo.checkInTime"
                    type="date"
                    placeholder="入住时间">
                </el-date-picker>
          </el-form-item>
          <el-form-item label="退房时间" prop="type">
              <el-date-picker
                    v-model="editOrderInfo.checkOutTime"
                    type="date"
                    placeholder="退房时间">
                </el-date-picker>
          </el-form-item>
          <el-form-item label="消费金额" prop="type">
            <el-input v-model="editOrderInfo.totalMoney" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="状态" prop="orderStatus">
            <el-select v-model="editOrderInfo.orderStatus" placeholder="请选择订单状态">
              <el-option v-for="item in orderStatus" :key="item" :label="item" :value="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="备注" prop="remarks">
            <el-input v-model="editOrderInfo.remarks" autocomplete="off" clearable ></el-input>
          </el-form-item>
           <el-form-item label="身份证" prop="customerIdCard">
            <el-input v-model="editOrderInfo.customerIdCard" autocomplete="off" clearable ></el-input>
          </el-form-item>
           <el-form-item label="姓名" prop="customer.customerName">
            <el-input v-model="editOrderInfo.customer.customerName" autocomplete="off" clearable  ></el-input>
          </el-form-item>
          <el-form-item label="性别" prop="customer.customerSex">
            <el-input v-model="editOrderInfo.customer.customerSex" autocomplete="off" clearable ></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="cancelEditOrder">取 消</el-button>
          <el-button type="primary" @click="sureEditOrder">确 定</el-button>
        </span>
      </el-dialog>

         <el-dialog title="提交订单页面" :visible.sync="finishOrderDialog" width="30%">
        <el-form
          :model="finishOrderInfo"
          status-icon
          ref="finishOrderInfo"
          label-width="100px"
          class="demo-ruleForm"
        >
            <el-form-item label="订单号" prop="orderNumber">
                <el-input v-model="finishOrderInfo.orderNumber" autocomplete="off" disabled></el-input>
            </el-form-item>
            <el-form-item label="房型" prop="type">
                <el-input v-model="finishOrderInfo.type" autocomplete="off" disabled></el-input>
            </el-form-item>
            <el-form-item label="房号" prop="roomNumber">
                <el-input v-model="finishOrderInfo.roomNumber" autocomplete="off" disabled></el-input>
            </el-form-item>
            <el-form-item label="身份证" prop="customerIdCard">
                <el-input v-model="finishOrderInfo.customerIdCard" autocomplete="off" disabled></el-input>
            </el-form-item>
            <el-form-item label="客户名" prop="customerName">
                <el-input v-model="finishOrderInfo.customerName" autocomplete="off" disabled></el-input>
            </el-form-item>
             <el-form-item label="入住时间" prop="checkInTime">
                <el-date-picker
                    v-model="finishOrderInfo.checkInTime"
                    type="date"
                    placeholder="入住时间">
                </el-date-picker>
            </el-form-item>
             <el-form-item label="完成时间" prop="checkOutTime">
                <el-date-picker
                    v-model="finishOrderInfo.checkOutTime"
                    type="date"
                    placeholder="完成时间">
                </el-date-picker>
            </el-form-item>
             <el-form-item label="订单状态" prop="orderStatus">
                <el-select v-model="finishOrderInfo.orderStatus" placeholder="请选择订单状态">
                    <el-option v-for="item in orderStatus" :key="item" :label="item" :value="item"></el-option>
                </el-select>
            </el-form-item>
             <el-form-item label="消费金额" prop="totalMoney">
                <el-input v-model="finishOrderInfo.totalMoney" autocomplete="off" ></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="cancalFinisgOrder">取 消</el-button>
          <el-button type="primary" @click="sureFinishOrder">确 定</el-button>
        </span>
      </el-dialog>

    </el-card>
    </div>
    
</template>

<script>
export default {
    name:'orderAdmin',
    data(){
        return {
            addOrderInfo:{//添加订单对话框中信息
                orderNumber:0,
                roomNumber:'',
                orderStatus:'',
                customerIdCard:'',
                checkInTime:'',
                checkOutTime:'',
                totalMoney:0,
                remarks:'' 
            },
            editOrderInfo:{//编辑订单对话框信息
                orderNumber: 0,
                orderStatus: '',
                customerIdCard: '',
                roomNumber: 0,
                checkInTime: '',
                checkOutTime: '',
                totalMoney: 150,
                remarks: '',
                orderTime: '',
                customer: {
                    customerName: '',
                    customerSex: '',
                    customerVipLevel:'',
                    totalAmount: 0
                },
                room: {
                    type: ''
                }
            },
            finishOrderInfo:{//完成订单对话框中信息
                orderNumber:'',
                roomNumber:'',
                type:'',
                totalMoney:0,
                customerIdCard:'',
                customerName:'',
                checkInTime:'',
                checkOutTime:'',
                orderStatus:''
            },
            finishOrderDialog:false,//完成订单对话框控制器
            addOrderDialog:false,//添加订单对话框控制器
            editOrderDialog:false,//编辑订单对话框控制器
            orderStatus:['已支付','未支付'],//订单状态
            orderList:[],//所有订单列表
            status:'',//
            count:0//订单数量
        }
    },
    methods:{
        cancalFinisgOrder:function(){
            this.finishOrderDialog = false;
            this.$refs.finishOrderInfo.resetFields();
        },
        sureFinishOrder:function(){
            this.finishOrderDialog = false;
            this.$axios.put('/order/update',this.finishOrderInfo)
            .then(res =>{
                if(res.data.success){
                    this.$message({
                        type:'success',
                        message:`${res.data.msg}`
                    });
                    this.finishOrderDialog = false;
                    this.$refs.finishOrderInfo.resetFields();
                    this.getAllOrder();
                }else{
                    this.$message({
                        type:'error',
                        message:`${res.data.msg}`
                    })
                }
            })
            .catch(err =>{
                this.$message({
                    type:'error',
                    message:'网络出错！'
                })
            })
        },
        finishOrder:function(scope){//完成订单
            this.finishOrderInfo.orderNumber = scope.orderNumber;
            this.finishOrderInfo.roomNumber = scope.roomNumber;
            this.finishOrderInfo.customerIdCard = scope.customerIdCard;
            this.finishOrderInfo.customerName = scope.customer.customerName;
            this.finishOrderInfo.checkInTime = scope.checkInTime;
            this.finishOrderInfo.checkOutTime = scope.checkOutTime;
            this.finishOrderInfo.totalMoney = scope.totalMoney;
            this.finishOrderInfo.orderStatus = scope.orderStatus;
            this.finishOrderInfo.type = scope.room.type;
            this.finishOrderDialog = true;
        },
        addOrder:function(){//打开添加订单对话框
            this.addOrderDialog = true;
            this.addOrderInfo.orderNumber = this.count + 1;
        },
        cancelAddOrder:function(){//取消订单对话框
            this.addOrderDialog = false;
            this.$refs.addOrderInfo.resetFields();
        },
        sureAddOrder:function(){//确认添加数据
            let empty = this.addOrderInfo.orderNumber==""|| this.addOrderInfo.orderStatus==""||
                        this.addOrderInfo.customerIdCard==""||this.addOrderInfo.roomNumber==""||
                        this.addOrderInfo.checkInTime==""||this.addOrderInfo.checkOutTime==""||
                        this.addOrderInfo.remarks=="";
            if(empty){
                this.$message({
                    type:'error',
                    message:'所填项不能为空!'
                })
            }else{
                this.$axios.post('/order/add',this.addOrderInfo)
                .then(res =>{
                    if(res.data.success){
                        this.$message({
                            type:'success',
                            message:`${res.data.msg}`
                        });
                        this.getAllOrder();
                        this.$refs.addOrderInfo.resetFields();
                        this.addOrderDialog = false;
                    }else{
                        this.$message({
                            type:'error',
                            message:`${res.data.msg}`
                        })
                    }
                })
                .catch(err =>{
                    this.$message({
                        type:'error',
                        message:'网络错误！'
                    })
                })
            }
        },
        delOrder:function(scope){//删除订单
            this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning",
            })
            .then(() => {
                this.$axios.delete('/order/del',{
                    data:{
                        orderNumber:scope.orderNumber
                    }
                })
                .then(res =>{
                    if(res.data.success){
                        this.$message({
                            type:'success',
                            message:`${res.data.msg}`
                        });
                        this.getAllOrder();
                    }else{
                        this.$message({
                            type:'error',
                            message:`${res.data.msg}`
                        })
                    }
                })
                .catch(err =>{
                    this.$message({
                        type:'error',
                        message:'网络错误！'
                    })
                })
            })
            .catch(() => {
                this.$message({
                    type: "info",
                    message: "已取消删除",
                });
            });
        },
        OpenEditOrder:function(scope){//查看订单详情
            this.editOrderDialog = true;
            this.editOrderInfo = scope;
        },
        cancelEditOrder:function(){//取消查看订单详情
            this.editOrderDialog = false;
            this.$refs.editOrderInfo.resetFields();
        },
        sureEditOrder:function(){//确定查看订单详情
            this.editOrderDialog = false;
        },
        chooseOrderStatus:function(item){//选择订单状态
            this.status = item;
            if(item==""){
                this.getAllOrder();
            }else{
                this.$axios.get('/order/getStatusOrder',{
                    params:{
                        orderStatus:this.status
                    }
                })
                .then(res =>{
                    if(res.data.success){
                        this.$message({
                            type:'success',
                            message:`${res.data.msg}`
                        });
                        this.orderList = res.data.orderList;
                        this.count = res.data.count;
                    }else{
                        this.$message({
                            type:'error',
                            message:`${res.data.msg}`
                        })
                    }
                })
                .catch(err =>{
                    this.$message({
                        type:'error',
                        message:'网络错误！'
                    })
                })
            }
        },
        getAllOrder:function(){//获取所有订单
            this.$axios.get('/order/getAllOrder',{
                params:{
                }
            })
            .then(res =>{
                if(res.data.success){
                    this.orderList = res.data.orderList;
                    this.count =  parseInt(res.data.orderList[res.data.orderList.length-1].orderNumber) ;
                    this.status = "";
                }else{
                    this.$message({
                        type:'error',
                        message:`${res.data.msg}`
                    })
                }
            })
            .catch(err =>{
                this.$message({
                    type:'error',
                    message:'网络错误！'
                })
            })
        }
    },
    mounted(){
        this.getAllOrder();
    }
}
</script>

<style scope>
    .selectStyle{
        margin-left: 20px;
    }
</style>