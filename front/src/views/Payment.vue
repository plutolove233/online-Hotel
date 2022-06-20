<template>
  <main class="main" ref="content">
    <!-- Modal to show payment status -->
    <div
      v-if="isModalOpen"
      class="
        payment-verification
        d-flex
        flex-column
        justify-content-evenly
        align-items-center
      "
    >
      <div v-if="!success" class="spinner-border text-primary" role="status">
        <span class="sr-only">正在加载....</span>
      </div>
      <div v-if="!success">Waiting For Payment Verification</div>
      <div
        v-if="success"
        class="d-flex flex-column justify-content-evenly align-items-center"
      >
        <div>
          <i
            style="color: green; font-size: 40px"
            class="fa fa-check-square-o mb-4"
            aria-hidden="true"
          ></i>
        </div>
        <div>付款成功</div>
      </div>
    </div>

    <!--When modal is closed, this area shows the booking and guests details-->
    <div v-if="!isModalOpen" class="booking-details">
      <!-- Button for downloading booking and guests detail as PDF (html2pdf.js)-->
      <button class="mb-3" @click="download">
        下载你的预定信息
      </button>
      <!--Booking confirmation details with hotel and guest info-->
      <h1 class="h3">预定信息</h1>
      <div class="hotel-details mb-3">
        <p class="m-0 mb-1">酒店名称: {{ selectedHotel.name }}</p>
        <p class="m-0 mb-1">酒店地址: {{ selectedHotel.adress }}</p>
        <p class="m-0 mb-1">入住时间: {{ guestData.checkinDate }}</p>
        <p class="m-0 mb-1">离开时间: {{ guestData.checkoutDate }}</p>
        <p class="m-0 mb-1">
          客人: {{ guestData.adult }} 位成人
          <span v-if="guestData.children !== 0"
            >, {{ guestData.children }} 位儿童</span
          >
        </p>
        <p class="m-0 mb-1">房间: {{ guestData.room }} 间</p>
        <p class="m-0 mb-1">总价:  {{ totalPrice }}元</p>
      </div>
      <div class="guest-details d-flex gap-5 mb-4">
        <div v-for="(guest, index) in allGuestInfo" :key="index" class="guest">
          <h2 class="h5">Guest {{ index + 1 }}</h2>
          <p class="m-0 mb-1">姓: {{ guest.fname }}</p>
          <p class="m-0 mb-1">名: {{ guest.lname }}</p>
          <p class="m-0 mb-1">身份证号码: {{ guest.tc }}</p>
          <p class="m-0 mb-1">
            <span class="me-4">性别: {{ guest.sex }}</span>
            <span>岁数: {{ guest.age }}</span>
          </p>
          <p class="m-0 mb-1">邮箱: {{ guest.email }}</p>
          <p class="m-0 mb-1">电话号码: {{ guest.phone }}</p>
          <!-- <p class="m-0 mb-1">HES Code: {{ guest.hes }}</p> -->
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import html2pdf from "html2pdf.js";

export default {
  name: "Reservation",
  data() {
    return {
      isModalOpen: true,
      success: false,
    };
  },
  props: {
    selectedHotel: Object,
    allGuestInfo: Array,
    guestData: Object,
  },
  methods: {
    closeModal() {
      setTimeout(() => (this.isModalOpen = false), 6000);
      setTimeout(() => (this.success = true), 3000);
    },
    download() {
      html2pdf(this.$refs.content);
    },
  },
  computed: {
    totalPrice() {
      return (
        this.selectedHotel.price * this.guestData.room * this.guestData.days +
        (this.selectedHotel.price * 18) / 100
      );
    },
  },
  mounted() {
    this.closeModal();
    console.log(this.selectedHotel);
  },
};
</script>

<style scoped>
.main {
  display: flex;
  padding: 120px 50px 50px 50px;
  background-color: #f5f5f5;
  min-height: 100vh;
}
.payment-verification {
  width: 40vw;
  height: 30vh;
  margin: 0 auto;
  background-color: white;
  border-radius: 10px;
  font-size: 24px;
  font-weight: 600;
}
.booking-details {
  width: 100vw;
  min-height: 100vh;
}
.guest-details {
  flex-wrap: wrap;
}
.guest {
  border: 1px solid rgb(177, 177, 177);
  border-radius: 5px;
  padding: 20px;
}
button {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background: #1a4a8d;
  font-size: 16px;
  color: #fff;
  cursor: pointer;
}
button:hover {
  background: #14396d;
}
</style>
