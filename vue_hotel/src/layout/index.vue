<template>
  <div class="layout">
    <div class="app-main">
      <router-view :key="$route.path"></router-view>
    </div>
  </div>
</template>
<script>
export default {
  components: {
  },
  data () {
    return {
    };
  },
  created () {
  }
};
</script>
<style lang="less" scoped>
.layout{
  height: 100%;
  // overflow: hidden;
.app-main {
  height: calc(100% - 80px);
  background-color: #dde8eb;
  position: relative;
}
}

</style>
