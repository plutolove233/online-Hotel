const data = {
  "err": 0,
  "msg": null,
  "data": [
      {
          "operateContent": "小贺导出变量两堆",
          "ip": "127.0.0.1",
          "operateType": "EXPORT",
          "userName": "小贺",
          "logTime": "2021-08-11 10:16:27"
      },
      {
          "operateContent": "小贺导出变量两堆",
          "ip": "127.0.0.1",
          "operateType": "EXPORT",
          "userName": "小贺",
          "logTime": "2021-08-11 10:16:27"
      }
  ]
}
module.exports = {
  url: '/ws/plantform/log',
  type: 'post',
  response: config => {
    return {
        data
    }
  }
}