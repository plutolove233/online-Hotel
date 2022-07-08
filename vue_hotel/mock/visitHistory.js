const data = 
{
  "err": 0,
  "msg": null,
  "data": [
    {
        "SEX": "女性",
        "DGNAM": "声门良性肿瘤",
        "AGE": 35
    },
    {
        "SEX": "女性",
        "DGNAM": "声门良性肿瘤",
        "AGE": 35
    },
    {
        "SEX": "女性",
        "DGNAM": "声门良性肿瘤",
        "AGE": 35
    },
    {
        "SEX": "女性",
        "DGNAM": "声门良性肿瘤",
        "AGE": 35
    },
    {
        "SEX": "女性",
        "DGNAM": "过敏性心肌炎",
        "AGE": 35
    },
    {
        "SEX": "女性",
        "DGNAM": "过敏性心肌炎",
        "AGE": 35
    },
    {
        "SEX": "女性",
        "DGNAM": "过敏性心肌炎",
        "AGE": 35
    },
    {
        "SEX": "女性",
        "DGNAM": "过敏性心肌炎",
        "AGE": 35
    }
]
}
module.exports = {
  url: '/ws/depository/queryHistoryVis',
  type: 'post',
  response: config => {
    return data
  }
}
