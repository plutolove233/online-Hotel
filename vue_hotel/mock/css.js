const data = 'body{}'

module.exports = {
  url: '/ws/css',
  type: 'get',
  response: config => {
    return data
  }
}
