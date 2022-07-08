<template>
    <div class="user">
        <el-card class="box-card">
            <el-row :gutter="20">
                <el-col :span="10">
                <el-input placeholder="请输入内容" clearable  v-model="queryName"  
                    @clear="getAllCustomer" @input="query">
                    <el-button slot="append" type="primary" 
                        icon="el-icon-search" @click="query">搜索</el-button>
                </el-input>
                </el-col>
                <el-col :span="10">
                    <el-button icon="el-icon-circle-plus-outline" type="primary" @click="openAddCustomer">新增顾客</el-button>
                    <el-button icon="el-icon-circle-plus-outline" type="primary" @click="getAllCustomer">所有顾客</el-button>
                </el-col>
            </el-row>
            <el-table :data="customerList" border style="width: 100%" class="tableStyle">
                 <el-table-column type="index" label="#" align="center" width="50px"></el-table-column>
                <el-table-column prop="customerIdCard" label="身份证号" align="center" ></el-table-column>
                <el-table-column prop="customerName" label="姓名" align="center" ></el-table-column>
                <el-table-column prop="customerSex" label="性别" align="center"></el-table-column>
                <el-table-column prop="customerPhoneNumber" label="手机号" align="center"></el-table-column>
                <el-table-column label="操作" align="center">
                <template slot-scope="scope">
                    <el-button type="warning" icon="el-icon-more" size="mini" 
                        @click="openEditCustomer(scope.row)">修改</el-button>
                    <el-button type="danger" icon="el-icon-delete" size="mini" 
                        @click="delCustomer(scope.row)">删除</el-button>
                </template>
                </el-table-column>
            </el-table>

                
            <el-dialog title="新增顾客信息" :visible.sync="addCustomerDialog" width="30%">
                <el-form :model="addCustomerInfo" status-icon 
                    ref="addCustomerInfo"  label-width="100px" class="demo-ruleForm">
                    <el-form-item label="身份证号" prop="customerIdCard">
                        <el-input v-model="addCustomerInfo.customerIdCard" autocomplete="off" ></el-input>
                    </el-form-item>
                    <el-form-item label="姓名" prop="customerName">
                    <el-input v-model="addCustomerInfo.customerName" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="性别" prop="customerSex">
                        <el-select v-model="addCustomerInfo.customerSex" placeholder="请选择">
                            <el-option v-for="item in SexList" :key="item" :label="item" :value="item"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="手机号" prop="customerPhoneNumber">
                        <el-input v-model="addCustomerInfo.customerPhoneNumber" autocomplete="off" clearable></el-input>
                    </el-form-item>
                </el-form>
                <span slot="footer" class="dialog-footer">
                    <el-button @click="cancelAddCustomer">取 消</el-button>
                    <el-button type="primary" @click="sureAddCustomer">确 定</el-button>
                </span>
            </el-dialog>

            <el-dialog title="编辑顾客信息" :visible.sync="editCustomerDialog" width="30%">
                <el-form :model="editCustomerInfo" status-icon 
                    ref="editCustomerInfo"  label-width="100px" class="demo-ruleForm">
                    <el-form-item label="身份证号" prop="customerIdCard">
                        <el-input v-model="editCustomerInfo.customerIdCard" autocomplete="off" disabled></el-input>
                    </el-form-item>
                    <el-form-item label="姓名" prop="customerName">
                    <el-input v-model="editCustomerInfo.customerName" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="性别" prop="customerSex">
                        <el-select v-model="editCustomerInfo.customerSex" placeholder="请选择">
                            <el-option v-for="item in SexList" :key="item" :label="item" :value="item"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="手机号" prop="customerPhoneNumber">
                        <el-input v-model="editCustomerInfo.customerPhoneNumber" autocomplete="off" clearable></el-input>
                    </el-form-item>
                </el-form>
                <span slot="footer" class="dialog-footer">
                    <el-button @click="cancelEditCustomer">取 消</el-button>
                    <el-button type="primary" @click="sureEditCustomer">确定</el-button>
                </span>
            </el-dialog>
        </el-card>
    </div>
</template>

<script>
export default {
  name: "roomAdmin",
    data(){
        return {
            queryName:'',
            SexList:['男','女'],
            customerList:[],//顾客信息列表
            count:0,
            editCustomerDialog:false,
            addCustomerDialog:false,
            editCustomerInfo:{
                customerIdCard:'',
                customerName:'',
                customerSex:'',
                customerPhoneNumber:''
            },
            addCustomerInfo:{
                customerIdCard:'',
                customerName:'',
                customerSex:'',
                customerPhoneNumber:''
            }

        }
    },
    methods:{
        openAddCustomer:function(){//打开新增顾客对话框
            this.addCustomerDialog = true;
        },
        cancelAddCustomer:function(){//取消新增顾客对话框
            this.addCustomerDialog = false;
            this.$refs.addCustomerInfo.resetFields();
        },
        sureAddCustomer:function(){//确认新增顾客对话框
            let empty = this.addCustomerInfo.customerIdCard==""||
                        this.addCustomerInfo.customerName==""||
                        this.addCustomerInfo.customerSex==""||
                        this.addCustomerInfo.customerPhoneNumber=="";
            if(empty){
                this.$message({
                    type:'error',
                    message:'新增顾客信息对话框不能为空！'
                })
            }else{
                this.$axios.post('/customer/add',this.addCustomerInfo)
                .then(res =>{
                    if(res.data.success){
                        this.addCustomerDialog = false;
                        this.$refs.addCustomerInfo.resetFields();
                        this.getAllCustomer();
                    }else{
                         this.$message({
                            type:'warning',
                            message:`${res.data.msg}`
                        });
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
        cancelEditCustomer:function(){//取消编辑顾客对话框
            this.editCustomerDialog = false;
            this.$refs.editCustomerInfo.resetFields();
        },
        sureEditCustomer:function(){//确定编辑顾客对话框
            this.$axios.put('/customer/update',this.editCustomerInfo)
            .then(res =>{
                if(res.data.success){
                    this.$message({
                        type:'success',
                        message:`${res.data.msg}`
                    });
                    this.$refs.editCustomerInfo.resetFields();
                }else{
                    this.$message({
                        type:'warning',
                        message:`${res.data.msg}`
                    });
                }
                this.editCustomerDialog = false;
                this.getAllCustomer();
            })
            .catch(err =>{
                this.$message({
                    type:'error',
                    message:'网络错误！'
                })
            })
        },
        openEditCustomer:function(scope){//打开编辑顾客信息对话框
            this.editCustomerDialog = true;
            this.editCustomerInfo.customerIdCard = scope.customerIdCard;
            this.editCustomerInfo.customerName = scope.customerName;
            this.editCustomerInfo.customerSex = scope.customerSex;
            this.editCustomerInfo.customerPhoneNumber = scope.customerPhoneNumber;
        },
        delCustomer:function(scope){//删除顾客
            this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning",
            })
            .then(() => {
                this.$axios.delete("/customer/del", {
                    data: {
                        customerIdCard:scope.customerIdCard
                    }})
                    .then((res) => {
                        if (res.data.success) {
                            this.$message({
                                type: "success",
                                message: `${res.data.msg}`
                            });
                            this.getAllCustomer();
                        } else {
                            this.$message({
                                type: "error",
                                message: `${res.data.msg}`
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
                    })
                });
        },
        getAllCustomer:function(){//查询所有顾客信息
            this.$axios.get('/customer/getAllCustomer',{
                params:{}
            })
            .then(res =>{
                if(res.data.success){
                    // this.$message({
                    //     type:'success',
                    //     message:`${res.data.msg}`
                    // });
                    this.customerList = res.data.customerList;
                    this.count = res.data.count;
                }else{
                    this.$message({
                        type:'warning',
                        message:`${res.data.msg}`
                    })
                }
            })
            .catch(err =>{
                // this.$message({
                //     type:'error',
                //     message:'网络错误！'
                // })
            })
        },
        query:function(){//模糊查询顾客信息
            if(this.queryName==""){
                this.$message({
                    type:'warning',
                    message:'顾客姓名不能为空！'
                })
            }else{
                this.$axios.get('/customer/queryCustomer',{
                    params:{
                        queryName:this.queryName
                    }
                })
                .then(res =>{
                    if(res.data.success){
                        this.customerList = res.data.customerList;
                        this.count = res.count;
                    }else{
                        this.$message({
                            type:'warning',
                            message:`${res.data.msg}`
                        })
                    }
                })
                .catch(err =>{
                    // this.$message({
                    //     type:'error',
                    //     message:'网络出错！'
                    // })
                })
            }
        }
    },
    mounted(){
        this.getAllCustomer();
    }
}
</script>

<style scope>
    .tableStyle{
        margin-top:20px;
    }
</style>