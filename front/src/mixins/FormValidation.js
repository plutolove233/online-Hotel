import { required, minLength, minValue, email } from "vuelidate/lib/validators";


// 身份证号验证 
function identityCheck(val) {
 var isIdCard2 = /^[1-9]\d{5}(19\d{2}|[2-9]\d{3})((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])(\d{4}|\d{3}X)$/i;
 var stard = "10X98765432"; //最后一位身份证的号码
 var first = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]; //1-17系数
 var sum = 0;
 if (!isIdCard2.test(val)) {
  return false;
  }
 var year = val.substr(6, 4);
 var month = val.substr(10, 2);
 var day = val.substr(12, 2);
 var birthday = val.substr(6, 8);
 if (birthday != dateToString(new Date(year + '/' + month + '/' + day))) { //校验日期是否合法
  return false;
  }
   for (var i = 0; i < val.length - 1; i++) {
   sum += val[i] * first[i];
   }
 var result = sum % 11;
 var last = stard[result]; //计算出来的最后一位身份证号码
 if (val[val.length - 1].toUpperCase() == last) {
  return true;
  } else {
  return false;
   }

  }
  
// function identityCheck(val) {
//   var odd = 0,
//     even = 0,
//     res = 0,
//     total = 0,
//     err = [
//       11111111110, 22222222220, 33333333330, 44444444440, 55555555550,
//       66666666660, 7777777770, 88888888880, 99999999990,
//     ];

//   if (val.length != 11) return false;
//   if (isNaN(val)) return false;
//   if (val[0] == 0) return false;

//   odd =
//     parseInt(val[0]) +
//     parseInt(val[2]) +
//     parseInt(val[4]) +
//     parseInt(val[6]) +
//     parseInt(val[8]);
//   even =
//     parseInt(val[1]) + parseInt(val[3]) + parseInt(val[5]) + parseInt(val[7]);

//   odd = odd * 7;
//   res = Math.abs(odd - even);
//   if (res % 10 != val[9]) return false;

//   for (let i = 0; i < 10; i++) {
//     total += parseInt(val[i]);
//   }

//   if (total % 10 != val[10]) return false;

//   if (err.toString().indexOf(val) != -1) return false;

//   return true;
// }

// //HES val checking algorithm for validation
// function hesCheck(val) {
//   let reg = /^[A-Z][0-9][A-Z][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9]$/g;
//   return reg.test(val);
// }

//Phone format checking algorithm (format => 5557778899)
function phoneCheck(val) {
  let reg = /^\d{10}$/;
  if (val === "") return true;
  else return reg.test(val);
}

export const FormValidation = {
  validations: {
    fname: {
      required,
      minLength: minLength(2),
    },
    // lname: {
    //   required,
    //   minLength: minLength(3),
    // },
    age: {
      required,
      minValue: minValue(1),
    },
    email: {
      required,
      email,
    },
    sex: {
      required,
    },
    tc: {
      required,
      identityCheck,
    },
    // hes: {
    //   required,
    //   hesCheck,
    // },
    phone: {
      required,
      phoneCheck,
    },
  },
};
