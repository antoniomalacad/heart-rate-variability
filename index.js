const fs = require("fs");

let ecgData = [];
fs.readFile("212.csv", "utf8", (error, rawData) => {
  if (error) throw error;
  let data = rawData.split("\n");
  for (let i = 1; i < 108000; i++) {
    ecgData.push(Number(data[i].split(",")[1]));
  }

  const peakInd = [];
  const peakVal = [];
  for (let i = 1; i < ecgData.length - 1; ++i) {
    if (
      ecgData[i - 1] < ecgData[i] &&
      ecgData[i] > ecgData[i + 1] &&
      ecgData[i] > 1150
    ) {
      peakInd.push(i);
      peakVal.push(ecgData[i]);
    }
  }

  const conv = 2.76923;
  const RR = [];
  for (let i = 0; i < peakInd.length - 1; i++) {
    RR.push((peakInd[i + 1] - peakInd[i]) * conv);
  }

  let mean = 0;
  for (let i = 0; i < RR.length - 1; i++) {
    mean += Math.abs(RR[i]);
  }
  mean = mean / RR.length;

  let sumOfMeanSq = 0;
  for (let i = 0; i < RR.length - 2; i++) {
    sumOfMeanSq += (RR[i] - mean) ** 2;
  }
  const SDNN = Math.sqrt(sumOfMeanSq / (RR.length - 1));

  let sumOfDiffSq = 0;
  for (let i = 0; i < RR.length - 2; i++) {
    sumOfDiffSq += (RR[i] - RR[i + 1]) ** 2;
  }
  const RMSSD = Math.sqrt(sumOfDiffSq / (RR.length - 1));
  console.log(mean, SDNN, RMSSD);
});
