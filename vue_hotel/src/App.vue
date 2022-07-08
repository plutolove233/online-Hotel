<template>
  <div id="app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App',
  components: {
  },
  watch: {
  },
  data () {
    return {
    };
  },
  computed: {
  },
  created () {
  },
  methods: {
  }
};
</script>

<style lang="less" scoped>
*{
  margin: 0;
  padding: 0;
}
#app {
  min-height: 100vh;
  margin: 0;
  background: linear-gradient(180deg, #c9cece 0%, #eaf2f3 93.75%);
}
</style>
