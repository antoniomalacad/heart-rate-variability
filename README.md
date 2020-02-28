# Heart Rate Variability

This was created during my time as a student at Code Chrysalis. <br />

This app uses a python script to extract ECG\* data from a csv file to analyze the ECG sample. It finds the R peaks of the sample, which can then be used to determine the RR intervals to calculate HRV\*\*.

### Background

With recent advancements in wearable technology, smartwatches such as the Apple Watch are capable of measuring electrocardiogram\* (ECG) signals. ECG measures the electrical output of the heart. This output can be mapped over time to determine the precise time between beats. The variation of the time between beats is called heart rate variability\*\* (HRV). HRV has been studied as a health metric for its correlation with autonomic activity, which has health and physiological implications [1].

I wished to explore possibility of extracting ECG data and analyzing it to determine HRV.

## Using Python Scripts

1. Ensure that you have [Python 3](https://www.python.org/downloads/) installed on your device.

2. Download the [MIT-BIH ECG Dataset](https://www.physionet.org/content/mitdb/1.0.0/) and place it in the root directory. Alternatively, you can use your own data in csv format.

3. Set the sampling rate (Hz) of your ECGz data or the provided data (360 Hz).

```python
fs = 360   #or your specified sampling frequency
```

4. Use the csv parser on the csv file you wish to extract data from.

```python
csvdata = np.loadtxt(open("file-name.csv", "rb"), dtype=int,
                       delimiter=",", skiprows=1)
```

5. Run the python script to conduct ECG and HRV analysis, as well as to generate a plot of the data.

## Acknowledegements

### Python Script Source

Python scripts for raw ECG analysis and HRV calculations: [Pypi](https://pypi.org/project/py-ecg-detectors/) and [Github](https://github.com/berndporr/py-ecg-detectors)

### Sample Data Source

Data samples used in this repository come from the [MIT-BIH Arrhythmia Database](https://www.physionet.org/content/mitdb/1.0.0/). <br/>
More information regarding the samples within the dataset can be found [here](https://archive.physionet.org/physiobank/database/html/mitdbdir/mitdbdir.htm).

### References

1. [Heart Rate Variability: Standards of Measurement, Physiological Interpretation, and Clinical Use](https://www.ahajournals.org/doi/full/10.1161/01.cir.93.5.1043) <br/>
2. [Electrocardiogram Sampling Frequency Range Acceptable for Heart Rate Variability Analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6085204/) <br/>
3. [An Overview of Heart Rate Variability Metrics and Norms](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5624990/) <br/>
4. [Heart Rate Variability – How to Analyze ECG Data](https://imotions.com/blog/heart-rate-variability/) <br/>
