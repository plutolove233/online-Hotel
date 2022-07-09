const data = [
  {
      "index": 1,
      "chartKey": "seeADoctor",
      "chartName": "就诊"
  },
  {
      "index": 2,
      "chartKey": "therapy",
      "chartName": "治疗"
  },
  {
      "index": 3,
      "chartKey": "examine",
      "chartName": "检查",
      "stairLAbel": [
          {
              "labelName": "专科检查",
              "secondaryLabel": [
                  {
                      "labelName": "胸廓畸形",
                      "fieldName": "SETDYN"
                  },
                  {
                      "labelName": "胸膜摩擦音",
                      "fieldName": "SEPFYN"
                  },
                  {
                      "labelName": "淋巴结肿大部位",
                      "fieldName": "SESLNL"
                  },
                  {
                      "labelName": "杵状指/趾",
                      "fieldName": "SECTYN"
                  },
                  {
                      "labelName": "上腔静脉综合征",
                      "fieldName": "SESVSYN"
                  },
                  {
                      "labelName": "声带麻痹",
                      "fieldName": "SEVCPYN"
                  }
              ]
          },
          {
              "labelName": "肺功能检查",
              "secondaryLabel": [
                  {
                      "labelName": "FEV1%",
                      "fieldName": "SPDFEV"
                  },
                  {
                      "labelName": "FEV1/FVC",
                      "fieldName": "SPDRFF"
                  },
                  {
                      "labelName": "PEF%",
                      "fieldName": "SPDFEF"
                  },
                  {
                      "labelName": "MMEF%",
                      "fieldName": "SPDMEF"
                  },
                  {
                      "labelName": "V75%",
                      "fieldName": "SPDVTQUA"
                  },
                  {
                      "labelName": "V50%",
                      "fieldName": "SPDVHAL"
                  },
                  {
                      "labelName": "V25%",
                      "fieldName": "SPDVQUA"
                  },
                  {
                      "labelName": "MVV%",
                      "fieldName": "SPDMVV"
                  },
                  {
                      "labelName": "VC%",
                      "fieldName": "SPDVC"
                  },
                  {
                      "labelName": "RV/TLC",
                      "fieldName": "SPDRVTLC"
                  },
                  {
                      "labelName": "DLCO%",
                      "fieldName": "SPDDLCO"
                  },
                  {
                      "labelName": "Raw%",
                      "fieldName": "SPDRAW"
                  },
                  {
                      "labelName": "sGaw%",
                      "fieldName": "SPDSGAW"
                  },
                  {
                      "labelName": "激发（舒张）",
                      "fieldName": "SPDAD"
                  },
                  {
                      "labelName": "FEV1",
                      "fieldName": "SPDFEVO"
                  },
                  {
                      "labelName": "MMEF75/25",
                      "fieldName": "SPDMEFT"
                  },
                  {
                      "labelName": "MEF50",
                      "fieldName": "SPDMEFFT"
                  },
                  {
                      "labelName": "MEF25",
                      "fieldName": "SPDMEFTF"
                  },
                  {
                      "labelName": "舒张后FEV1%",
                      "fieldName": "SPDPDFEP"
                  },
                  {
                      "labelName": "舒张后FEV1/FVC",
                      "fieldName": "SPDPDRFF"
                  },
                  {
                      "labelName": "舒张后FEV1",
                      "fieldName": "SPDPDFEV"
                  },
                  {
                      "labelName": "呼吸道阻力",
                      "fieldName": "SPDAR"
                  }
              ]
          },
          {
              "labelName": "纤支镜检查",
              "secondaryLabel": [
                  {
                      "labelName": "纤支镜类型",
                      "fieldName": "SFBTYPE"
                  },
                  {
                      "labelName": "肺纤支镜次数",
                      "fieldName": "SFBNUM"
                  },
                  {
                      "labelName": "肺纤支镜总次数",
                      "fieldName": "SFBTNUM"
                  },
                  {
                      "labelName": "有无病理学活检",
                      "fieldName": "SFBPBTN"
                  },
                  {
                      "labelName": "病理学活检部位",
                      "fieldName": "SFBPBLOC"
                  },
                  {
                      "labelName": "有无细胞学刷片",
                      "fieldName": "SFBCBYN"
                  },
                  {
                      "labelName": "细胞学刷片部位",
                      "fieldName": "SFBCBLOC"
                  },
                  {
                      "labelName": "会厌异常",
                      "fieldName": "SFBEAYN"
                  },
                  {
                      "labelName": "声带活动减弱",
                      "fieldName": "SFBVADYN"
                  },
                  {
                      "labelName": "声带活动减弱位置",
                      "fieldName": "SFBVADLOC"
                  },
                  {
                      "labelName": "声带结构异常",
                      "fieldName": "SFBVSAYN"
                  },
                  {
                      "labelName": "声带结构异常位置",
                      "fieldName": "SFBVSALOC"
                  },
                  {
                      "labelName": "隆突异常",
                      "fieldName": "SFBCAYN"
                  },
                  {
                      "labelName": "软骨环结构异常",
                      "fieldName": "SFBCSAYN"
                  },
                  {
                      "labelName": "粘膜异常",
                      "fieldName": "SFBMAYN"
                  },
                  {
                      "labelName": "气管管腔异常",
                      "fieldName": "SFBTLAYN"
                  },
                  {
                      "labelName": "气管管腔异常类型",
                      "fieldName": "SFBTLAT"
                  },
                  {
                      "labelName": "支气管粘膜异常",
                      "fieldName": "SFBBMAYN"
                  },
                  {
                      "labelName": "支气管粘膜异常位置",
                      "fieldName": "SFBBMLOC"
                  },
                  {
                      "labelName": "支气管管腔异常",
                      "fieldName": "SFBBLAYN"
                  },
                  {
                      "labelName": "支气管管腔异常类型",
                      "fieldName": "SFBBLAT"
                  },
                  {
                      "labelName": "支气管管腔异常位置",
                      "fieldName": "SFBBLLOC"
                  },
                  {
                      "labelName": "开口异常",
                      "fieldName": "SFBOAYN"
                  },
                  {
                      "labelName": "开口异常类型",
                      "fieldName": "SFBOAT"
                  },
                  {
                      "labelName": "开口异常位置",
                      "fieldName": "SFBOALOC"
                  },
                  {
                      "labelName": "出血",
                      "fieldName": "SFBBDYN"
                  },
                  {
                      "labelName": "出血位置",
                      "fieldName": "SFBBDLOC"
                  },
                  {
                      "labelName": "有无分泌物",
                      "fieldName": "SFBSCYN"
                  },
                  {
                      "labelName": "分泌物性质",
                      "fieldName": "SFBSCN"
                  },
                  {
                      "labelName": "分泌物位置",
                      "fieldName": "SFBSCLOC"
                  },
                  {
                      "labelName": "嵴异常",
                      "fieldName": "SFBRAYN"
                  },
                  {
                      "labelName": "嵴异常位置",
                      "fieldName": "SFBRALOC"
                  },
                  {
                      "labelName": "有无新生物",
                      "fieldName": "SFBNCYN"
                  },
                  {
                      "labelName": "新生物性质",
                      "fieldName": "SFBNCN"
                  },
                  {
                      "labelName": "新生物位置",
                      "fieldName": "SFBNCLOC"
                  }
              ]
          },
          {
              "labelName": "petct检查",
              "secondaryLabel": [
                  {
                      "labelName": "有无糖代谢水平变化",
                      "fieldName": "SPCGMCYN"
                  },
                  {
                      "labelName": "糖代谢水平位置",
                      "fieldName": "SPCGMLOC"
                  },
                  {
                      "labelName": "糖代谢水平变化",
                      "fieldName": "SPCGMLC"
                  },
                  {
                      "labelName": "有无SUV",
                      "fieldName": "SPCSUVYN"
                  },
                  {
                      "labelName": "SUV",
                      "fieldName": "SPCSUV"
                  },
                  {
                      "labelName": "SUV取值部位",
                      "fieldName": "SPCSUVLOC"
                  },
                  {
                      "labelName": "有无非肺癌肿瘤",
                      "fieldName": "SPCNLCT"
                  },
                  {
                      "labelName": "非肺癌肿瘤类型",
                      "fieldName": "SPCNLCTN"
                  },
                  {
                      "labelName": "非肺癌肿瘤确诊程度",
                      "fieldName": "SPCNLCTD"
                  },
                  {
                      "labelName": "静脉注射18F-FDG",
                      "fieldName": "SPCIIFDG"
                  },
                  {
                      "labelName": "有无结节",
                      "fieldName": "SPCNDYN"
                  },
                  {
                      "labelName": "结节位置",
                      "fieldName": "SPCNDLOC"
                  },
                  {
                      "labelName": "结节大小",
                      "fieldName": "SPCNDSZ"
                  },
                  {
                      "labelName": "密度",
                      "fieldName": "SPCNDD"
                  },
                  {
                      "labelName": "分叶征",
                      "fieldName": "SPCLSYN"
                  },
                  {
                      "labelName": "毛刺征",
                      "fieldName": "SPCGSYN"
                  },
                  {
                      "labelName": "空泡征",
                      "fieldName": "SPCVSYN"
                  },
                  {
                      "labelName": "肺气肿",
                      "fieldName": "SPCEPSYN"
                  },
                  {
                      "labelName": "肺大泡",
                      "fieldName": "SPCPBYN"
                  },
                  {
                      "labelName": "肺纤维化",
                      "fieldName": "SPCPFYN"
                  },
                  {
                      "labelName": "胸腔积液",
                      "fieldName": "SPCPEYN"
                  },
                  {
                      "labelName": "胸腔积液位置",
                      "fieldName": "SPCPELOC"
                  },
                  {
                      "labelName": "心包积液",
                      "fieldName": "SPCPCEYN"
                  },
                  {
                      "labelName": "淋巴结肿大",
                      "fieldName": "SPCSLNYN"
                  },
                  {
                      "labelName": "淋巴结肿大位置",
                      "fieldName": "SPCLELOC"
                  },
                  {
                      "labelName": "淋巴结转移",
                      "fieldName": "SPCLMYN"
                  },
                  {
                      "labelName": "淋巴结转移位置",
                      "fieldName": "SPCLMLOC"
                  },
                  {
                      "labelName": "骨骼转移",
                      "fieldName": "SPCBMYN"
                  },
                  {
                      "labelName": "骨质破坏",
                      "fieldName": "SPCBDYN"
                  },
                  {
                      "labelName": "胸膜转移",
                      "fieldName": "SPCPMYN"
                  },
                  {
                      "labelName": "支气管狭窄",
                      "fieldName": "SPCBSYN"
                  },
                  {
                      "labelName": "支气管狭窄位置",
                      "fieldName": "SPCBSLOC"
                  },
                  {
                      "labelName": "肺不张",
                      "fieldName": "SPCATYN"
                  },
                  {
                      "labelName": "肺炎",
                      "fieldName": "SPCPNYN"
                  },
                  {
                      "labelName": "血管侵犯",
                      "fieldName": "SPCVIYN"
                  },
                  {
                      "labelName": "心脏侵犯",
                      "fieldName": "SPCHIYN"
                  },
                  {
                      "labelName": "心包侵犯",
                      "fieldName": "SPCPVYN"
                  },
                  {
                      "labelName": "纵隔侵犯",
                      "fieldName": "SPCMIYN"
                  },
                  {
                      "labelName": "膈肌侵犯",
                      "fieldName": "SPCDIYN"
                  },
                  {
                      "labelName": "胸膜侵犯",
                      "fieldName": "SPCPIYN"
                  },
                  {
                      "labelName": "胸壁侵犯",
                      "fieldName": "SPCCWVYN"
                  },
                  {
                      "labelName": "肺癌",
                      "fieldName": "SPCLC"
                  }
              ]
          },
          {
              "labelName": "CT检查",
              "secondaryLabel": [
                  {
                      "labelName": "结节数量",
                      "fieldName": "SCTNDNUM"
                  },
                  {
                      "labelName": "结节位置",
                      "fieldName": "SCTNDLOC"
                  },
                  {
                      "labelName": "结节长径",
                      "fieldName": "SCTNDLD"
                  },
                  {
                      "labelName": "结节短径",
                      "fieldName": "SCTNDSD"
                  },
                  {
                      "labelName": "密度",
                      "fieldName": "SCTNDD"
                  },
                  {
                      "labelName": "分叶征",
                      "fieldName": "SCTLSYN"
                  },
                  {
                      "labelName": "毛刺征",
                      "fieldName": "SCTGSYN"
                  },
                  {
                      "labelName": "空泡征",
                      "fieldName": "SCTVSYN"
                  },
                  {
                      "labelName": "胸膜凹陷征",
                      "fieldName": "SCTPDSYN"
                  },
                  {
                      "labelName": "倍增时间",
                      "fieldName": "SCTDBDUR"
                  },
                  {
                      "labelName": "肺气肿",
                      "fieldName": "SCTEPSYN"
                  },
                  {
                      "labelName": "肺大泡",
                      "fieldName": "SCTPBYN"
                  },
                  {
                      "labelName": "肺纤维化",
                      "fieldName": "SCTPFYN"
                  },
                  {
                      "labelName": "胸腔积液",
                      "fieldName": "SCTPEYN"
                  },
                  {
                      "labelName": "胸腔积液位置",
                      "fieldName": "SCTPELOC"
                  },
                  {
                      "labelName": "心包积液",
                      "fieldName": "SCTPCEYN"
                  },
                  {
                      "labelName": "淋巴结肿大",
                      "fieldName": "SCTSLNYN"
                  },
                  {
                      "labelName": "淋巴结转移",
                      "fieldName": "SCTLNMYN"
                  },
                  {
                      "labelName": "骨骼转移",
                      "fieldName": "SCTBMYN"
                  },
                  {
                      "labelName": "骨质破坏",
                      "fieldName": "SCTBDYN"
                  },
                  {
                      "labelName": "胸膜转移",
                      "fieldName": "SCTPMYN"
                  },
                  {
                      "labelName": "支气管狭窄",
                      "fieldName": "SCTBSYN"
                  },
                  {
                      "labelName": "肺不张",
                      "fieldName": "SCTATYN"
                  },
                  {
                      "labelName": "肺炎",
                      "fieldName": "SCTPNYN"
                  },
                  {
                      "labelName": "血管侵犯",
                      "fieldName": "SCTVIYN"
                  },
                  {
                      "labelName": "心脏侵犯",
                      "fieldName": "SCTHIYN"
                  },
                  {
                      "labelName": "心包侵犯",
                      "fieldName": "SCTPVYN"
                  },
                  {
                      "labelName": "纵隔侵犯",
                      "fieldName": "SCTMIYN"
                  },
                  {
                      "labelName": "膈肌侵犯",
                      "fieldName": "SCTDIYN"
                  },
                  {
                      "labelName": "胸膜侵犯",
                      "fieldName": "SCTPIYN"
                  },
                  {
                      "labelName": "胸壁侵犯",
                      "fieldName": "SCTCWIYN"
                  }
              ]
          },
          {
              "labelName": "体格检查",
              "secondaryLabel": [
                  {
                      "labelName": "身高",
                      "fieldName": "PEHEIGH"
                  },
                  {
                      "labelName": "体重",
                      "fieldName": "PEWEIGH"
                  },
                  {
                      "labelName": "体温",
                      "fieldName": "PETEMP"
                  },
                  {
                      "labelName": "脉搏",
                      "fieldName": "PEPULSE"
                  },
                  {
                      "labelName": "心率",
                      "fieldName": "PEHR"
                  },
                  {
                      "labelName": "收缩压",
                      "fieldName": "PESP"
                  },
                  {
                      "labelName": "舒张压",
                      "fieldName": "PEDP"
                  },
                  {
                      "labelName": "呼吸",
                      "fieldName": "PER"
                  },
                  {
                      "labelName": "体重指数BMI",
                      "fieldName": "PEBMI"
                  },
                  {
                      "labelName": "体表面积BSA",
                      "fieldName": "PEBSA"
                  },
                  {
                      "labelName": "ECOG评分结果",
                      "fieldName": "PEECOG"
                  },
                  {
                      "labelName": "KPS评分结果",
                      "fieldName": "PEKPS"
                  }
              ]
          }
      ]
  },
  {
      "index": 4,
      "chartKey": "checkout",
      "chartName": "检验",
      "stairLAbel": [
          {
              "labelName": "血常规",
              "secondaryLabel": [
                  {
                      "labelName": "白细胞计数(WBC)-静脉血",
                      "fieldName": "WBCVB"
                  },
                  {
                      "labelName": "中性粒细胞绝对值(NEUT#)-静脉血",
                      "fieldName": "NEUT#VB"
                  },
                  {
                      "labelName": "淋巴细胞绝对值(LY#)-静脉血",
                      "fieldName": "LY#VB"
                  },
                  {
                      "labelName": "淋巴细胞百分比(LY%)-静脉血",
                      "fieldName": "LY%-VB"
                  },
                  {
                      "labelName": "淋巴细胞群计数(LYM#)-静脉血",
                      "fieldName": "LYM#-VB"
                  },
                  {
                      "labelName": "单核细胞绝对值(MONO#)-静脉血",
                      "fieldName": "MONO#-VB"
                  },
                  {
                      "labelName": "单核细胞百分比(MONO%)-静脉血",
                      "fieldName": "MONO%-VB"
                  },
                  {
                      "labelName": "中性粒细胞百分比(NE%)-静脉血",
                      "fieldName": "NE%-VB"
                  },
                  {
                      "labelName": "嗜碱性粒细胞绝对值(BASO#)-静脉血",
                      "fieldName": "BASO#-VB"
                  },
                  {
                      "labelName": "嗜碱性粒细胞百分比(BASO%)-静脉血",
                      "fieldName": "BASO%-VB"
                  },
                  {
                      "labelName": "嗜酸性粒细胞绝对值(EO#)-静脉血",
                      "fieldName": "EO#-VB"
                  },
                  {
                      "labelName": "嗜酸性粒细胞百分比(EO%)-静脉血",
                      "fieldName": "EO%-VB"
                  },
                  {
                      "labelName": "红细胞(RBC)-静脉血",
                      "fieldName": "RBC-VB"
                  },
                  {
                      "labelName": "血红蛋白(Hb)测定-静脉血",
                      "fieldName": "Hb-VB"
                  },
                  {
                      "labelName": "红细胞压积(PCV)-静脉血",
                      "fieldName": "PCV-VB"
                  },
                  {
                      "labelName": "红细胞比容(Hct)-静脉血",
                      "fieldName": "Hct-VB"
                  },
                  {
                      "labelName": "平均红细胞体积(MCV)-静脉血",
                      "fieldName": "MCV-VB"
                  },
                  {
                      "labelName": "平均红细胞血红蛋白含量(MCH)-静脉血",
                      "fieldName": "MCH-VB"
                  },
                  {
                      "labelName": "平均红细胞血红蛋白浓度(MCHC)-静脉血",
                      "fieldName": "MCHC-VB"
                  },
                  {
                      "labelName": "平均红细胞体积分布宽度(RDW)-静脉血",
                      "fieldName": "RDW-VB"
                  },
                  {
                      "labelName": "红细胞体积分布宽度(RDW-CV)-静脉血",
                      "fieldName": "RDW-CV-VB"
                  },
                  {
                      "labelName": "红细胞分布宽度(RDW-SD)-静脉血",
                      "fieldName": "RDW-SD-VB"
                  },
                  {
                      "labelName": "平均红细胞体积分布宽度(RDW-SV)-静脉血",
                      "fieldName": "RDW-SV-VB"
                  },
                  {
                      "labelName": "血小板(PLT)-静脉血",
                      "fieldName": "PLT-VB"
                  },
                  {
                      "labelName": "平均血小板体积(MPV)-静脉血",
                      "fieldName": "MPV-VB"
                  },
                  {
                      "labelName": "血小板压积(PCT)-静脉血",
                      "fieldName": "PCT-VB"
                  },
                  {
                      "labelName": "血小板分布宽度(PDW)-静脉血",
                      "fieldName": "PDW-VB"
                  },
                  {
                      "labelName": "大血小板比率(P-LCR)-静脉血",
                      "fieldName": "P-LCR-VB"
                  },
                  {
                      "labelName": "大血小板体积(PLCR)-静脉血",
                      "fieldName": "PLCR-VB"
                  },
                  {
                      "labelName": "大红细胞百分比(MACR%)-静脉血",
                      "fieldName": "MACR%-VB"
                  },
                  {
                      "labelName": "小红细胞百分比(MICR%)-静脉血",
                      "fieldName": "MICR%-VB"
                  },
                  {
                      "labelName": "网织红细胞百分比(RET%)-静脉血",
                      "fieldName": "RET%-VB"
                  },
                  {
                      "labelName": "网织红细胞绝对值(RET#)-静脉血",
                      "fieldName": "RET#-VB"
                  },
                  {
                      "labelName": "网织红细胞平均体积(MCVr)-静脉血",
                      "fieldName": "MCVr-VB"
                  },
                  {
                      "labelName": "单个网织红细胞平均血红蛋白浓度(CHCMr)-静脉血",
                      "fieldName": "CHCMr-VB"
                  },
                  {
                      "labelName": "网织红细胞分布宽度(RDWr)-静脉血",
                      "fieldName": "RDWr-VB"
                  },
                  {
                      "labelName": "单个网织红细胞血红蛋白含量(CHr)-静脉血",
                      "fieldName": "Chr-VB"
                  },
                  {
                      "labelName": "网织红细胞成熟指数(RMI)-静脉血",
                      "fieldName": "RMI-VB"
                  },
                  {
                      "labelName": "未成熟网织红细胞比率(IRF)-静脉血",
                      "fieldName": "IRF-VB"
                  },
                  {
                      "labelName": "中荧光强度网织红细胞(MFR)-静脉血",
                      "fieldName": "MFR-VB"
                  },
                  {
                      "labelName": "高荧光强度网织红细胞(HFR)-静脉血",
                      "fieldName": "HFR-VB"
                  },
                  {
                      "labelName": "低荧光强度网织红细胞(LFR)-静脉血",
                      "fieldName": "LFR-VB"
                  }
              ]
          },
          {
              "labelName": "便常规",
              "secondaryLabel": [
                  {
                      "labelName": "外观-粪便",
                      "fieldName": "AP-F"
                  },
                  {
                      "labelName": "颜色-粪便",
                      "fieldName": "CO-F"
                  },
                  {
                      "labelName": "性状-粪便",
                      "fieldName": "CH-F"
                  },
                  {
                      "labelName": "隐血试验-粪便",
                      "fieldName": "HB-F"
                  },
                  {
                      "labelName": "红细胞-粪便",
                      "fieldName": "RBC-F"
                  },
                  {
                      "labelName": "白细胞-粪便",
                      "fieldName": "WBC-F"
                  },
                  {
                      "labelName": "粪胆素检查-粪便",
                      "fieldName": "FB-F"
                  },
                  {
                      "labelName": "霉菌-粪便",
                      "fieldName": "M-F"
                  }
              ]
          },
          {
              "labelName": "尿常规",
              "secondaryLabel": [
                  {
                      "labelName": "尿量-尿液",
                      "fieldName": "UV-U"
                  },
                  {
                      "labelName": "颜色-尿液",
                      "fieldName": "CO-U"
                  },
                  {
                      "labelName": "透明度-尿液",
                      "fieldName": "TR-U"
                  },
                  {
                      "labelName": "渗透压-尿液",
                      "fieldName": "OP-U"
                  },
                  {
                      "labelName": "隐血(HB)-尿液",
                      "fieldName": "HB-U"
                  },
                  {
                      "labelName": "白细胞LEU-尿液",
                      "fieldName": "LEU-U"
                  },
                  {
                      "labelName": "尿蛋白PRO-尿液",
                      "fieldName": "PRO-U"
                  },
                  {
                      "labelName": "尿酮体KET-尿液",
                      "fieldName": "KET-U"
                  },
                  {
                      "labelName": "尿糖GLU-尿液",
                      "fieldName": "GLU-U"
                  },
                  {
                      "labelName": "亚硝酸盐NIT-尿液",
                      "fieldName": "NIT-U"
                  },
                  {
                      "labelName": "尿胆红素BIL-尿液",
                      "fieldName": "BIL-U"
                  },
                  {
                      "labelName": "尿胆原URO-尿液",
                      "fieldName": "URO-U"
                  },
                  {
                      "labelName": "维生素C(Vit C)-尿液",
                      "fieldName": "VitC-U"
                  },
                  {
                      "labelName": "酸碱度(PH值)测定-尿液",
                      "fieldName": "PH-U"
                  },
                  {
                      "labelName": "比重测定SG-尿液",
                      "fieldName": "SG-U"
                  },
                  {
                      "labelName": "白细胞WBC-尿液",
                      "fieldName": "WBC-U"
                  },
                  {
                      "labelName": "红细胞RBC-尿液",
                      "fieldName": "RBC-U"
                  }
              ]
          },
          {
              "labelName": "生化检查",
              "secondaryLabel": [
                  {
                      "labelName": "总蛋白(TP)测定-静脉血",
                      "fieldName": "TP-VB"
                  },
                  {
                      "labelName": "白蛋白(Alb)测定-静脉血",
                      "fieldName": "Alb-VB"
                  },
                  {
                      "labelName": "球蛋白(Glb)测定-静脉血",
                      "fieldName": "Glb-VB"
                  },
                  {
                      "labelName": "白蛋白/球蛋白(ALB/GLO)比值-静脉血",
                      "fieldName": "ALB/GLO-VB"
                  },
                  {
                      "labelName": "白蛋白(Alb)测定-静脉血",
                      "fieldName": "Alb-VB"
                  },
                  {
                      "labelName": "葡萄糖(Glu)测定-静脉血",
                      "fieldName": "Glu-VB"
                  },
                  {
                      "labelName": "空腹血糖(FBG)-静脉血",
                      "fieldName": "FBG-VB"
                  },
                  {
                      "labelName": "乳酸(LA)测定-静脉血",
                      "fieldName": "LA-VB"
                  },
                  {
                      "labelName": "丙酮酸(PA)测定-静脉血",
                      "fieldName": "PA-VB"
                  },
                  {
                      "labelName": "糖化红细胞膜蛋白测定-静脉血",
                      "fieldName": "GEMPA-VB"
                  },
                  {
                      "labelName": "糖化血清蛋白(GSP)测定-静脉血",
                      "fieldName": "GSP-VB"
                  },
                  {
                      "labelName": "糖化白蛋白(GA)测定-静脉血",
                      "fieldName": "GA-VB"
                  },
                  {
                      "labelName": "糖化血红蛋白(HbA1c)测定-静脉血",
                      "fieldName": "HbA1c-VB"
                  },
                  {
                      "labelName": "糖基化血红蛋白(GHb)-静脉血",
                      "fieldName": "Ghb-VB"
                  }
              ]
          }
      ]
  }
]
module.exports = {
  url: '/ws/depository/queryTimeViewAllConfig',
  type: 'get',
  response: config => {
    return data
  }
}