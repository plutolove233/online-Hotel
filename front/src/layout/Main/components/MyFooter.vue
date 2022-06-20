<!--网页尾部组件-->
<template>
  <footer>
    <div id="copyright">
      <p>
        版权所有© Copyright
        <a href="https://www.ncepu.edu.cn/">华北电力大学</a>
        控制与计算机工程学院
        技术支持:010-61772988 QQ:812520785
      </p>
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style>
footer {
  margin-top: 20px;
  height: 40px;
  padding: 5px 0;
  background-image: linear-gradient(
    to bottom,
    rgb(241, 244, 246),
    rgb(241, 244, 246),
    rgb(241, 244, 246),
  );
  background-size: 1px 150px;
  position: relative;
  overflow: hidden;
  /* width: 1200px; */
}
footer #copyright {
  font-size: 14px;
  color: black;
  text-align: center;
}
footer #copyright a{
  color: black;
}
</style>
