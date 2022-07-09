const data = {
  "err": 0,
  "msg": null,
  "data": {    
    theader:[{
      prop: 'identifier',
      label: '患者编号',
      sortable: true
    }, {
      prop: 'name',
      label: '姓名',
      minWidth: '120'
    }, {
      prop: 'sex',
      label: '性别',
      minWidth: '120'
    }, {
      prop: 'nation',
      label: '民族',
      minWidth: '120'
    }, {
      prop: 'birthdate',
      label: '出生日期',
      minWidth: '120'
    }, {
      prop: 'job',
      label: '职业类型',
      minWidth: '120'
    }
      ],
      tbody:[
        {
          
        },
        {
          identifier: '1',
          name: '王小虎1',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发'
        }, 
        {
          identifier: '2',
          name: '王小虎2',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发'
        },
        {
          identifier: '3',
          name: '王小虎3',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发'
        },
        {
          identifier: '4',
          name: '王小虎4',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发'
        },
        {
          identifier: '5',
          name: '王小虎5',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发'
        },
      ]
    }
  }

module.exports = {
  url: '/ws/diseaseproject/list',
  type: 'get',
  response: config => {
    return {
        data
    }
  }
}