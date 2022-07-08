const data = [{
  "index": 1,
  "chartKey": "fiberbronchoscopy",
  "chartName": "纤支镜检查"
  },{
  "index": 2,
  "chartKey": "dischargeRecord",
  "chartName": "出院记录"
  },{
  "index": 3,
  "chartKey": "PETCTCheckup",
  "chartName": "petct检查"
  },{
  "index": 4,
  "chartKey": "pathologicalFindings",
  "chartName": "病理报告结果"
  },{
  "index": 5,
  "chartKey": "hospitalizedRecords",
  "chartName": "入院记录"
  },{
  "index": 6,
  "chartKey": "lungCancerSurgeryRecords",
  "chartName": "肺癌手术记录"
  },{
  "index": 7,
  "chartKey": "diagnosisInformation",
  "chartName": "患者诊疗信息"
  },{
  "index": 8,
  "chartKey": "hospitalRecords",
  "chartName": "住院记录"
  },{
  "index": 9,
  "chartKey": "pathologicalRecords",
  "chartName": "病理记录"
  },{
  "index": 10,
  "chartKey": "personalHistory",
  "chartName": "个人史"
  },{
  "index": 11,
  "chartKey": "healthCheckup",
  "chartName": "体格检查"
  },{
  "index": 12,
  "chartKey": "emergencyHistory",
  "chartName": "门急诊病历"
  },{
  "index": 13,
  "chartKey": "medicalRecordInformation",
  "chartName": "病案首页主信息"
  },{
  "index": 14,
  "chartKey": "informedConsent",
  "chartName": "知情同意书"
  },{
  "index": 15,
  "chartKey": "specialityCheckup",
  "chartName": "专科检查"
  },{
  "index": 16,
  "chartKey": "diagnosisRecords",
  "chartName": "诊断记录"
  },{
  "index": 17,
  "chartKey": "selfreportedSymptom",
  "chartName": "主诉症状"
  },{
  "index": 18,
  "chartKey": "emergencyRecords",
  "chartName": "门急诊记录"
  },{
  "index": 19,
  "chartKey": "demographicInformation",
  "chartName": "患者人口学信息"
  },{
  "index": 20,
  "chartKey": "operationTechniqueInformation",
  "chartName": "手术操作信息"
  },{
  "index": 21,
  "chartKey": "microbiologicalReport",
  "chartName": "微生物报告"
  },{
  "index": 22,
  "chartKey": "drugSensitiveTest",
  "chartName": "药敏试验"
  },{
  "index": 23,
  "chartKey": "imageologicalExamination",
  "chartName": "影像学检查"
  },{
  "index": 24,
  "chartKey": "presentHistorySymptom",
  "chartName": "现病史症状"
  },{
  "index": 25,
  "chartKey": "familyHistory",
  "chartName": "家族史"
  },{
  "index": 26,
  "chartKey": "nonpharmaceuticalOrders",
  "chartName": "住院非药品医嘱"
  },{
  "index": 27,
  "chartKey": "previousHistory",
  "chartName": "既往史"
  },{
  "index": 28,
  "chartKey": "menstruationHistory",
  "chartName": "月经婚育史"
  },{
  "index": 29,
  "chartKey": "pulmonaryFunctionTest",
  "chartName": "肺功能检查"
  },{
  "index": 30,
  "chartKey": "medicalRecordDiagnosis",
  "chartName": "病案首页诊断"
  },{
  "index": 31,
  "chartKey": "surgeryRecords",
  "chartName": "手术记录"
  },{
  "index": 32,
  "chartKey": "hospitalDrugUse",
  "chartName": "住院用药"
  },{
  "index": 33,
  "chartKey": "outpatientPrescription",
  "chartName": "门诊处方"
  },{
  "index": 34,
  "chartKey": "progressNote",
  "chartName": "病程记录"
  },{
  "index": 35,
  "chartKey": "targetedDrugOrders",
  "chartName": "靶向药物医嘱"
  },{
  "index": 36,
  "chartKey": "CTExamination",
  "chartName": "CT检查"
  },{
  "index": 37,
  "chartKey": "chemotherapy",
  "chartName": "化疗药物医嘱"
  },{
  "index": 38,
  "chartKey": "surveyReports",
  "chartName": "检验报告"
  }
]
module.exports = {
  url: '/ws/depository/queryDoMainAllConfig',
  type: 'get',
  response: config => {
    return {
        'err':0,
        'msg':'获取分域侧边栏成功',
        'data':data
    }
  }
}
