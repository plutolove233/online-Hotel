const data = {
  "err": 0,
  "msg": null,
  "data": {
      "id": 14,
      "isDeleted": 0,
      "createdTime": "2021-09-18",
      "updatedTime": "2021-09-26",
      "projectName": "回顾研究测试update",
      "projectType": 0,
      "projectIntroduction": "测试数据update",
      "domain": 6,
      "stopTime": "2021-09-18",
      "status": 0
  }
}
module.exports = {
  url: '/ws/project/selectProInfo',
  type: 'post',
  response: config => {
    return {
        data:data.data
    }
  }
}