const fs = require("fs");

let ecgData = [];
fs.readFile("212.csv", "utf8", (error, rawData) => {
  if (error) throw error;
  let data = rawData.split("\n");
  for (let i = 1; i < data.length; i++) {
    ecgData.push(Number(data[i].split(",")[1]));
  }
});
