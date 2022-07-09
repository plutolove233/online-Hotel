module.exports = {
  url: '/ws/login',
  type: 'post',
  response: config => {
    return {
        code:200,
        msg:'登录成功',
        token:'123456',
        permission:{
          userManagementCode:1,
          logAuditCode:1,
          accountSettingsCode:1,
          userPermissionCode:1,
          dataStrategyCode:1
        }
    }
  }
}
