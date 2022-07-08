<template>
  <div id="app">
    <div class="content">
        <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name:'App'
}
</script>

<style>
    html,body{
      width:100%;
      height:100%;
    }
    *{
      margin:0;
      padding:0;
    }
    #app{
      width:100%;
      height:100%;
    }
    #app .content{
      width:100%;
      height:100%;
    }
</style>
