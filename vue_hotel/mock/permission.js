module.exports = {
  url: '/ws/permission',
  type: 'get',
  response: config => {
    return {
        code:200,
        msg:'获取权限成功',
        permission:
          [{userManagementCode:1},
          {logAuditCode:0},
          {accountSettingsCode:1},
          {userPermissionCode:0},
          {dataStrategyCode:1}]
        
    }
  }
}
