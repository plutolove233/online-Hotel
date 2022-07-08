const data = 
  {
    "err": 0,
    "msg": null,
    "data": {
        "minVisTime": "2019-04-10",
        "maxVisTime": "2021-01-18"
    }
  }
module.exports = {
  url: '/ws/depository/queryVisTime',
  type: 'post',
  response: config => {
    return data
  }
}
