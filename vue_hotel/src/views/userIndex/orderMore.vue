 <template>
  <div class="orderMore">
    <div class="left"  v-if="currentRoom">
        <img :src="currentRoom.RoomPicUrl" alt="">
        <div class="img-box">
            <img :src="currentRoom.RoomPicUrl" alt="">
        </div>
        <div class="room-detail">
            <div class="room-item">
                <p>面积</p>

                
                <p>{{currentRoom.Square}}</p>
            </div>
            <div class="room-item">
                <p>楼层</p>
                <p>{{currentRoom.Floor}}</p>
            </div>

            
            <div class="room-item">
                <p>窗户</p>
                <p>{{currentRoom.WindowDescription}}</p>
            </div>
        </div>
    </div>

    
    <div class="right">
      <el-form
        :model="ruleForm"
        status-icon
        :rules="rules"
        ref="ruleForm"
        label-width="100px"
        class="demo-ruleForm"
      >
      <el-form-item v-model="ruleForm.info" label="订房信息" prop="info">
        <button @click="reduce">-</button>
        <span>{{ ruleForm.info }}</span>
        <button @click="add">+</button>
        间
      </el-form-item>
        <el-form-item label="住客姓名" prop="GuestName">
          <el-input type="text" v-model="ruleForm.GuestName" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="身份证" prop="GuestID">
          <el-input type="text" v-model="ruleForm.GuestID" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="电话号码" prop="GuestPhone">
          <el-input v-model="ruleForm.GuestPhone"></el-input>
        </el-form-item>
        <el-form-item label="预计到店时间" prop="ArrivalTime">
          <el-date-picker value-format="yyyy-MM-dd"  v-model="ruleForm.ArrivalTime" autocomplete="off"></el-date-picker>
        </el-form-item>
        <el-form-item label="预计离店时间" prop="CheckOutTime">
          <el-date-picker  value-format="yyyy-MM-dd"  v-model="ruleForm.CheckOutTime" autocomplete="off"></el-date-picker>
        </el-form-item>
        <el-form-item>
            <span>在线支付{{totalPrice}}元</span>
          <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import * as Api from '@/request/api.js'
export default {
  data() {
    var checkEmpty = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('不能为空'));
      } else {
            callback();
      }
    }
    return {
      currentRoom:{
        Price:0,
        RoomPicUrl:''
      },
      ruleForm: {
        GuestName: '',
        GuestID: '',
        GuestPhone: '',
        ArrivalTime:null,
        CheckOutTime:null,
        info:0
      },
      rules: {
        GuestName: [{ validator: checkEmpty, trigger: 'blur' }],
        GuestID: [{ validator: checkEmpty, trigger: 'blur' }],
        GuestPhone: [{ validator: checkEmpty, trigger: 'blur' }],
        ArrivalTime: [{ validator: checkEmpty, trigger: 'blur' }],
        CheckOutTime: [{ validator: checkEmpty, trigger: 'blur' }],
      },
    };
  },
  computed: {
    totalPrice() {
        return this.ruleForm.info * this.currentRoom.Price
    }
  },
  mounted() {
    this.getRoomInfo()
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
            const params = {...this.ruleForm,HotelID:this.$route.query.hotelId*1,RoomTypeID:this.$route.query.roomId*1}
            console.log(params)
            const res = await Api.orderRoom(params)
            console.log(res)
            if(res.code == 2000) {              this.$message({
                message: '预定成功',
                type: 'success'
              });
              this.$router.push(
                {
                    path:'paySuccess'
                }
              )
            } else {
                
                this.$message.error(res.message);
            }
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    async getRoomInfo() {
        const res = await Api.getRoomInfo({RoomID: this.$route.query.roomId*1})
        console.log(res)
        if(res.data.length == 0) return
        this.currentRoom = res.data[0]
    },
    reduce() {
        if(this.ruleForm.info <= 0) return
        this.ruleForm.info -= 1
    },
    add() {
        this.ruleForm.info += 1
    }
  },
};
</script>
<style lang="less" scoped>
.orderMore{
    width: 70vw;
    margin: 0 auto;
    display: flex;
    box-sizing: border-box;
    padding: 20vh 0;
    .left{
        margin-right: 24px;
        width: 50%;
        .img-box{
            height: 200px;
            width: 100%;
            img{
                width: 100%;
                height: 100%;
            }
        }
        .room-detail{
            display: flex;
            justify-content: space-around;
        }
    }
    .right{
        box-sizing: border-box;
        padding: 16px;
        border-radius: 8px;
        width: 50%;
        border: 1px solid #ccc;
        box-shadow: 5px 5px 5px #ccc;
    }
}
</style>