import numpy as np
import matplotlib.pyplot as plt
import pathlib
from ecgdetectors import Detectors
from hrv import HRV

fs = 360
detectors = Detectors(fs)
rawcsv212 = np.loadtxt(open("212.csv", "rb"), dtype=int,
                       delimiter=",", skiprows=1)

rawcsv113 = np.loadtxt(open("113.csv", "rb"), dtype=int,
                       delimiter=",", skiprows=1)

print("Finished reading csv")

ecg212 = rawcsv212[:, 1]
ecg113 = rawcsv113[:, 1]
r_peaks212 = detectors.pan_tompkins_detector(ecg212)
r_peaks113 = detectors.pan_tompkins_detector(ecg113)

myHRV = HRV(360)
rmssd212 = myHRV.RMSSD(r_peaks212)
sdnn212 = myHRV.SDNN(r_peaks212)
rmssd113 = myHRV.RMSSD(r_peaks113)
sdnn113 = myHRV.SDNN(r_peaks113)

rr212 = list()
for i in range(1, len(r_peaks212), 1):
    rr212.append((r_peaks212[i] - r_peaks212[i-1]) * 2.76923077)

rr113 = list()
for i in range(1, len(r_peaks113), 1):
    rr113.append((r_peaks113[i] - r_peaks113[i-1]) * 2.76923077)

print("212", np.mean(rr212), rmssd212, sdnn212)
print("113", np.mean(rr113), rmssd113, sdnn113)

f1 = plt.figure(1)
plt.plot(ecg212[0:10800])
plt.suptitle('ECG Sample 212')
f2 = plt.figure(2)
plt.plot(ecg113[0:10800])
plt.suptitle('ECG Sample 113')
plt.show()
