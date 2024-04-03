import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np

file_path = "2023-10-26-17-30-4440Secondecg.txt"

ecg_data = np.loadtxt(file_path)
signals, info = nk.ecg_process(ecg_data, sampling_rate=500)
nk.ecg_plot(signals, info)

plt.show()