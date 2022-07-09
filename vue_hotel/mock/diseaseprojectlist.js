const data = {
  "err": 0,
  "msg": null,
  "data": {
    "total": 5,
    "dataList": [{
        "id": 1,
        "isDeleted": 0,
        "createdTime": "2021-09-10",
        "updatedTime": "2021-09-10",
        "projectName": "回顾项目1",
        "projectType": 0,
        "projectIntroduction": "111",
        "domain": 1,
        "stopTime": "2021-09-10",
        "status": 0,
        "totalPatients": null,
        "member": {
          "id": 1,
          "isDeleted": 0,
          "createdTime": "2021-09-10",
          "updatedTime": "2021-09-10",
          "userId": null,
          "userName": "管理员1",
          "accountId": null,
          "projectId": null,
          "roleId": null,
          "expiredTime": null
        }
      },{
        "id": 2,
        "isDeleted": 0,
        "createdTime": "2021-09-10",
        "updatedTime": "2021-09-10",
        "projectName": "回顾项目1",
        "projectType": 0,
        "projectIntroduction": "111",
        "domain": 2,
        "stopTime": "2021-09-10",
        "status": 0,
        "totalPatients": null,
        "member": {
          "id": 1,
          "isDeleted": 0,
          "createdTime": "2021-09-10",
          "updatedTime": "2021-09-10",
          "userId": null,
          "userName": "管理员1",
          "accountId": null,
          "projectId": null,
          "roleId": null,
          "expiredTime": null
        }
      },{
        "id": 3,
        "isDeleted": 0,
        "createdTime": "2021-09-10",
        "updatedTime": "2021-09-10",
        "projectName": "回顾项目1",
        "projectType": 0,
        "projectIntroduction": "111",
        "domain": 3,
        "stopTime": "2021-09-10",
        "status": 0,
        "totalPatients": null,
        "member": {
          "id": 1,
          "isDeleted": 0,
          "createdTime": "2021-09-10",
          "updatedTime": "2021-09-10",
          "userId": null,
          "userName": "管理员1",
          "accountId": null,
          "projectId": null,
          "roleId": null,
          "expiredTime": null
        }
      },{
        "id": 4,
        "isDeleted": 0,
        "createdTime": "2021-09-10",
        "updatedTime": "2021-09-10",
        "projectName": "回顾项目1",
        "projectType": 0,
        "projectIntroduction": "111",
        "domain": 4,
        "stopTime": "2021-09-10",
        "status": 0,
        "totalPatients": null,
        "member": {
          "id": 1,
          "isDeleted": 0,
          "createdTime": "2021-09-10",
          "updatedTime": "2021-09-10",
          "userId": null,
          "userName": "管理员1",
          "accountId": null,
          "projectId": null,
          "roleId": null,
          "expiredTime": null
        }
      },{
        "id": 5,
        "isDeleted": 0,
        "createdTime": "2021-09-10",
        "updatedTime": "2021-09-10",
        "projectName": "回顾项目1",
        "projectType": 0,
        "projectIntroduction": "111",
        "domain": 5,
        "stopTime": "2021-09-10",
        "status": 0,
        "totalPatients": null,
        "member": {
          "id": 1,
          "isDeleted": 0,
          "createdTime": "2021-09-10",
          "updatedTime": "2021-09-10",
          "userId": null,
          "userName": "管理员1",
          "accountId": null,
          "projectId": null,
          "roleId": null,
          "expiredTime": null
        }
      }
    ]
  }
}
module.exports = {
  url: '/ws/project/query',
  type: 'post',
  response: config => {
    return {
      data
    }
  }
}
