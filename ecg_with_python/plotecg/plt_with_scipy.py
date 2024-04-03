import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def plot_ecg_from_txt(filename):
    with open(filename, 'r') as file:
        ecg_data = np.array([float(line.strip()) for line in file.readlines()])

    sampling_rate = 1000 
    time = np.arange(len(ecg_data)) / sampling_rate

    desired_sampling_rate = 1
    resampled_time = np.arange(0, len(ecg_data) / sampling_rate, 1 / desired_sampling_rate)
    cs = CubicSpline(time, ecg_data)
    resampled_ecg_data = cs(resampled_time)

    normalized_ecg_data = (resampled_ecg_data - np.min(resampled_ecg_data)) / (np.max(resampled_ecg_data) - np.min(resampled_ecg_data))
    normalized_ecg_data = 2 * normalized_ecg_data - 1

    plt.figure(figsize=(10, 6))
    plt.plot(resampled_time, normalized_ecg_data, color='blue')
    plt.title('ECG Data')
    plt.xlabel('Time (s)')
    plt.ylabel('ECG Amplitude')
    plt.grid(True)
    plt.show()

plot_ecg_from_txt('2023-10-26-17-30-4440Secondecg.txt')