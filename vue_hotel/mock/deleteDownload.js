module.exports = {
  url: `/ws/platform/delete`,
  type: 'post',
  response: config => {
    return {
        'err':0,
        'msg':null,
        'data':'删除成功'
    }
  }
}