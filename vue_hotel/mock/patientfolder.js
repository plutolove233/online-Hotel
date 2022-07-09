const data = {
  err:0,
  data:[
    {
      type:'感染发热1',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:1,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'发热',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:4,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'白血病',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:1,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'ALL感染',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:1,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'白血病',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:3,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'感染发热2',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:2,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'感染性发热3',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:4,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'感染发热4',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:3,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'感染发热5',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:2,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'感染发热6',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:2,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'感染发热8',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:2,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'感染发热7',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:2,
      details:[
        {
          name:'AA',
          
        }
      ]
    },
    {
      type:'感染发热9',
      date:'2017/10/14',
      secondtype:'儿童门诊',
      status:2,
      details:[
        {
          name:'AA',
          
        }
      ]
    } 
  ]
}

module.exports = {
  url: '/ws/patientType',
  type: 'get',
  response: config => {
    return data
  }
}
