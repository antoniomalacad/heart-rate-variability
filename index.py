import numpy as np
import matplotlib.pyplot as plt
import pathlib
from ecgdetectors import Detectors
from hrv import HRV

fs = 360
detectors = Detectors(fs)
rawcsv = np.loadtxt(open("212.csv", "rb"), dtype=int,
                    delimiter=",", skiprows=1)
print("Finished reading csv")

ecg = rawcsv[:, 1]  # ecg only
r_peaks = detectors.pan_tompkins_detector(ecg)

myHRV = HRV(360)
rmssd = myHRV.RMSSD(r_peaks)
sdnn = myHRV.SDNN(r_peaks)

dist = list()
for i in range(1, len(r_peaks), 1):
    dist.append((r_peaks[i] - r_peaks[i-1]) * 2.76923077)

# plt.hist(dist, bins=25)

plt.plot(ecg[r_peaks[0]:r_peaks[10]])
plt.title('ECG Sample')
plt.show()
