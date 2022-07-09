const data = {
  "err": 0,
  "msg": null,
  "data": {    
    theader:[{
      prop: 'identifier',
      label: '患者编号',
      minWidth: '120'
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
          rate1:10,
          rate2:20,
          rate3:30,
          rate4:40,
          rate5:50,
          rate6:60
        },
        {
          identifier: '11',
          name: '王小虎1',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发',
        }, 
        {
          identifier: '22',
          name: '王小虎2',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发',
        },
        {
          identifier: '33',
          name: '王小虎3',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发'
        },
        {
          identifier: '44',
          name: '王小虎4',
          sex: '男',
          nation: '汉',
          birthdate: '2016-05-03',
          job: '前端开发',
        },
        {
          identifier: '55',
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
  url: '/ws/datawarehouse/list',
  type: 'get',
  response: config => {
    return {
        data
    }
  }
}