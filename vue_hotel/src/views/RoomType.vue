<template>
  <div class="user">
    <el-card class="box-card">
      <el-row :gutter="20">
        <el-col :span="20">
          <el-select v-model="type" placeholder="请选择" @change="chooseRoomType" title="选择房型">
            <el-option v-for="item in typeList" :key="item" :label="item" :value="item"></el-option>
          </el-select>
          <el-button
            icon="el-icon-circle-plus-outline"
            type="primary"
            @click="openAddRoom"
            style="margin-left:20px"
          >添加房型</el-button>
          <el-button
            icon="el-icon-circle-plus-outline"
            type="primary"
            @click="getAllRoomType"
            style="margin-left:20px"
          >所有房型</el-button>
        </el-col>
      </el-row>
      <el-table :data="roomTypeList" border class="tableStyle">
        <el-table-column type="index" label="#" align="center"></el-table-column>
        <el-table-column prop="url" label="图片链接" align="center">
          <template slot-scope="scope">
            <img :src="scope.row.url" style="height:100px" />
          </template>
        </el-table-column>
        <el-table-column prop="type" label="房型" align="center"></el-table-column>
        <el-table-column prop="description" label="描述" align="center"></el-table-column>
        <el-table-column prop="price" label="价格" align="center"></el-table-column>
        <el-table-column label="操作" align="center" width="200px">
          <template slot-scope="scope">
            <el-button type="primary" icon="el-icon-edit" size="mini" @click="update(scope.row)"></el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini" @click="delRoom(scope)"></el-button>
            <img :src="scope.url" alt style="width:100px" />
          </template>
        </el-table-column>
      </el-table>

      <el-dialog title="添加房型" :visible.sync="addRoomDialog" width="30%">
        <el-form
          :model="addRoomInfo"
          status-icon
          :rules="addRoomRules"
          ref="addRoomInfo"
          label-width="100px"
          class="demo-ruleForm"
        >
            <el-form-item label="房型" prop="type">
                <el-input v-model="addRoomInfo.type" autocomplete="off" clearable></el-input>
            </el-form-item>
            <el-form-item label="价格" prop="price">
                <el-input v-model="addRoomInfo.price" autocomplete="off" clearable></el-input>
            </el-form-item>
            <el-form-item label="描述" prop="description">
                <el-input v-model="addRoomInfo.description" autocomplete="off" clearable></el-input>
            </el-form-item>
            <el-form-item label="图片" prop="url">
                <el-input v-model="addRoomInfo.url" autocomplete="off" clearable></el-input>
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
            <el-form-item label="房型" prop="type">
                <el-input v-model="editRoomInfo.type" autocomplete="off" clearable></el-input>
            </el-form-item>
            <el-form-item label="价格" prop="price">
                <el-input v-model="editRoomInfo.price" autocomplete="off" clearable></el-input>
            </el-form-item>
            <el-form-item label="描述" prop="description">
                <el-input v-model="editRoomInfo.description" autocomplete="off" clearable></el-input>
            </el-form-item>
            <el-form-item label="图片" prop="url">
                <el-input v-model="editRoomInfo.url" autocomplete="off" clearable></el-input>
            </el-form-item>
        </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="cancelEditRoom">取 消</el-button>
                <el-button type="primary" @click="sureEditRoom">确 定</el-button>
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
      addRoomDialog: false,//添加房型对话框控制器
      editRoomDialog:false,//编辑房型对话框控制器
      type: "",//选择房型
      searchInfo: "",//查询信息
      addRoomInfo: {//添加房型对话框中对应信息
        type: "",
        price: "",
        description: "",
        url: "",
      },
      editRoomInfo: {//编辑房型对话框中对应信息
        type: "",
        price: "",
        description: "",
        url: "",
      },
      typeList: [],//房型列表type
      roomTypeList: [],//所有房型列表
      count: 0,//房型数量
      pageSize: 10,//每页数量
      offset: 1,//当前页
      addRoomRules: {//添加房型规则
        type: [{ required: true, message: "请输入房间类型", trigger: "blur" }],
        price: [{ required: true, message: "请输入房间价格", trigger: "blur" }],
        description: [
          { required: true, message: "请输入描述", trigger: "blur" },
        ],
        url: [{ required: true, message: "请输入图片链接", trigger: "blur" }],
      }
    };
  },
  methods: {
    update:function(scope){
        this.editRoomInfo = scope;
        this.editRoomDialog = true;
    },
    cancelEditRoom:function(){//取消编辑房型页面
        this.editRoomDialog = false;
        this.$refs.editRoomInfo.resetFields();
    },
    sureEditRoom:function(){
        let empty = this.editRoomInfo.type ==""||this.editRoomInfo.price==""||
                    this.editRoomInfo.description=="" ||this.editRoomInfo.url=="";
        if(empty){
            this.$message({
                type:'error',
                message:'修改信息不能为空！'
            })
        }else{
            this.$axios.put('/roomtype/update',this.editRoomInfo)
            .then(res =>{
                if(res.data.success){
                    this.$message({
                        type:success,
                        message:`${res.data.msg}`
                    });
                    this.editRoomDialog = false;
                    this.$refs.editRoomInfo.resetFields();
                    this.chooseRoomType();

                }else{
                     this.$message({
                        type:success,
                        message:`${res.data.msg}`
                    })
                }
            })
            .catch(err =>{
                 this.$message({
                        type:success,
                        message:'网络错误！'
                    })
            })
        }

        this.editRoomDialog = false;
    },
    delRoom: function (scope) {
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
            this.$axios.delete('/roomtype/del',{
                data:{
                    type:scope.row.type
                }
            })
            .then(res =>{
                if(res.data.success){
                    this.$message({
                        type:'success',
                        message:`${res.data.msg}`
                    });
                    this.getAllRoomType();
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
                    message:`${res.data.msg}`
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
    chooseRoomType: function (realType) {
      //选择房型
      if (this.type == "") {
        this.getAllRoomType();
      } else {
        this.$axios
          .get("/roomtype/getOneRoomType", {
            params: {
              type: realType,
            },
          })
          .then((res) => {
            if (res.data.success) {
              this.$message({
                type: "success",
                message: `${res.data.msg}`,
              });
              this.roomTypeList = res.data.roomTypeList;
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
              message: `${res.data.msg}`,
            });
          });
      }
    },
    openAddRoom: function () {
      //打开添加房间类型
      this.addRoomDialog = true;
    },
    sureAddRoom: function () {
      //确定添加房间类型
      let empty =
        this.addRoomInfo.type == "" ||
        this.addRoomInfo.price == "" ||
        this.addRoomInfo.description == "" ||
        this.addRoomInfo.url == "";
      if (empty) {
        this.$message({
          type: "error",
          message: "所填项不能为空！",
        });
      } else {
        this.$axios.post("/roomtype/add", this.addRoomInfo).then((res) => {
          if (res.data.success) {
            this.$message({
              type: "success",
              message: `${res.data.msg}`,
            });
            this.getAllRoomType();
            this.getAllType();
            this.addRoomDialog = false;
            this.$refs.addRoomInfo.resetFields();
          } else {
            this.$message({
              type: "error",
              message: `${res.data.msg}`,
            });
          }
        });
      }
      this.addRoomDialog = false;
    },
    cancelAddRoom: function () {
      //取消添加房间类型
      this.addRoomDialog = false;
    },
    getAllRoomType: function () {
      this.$axios
        .get("/roomtype/getAllRoomType", {
          params: {
            //    pageSize:this.pageSize,
            //    offset:this.offset
          },
        })
        .then((res) => {
          if (res.data.success) {
            this.roomTypeList = res.data.roomTypeList;
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
          //   type: "error",
          //   msg: "网路错误！",
          // });
        });
    },
    getAllType: function () {
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
            this.typeList = res.data.typeList;
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
    }
  },
  mounted() {
    this.getAllRoomType();
    this.getAllType();
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
.tableStyle {
  width: 100%;
  height: 100%;
  overflow-y: auto;
}
</style>