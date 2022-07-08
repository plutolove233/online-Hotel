const data = [
  {
    id:1,
    createdTime:1629101149,
    fileName:'',
    type:1,
    status:0,
    errMsg:'文件生成中',
    fileForm:1
  }, {
    id:2,
    createdTime:1629101142,
    fileName:'',
    type:1,
    status:0,
    errMsg:'文件生成中',
    fileForm:1
  },{
    id:3,
    createdTime:1629101140,
    fileName:'',
    type:1,
    status:0,
    errMsg:'文件生成中',
    fileForm:1
  },
  {
    id:4,
    createdTime:1573467375,
    fileName:'',
    type:2,
    status:1,
    errMsg:'下载成功',
    fileForm:1
  },
  {
    id:5,
    createdTime:1573467373,
    fileName:'',
    type:2,
    status:1,
    errMsg:'下载成功',
    fileForm:1
  },
  {
    id:6,
    createdTime:1473467377,
    fileName:'',
    type:3,
    status:2,
    errMsg:'下载失败',
    fileForm:0
  },
  {
    id:7,
    createdTime:1473467373,
    fileName:'',
    type:3,
    status:2,
    errMsg:'下载失败',
    fileForm:0
  }
]
module.exports = {
  url: '/ws/platform/export/query',
  type: 'post',
  response: config => {
    return {
        'err':0,
        msg:null,
        'data':data
    }
  }
}
