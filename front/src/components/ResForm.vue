<template>
  <div class="testbox d-flex flex-column">
    <form>
      <fieldset>
        <legend class="rounded">客人 - {{ num }}</legend>
        <div class="columns">
          <!-- Name input area and validations -->
          <div class="item">
            <div
              class="form-group"
              :class="{ 'form-group--error': $v.fname.$error }"
            ></div>
            <label class="form__label" for="fname"
              >姓名<span>*</span></label
            >
            <input
              class="form__input"
              v-model.trim="$v.fname.$model"
              id="fname"
              type="text"
              name="fname"
              placeholder="张三"
              ref="input"
            />
            <div class="error" v-if="!$v.fname.required && $v.fname.$dirty">
              姓名必须填！
            </div>
            <div class="error" v-if="!$v.fname.minLength">
             姓名至少不少于
              {{ $v.fname.$params.minLength.min }}字 
            </div>
          </div>
          <!-- Last name input area and validations -->
          <!-- <div class="item">
            <div
              class="form-group"
              :class="{ 'form-group--error': $v.lname.$error }"
            ></div>
            <label class="form__label" for="lname">
              名<span>*</span></label
            >
            <input
              class="form__input"
              v-model.trim="$v.lname.$model"
              id="lname"
              type="text"
              name="lname"
              placeholder="Ozoglu"
            />
            <div class="error" v-if="!$v.lname.required && $v.lname.$dirty">
              名需要填
            </div>
            <div class="error" v-if="!$v.lname.minLength">
              Name must have at least
              {{ $v.lname.$params.minLength.min }} letters.
            </div>
          </div> -->
          <!-- Age input area and validations -->
          <div class="item">
            <div
              class="form-group"
              :class="{ 'form-group--error': $v.age.$error }"
            >
              <label class="form__label" for="age">年龄<span>*</span></label>
              <input
                class="form__input"
                id="age"
                type="number"
                name="age"
                v-model.trim="$v.age.$model"
                placeholder="必须大于1岁"
              />
            </div>
            <div class="error" v-if="!$v.age.required && $v.age.$dirty">
              年龄必须填
            </div>
            <div class="error" v-if="!$v.age.minValue">
              年龄大于 {{ $v.age.$params.minValue.min }}岁
            </div>
          </div>
          <!-- Sex input area and validations -->
          <div class="item">
            <div
              class="form-group"
              :class="{ 'form-group--error': $v.sex.$error }"
            ></div>
            <label class="d-block mb-1" for="sex">性别<span>*</span></label>
            <select v-model.trim="$v.sex.$model" name="sex" id="sex">
              <option value="" disabled selected>选择你的性别</option>
              <option value="male">男</option>
              <option value="female">女</option>
              <!-- <option value="other">Other</option> -->
            </select>

            <div class="error" v-if="!$v.sex.required && $v.sex.$dirty">
              请填你的性别！
            </div>
          </div>
          <!-- T.C. Identity No. input area and validations -->
          <div class="item">
            <div
              class="form-group"
              :class="{ 'form-group--error': $v.tc.$error }"
            ></div>
            <label for="tc">身份证号码<span>*</span></label>
            <input
              v-model.trim="$v.tc.$model"
              id="tc"
              type="text"
              name="tc"
              placeholder="请输入18位有效身份证号码"
            />

            <div class="error" v-if="!$v.tc.required && $v.tc.$dirty">
              请填入你的身份证号码
            </div>
            <div
              class="error"
              v-if="$v.tc.$model !== '' && !$v.tc.identityCheck && $v.tc.$dirty"
            >
              请填入有效身份证号码！
            </div>
          </div>
          <!-- HES Code input area and validations -->
          <!-- <div class="item">
            <div
              class="form-group"
              :class="{ 'form-group--error': $v.hes.$error }"
            ></div>
            <label for="hes">HES Code<span>*</span></label>
            <input
              v-model.trim="$v.hes.$model"
              id="hes"
              type="text"
              name="hes"
              placeholder="C5V9-4567-24"
            />
            <div class="error" v-if="!$v.hes.required && $v.hes.$dirty">
              Please enter your HES Code
            </div>
            <div
              class="error"
              v-if="$v.hes.$model !== '' && !$v.hes.hesCheck && $v.hes.$dirty"
            >
              Please enter a valid HES Code
            </div>
          </div> -->
          <!-- E-mail input area and validations -->
          <div class="item">
            <div
              class="form-group"
              :class="{ 'form-group--error': $v.email.$error }"
            ></div>
            <label class="form__label" for="email"
              >邮箱<span>*</span></label
            >
            <input
              class="form__input"
              v-model.trim="$v.email.$model"
              id="email"
              type="email"
              name="email"
              placeholder="fatihozoglu@yahoo.com"
            />
            <div class="error" v-if="!$v.email.required && $v.email.$dirty">
              邮箱必须填
            </div>
            <div class="error" v-if="!$v.email.email">
              请填入有效的邮箱地址！
            </div>
          </div>
          <!-- Phone input area and validations -->
          <div class="item">
            <div
              class="form-group"
              :class="{ 'form-group--error': $v.phone.$error }"
            ></div>
            <label for="phone">手机号<span>*</span></label>
            <input
              v-model.trim="$v.phone.$model"
              id="phone"
              type="tel"
              name="phone"
              placeholder="5395845151"
            />
            <div class="error" v-if="!$v.phone.required && $v.phone.$dirty">
              手机号码必须填
            </div>
            <div class="error" v-if="!$v.phone.phoneCheck && $v.phone.$dirty">
              请填入有效手机号码
            </div>
          </div>
        </div>
      </fieldset>
      <br />
      <!-- Showing "Next Guest" button for forms except the last form item-->
      <button v-if="id !== totalGuests - 1" @click.prevent="checkCompletion">
        下一位客人
      </button>
      <!-- Showing "Go to Payment" button for the last form item to route to /payment Payment view component -->
      <button v-else @click.prevent="goPayment">支付</button>
    </form>
  </div>
</template>

<script>
import { FormValidation } from "../mixins/FormValidation";

export default {
  name: "ResForm",
  mixins: [FormValidation],
  data() {
    return {
      fname: "",
      lname: "",
      age: "",
      email: "",
      sex: "",
      tc: "",
      hes: "",
      phone: "",
    };
  },
  props: {
    num: Number,
    form: String,
    id: Number,
    totalGuests: Number,
    allGuestInfo: Array,
    selectedHotel: Object,
  },
  methods: {
    focus() {
      this.$refs.input.focus();
    },
    //Checking the form if it is completed and there is no error, if it is complete focusing next form else giving validation error
    checkCompletion() {
      if (this.$v.$dirty && !this.$v.$invalid) {
        this.$emit("formCompleted", {
          formId: this.id,
          fname: this.fname,
          lname: this.lname,
          age: this.age,
          email: this.email,
          sex: this.sex,
          tc: this.tc,
          hes: this.hes,
          phone: this.phone,
        });
      } else {
        this.$v.$touch();
      }
    },
    //Checking if all forms are complete and if they are, routing to /payment route
    goPayment() {
      this.checkCompletion();
      if (this.allGuestInfo.length === this.totalGuests) {
        this.$emit("goPayment");
        this.$router.push({
          name: "Payment",
          params: { selectedHotel: this.selectedHotel },
        });
      }
    },
  },
};
</script>

<style scoped>
div,
form,
input,
select,
textarea,
label {
  padding: 0;
  margin: 0;
  outline: none;
  font-family: Roboto, Arial, sans-serif;
  font-size: 14px;
  color: #666;
  line-height: 22px;
}
h1 {
  position: absolute;
  margin: 0;
  font-size: 50px;
  color: #fff;
  z-index: 2;
  line-height: 83px;
}
legend {
  padding: 10px;
  font-family: Roboto, Arial, sans-serif;
  font-size: 18px;
  color: #fff;
  background-color: #1a4a8d;
}
textarea {
  width: calc(100% - 12px);
  padding: 5px;
}
.testbox {
  display: flex;
  justify-content: center;
  align-items: center;
  height: inherit;
  padding: 20px;
}
form {
  width: 100%;
  padding: 20px;
  border-radius: 6px;
  background: #fff;
  box-shadow: 0 0 8px #1a4a8d;
}
input,
select,
textarea {
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
}
input {
  width: calc(100% - 10px);
  padding: 5px;
}
input[type="date"] {
  padding: 4px 5px;
}
textarea {
  width: calc(100% - 12px);
  padding: 5px;
}
select {
  height: 30px;
}
.item:hover p,
.item:hover i,
.item input:hover,
.item select:hover,
.item textarea:hover {
  border: 1px solid transparent;
  box-shadow: 0 0 3px 0 #1a4a8d;
  color: #1a4a8d;
}
.item {
  position: relative;
  margin: 10px 0;
}
.item span {
  color: red;
}
.item i {
  right: 1%;
  top: 30px;
  z-index: 1;
}
.columns {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  flex-wrap: wrap;
}
.columns div {
  width: 48%;
}
.btn-block {
  margin-top: 10px;
  text-align: center;
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
.error {
  color: red;
}
@media (min-width: 568px) {
  .name-item,
  .city-item {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .name-item input,
  .name-item div {
    width: calc(50% - 20px);
  }
  .name-item div input {
    width: 97%;
  }
  .name-item div label {
    display: block;
    padding-bottom: 5px;
  }
}
</style>
