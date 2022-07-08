<template>
<el-dialog
  title="订单信息"
  :visible="dialogVisible"
  width="30%"
  :before-close="handleClose">
  <slot></slot>
  <span slot="footer" class="dialog-footer">
    <el-button @click="handleClose">取 消</el-button>
    <el-button type="primary" @click="handleConfirm">确 定</el-button>
  </span>
</el-dialog>
</template>
<script>
export default {
    props:{
        dialogVisible:{
            type:Boolean,
            default: () => false
        }
    },
    methods:{
        handleClose() {
            this.$emit('close')
        },
        handleConfirm() {
            this.$emit('confirm')
        }
    }
}
</script>