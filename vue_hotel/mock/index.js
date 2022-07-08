let [css, userinfo, message, download, permission, log, deleteDownload, specialDisease, diseaseproject,datawarehouse, patientfolder, depository, timeconfig, visittime, timeviewdata, historyVis,diseaseprojectList, currentproject] = [
  require('./css'),
  require('./userinfo'),
  require('./message'),
  require('./download'),
  require('./permission'),
  require('./log'),
  require('./deleteDownload'),
  require('./specialDisease'),
  require('./diseaseproject'),
  require('./datawarehouse'),
  require('./patientfolder'),
  require('./depository'),
  require('./timeconfig'),
  require('./visittime'),
  require('./timeviewData'),
  require('./visitHistory'),
  require('./diseaseprojectlist'),
  require('./currentproject')
  // require('./refresh'),
  // require('./flip'),
  // require('./history')
];
const mocks = [
  css,
  userinfo,
  message,
  download,
  permission,
  log,
  deleteDownload,
  specialDisease,
  diseaseproject,
  datawarehouse,
  patientfolder,
  depository,
  timeconfig,
  visittime,
  timeviewdata,
  historyVis,
  diseaseprojectList,
  currentproject
  // refresh,
  // flip,
  // history
];

module.exports = mocks;
