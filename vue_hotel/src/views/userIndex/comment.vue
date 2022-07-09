<template>
    <div class="comment">
        <div class="comment-list">
            <div class="comment-item" v-for="(item,index) of commentList" :key="index">
                <div class="left">
                    <img :src="item.FaceUrl" alt="">
                </div>
                <div class="right">{{item.RemarkContent}}</div>
            </div>
        </div>
        <h3>我的评论</h3>
        <div class="my-comment">
            <el-input
            type="textarea"
            placeholder="请输入内容"
            v-model="comment">
            </el-input>
            <el-button @click="submit">提交</el-button>
        </div>
    </div>
</template>
<script>
import * as Api from '@/request/api.js'
import index from '../../layout/index.vue'
export default {
  components: { index },
    data() {
        return {
            commentList:[],
            comment:''
        }
    },
    mounted() {
        this.getCommentList()
    },
    methods:{
        async getCommentList() {
            const res = await Api.getCommentInfo({HotelID:this.$route.query.id})
            // console.log(res)
            this.commentList = res.data
        },
        async submit() {
            const res = await Api.addCommentInfo({RemarkContent: this.comment,HotelID:this.$route.query.id})
            console.log(res)
            if(res.code == 2000) {
              this.$message({
                message: '添加成功',
                type: 'success'
              });
              this.getCommentList()
            } else {
              this.$message({
                message: '添加失败',
                type: 'error'
              });
            }
        }
    }
}
</script>
<style lang="less" scoped>
.comment{
    box-sizing: border-box;
    padding: 48px 24px;
    .comment-list{
        .comment-item{
            display: flex;
            border: 1px dashed black;
            .left{
                width: 150px;
                height: 150px;
                box-sizing: border-box;
                padding: 12px;
                border-right: 1px dashed black;
                img{
                    width: 100%;
                    height: 100%;
                }
            }
            .right{
                flex: 1;
                box-sizing: border-box;
                padding: 24px;
            }
        }
    }
        h3{
            margin-top: 48px;
            border-top: 2px solid #ccc;
        }
        /deep/.my-comment{
            .el-textarea{
                .el-textarea__inner{
                    min-height: 300px !important;
                }
            }
        }
}
</style>