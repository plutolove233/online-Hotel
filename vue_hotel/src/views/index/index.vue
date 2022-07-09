<template>
    <div class="index">
        <div class="slider">
            <li v-for="(item,index) of navList" :key="index" :class="{active: index == current}" @click="handleLeft(index)">
                <span>{{item.label}}</span>
            </li>
        </div>
        <div class="main">
            <component :is="current == 0 ? 'check' : 'room'"></component>
        </div>
    </div>
</template>
<script>
import check from './check.vue'
import room from './room.vue'
export default {
    name:'index',
    components:{
        check,
        room
    },
    data() {
        return{
            current:0,
            navList:[
                {
                    label:'办理手续',
                    value:'1'
                },
                {
                    label:'查看酒店房间',
                    value:'2'
                },

            ]
        }
    },
    methods:{
        handleLeft(idx) {
            this.current = idx
        }
    }
}
</script>  
<style lang="less" scoped>
ul,li{
    list-style: none;
}
.index{
    width: 100%;
    display: flex;
    .slider{
        box-sizing: border-box;
        padding: 50px 24px;
        width: 200px;
        li{
            cursor: pointer;
            width: 100%;
            height: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            background: rgb(71, 121, 230);
            border-radius: 4px;
            &.active{
                background: orange;
            }
            span{
                color: white;
            }
        }
    }
    .main{
        width: calc(100vw - 200px);
    }
}
</style>