import ecg_plot
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as ipt

def read_ecg_data(file_path):
  """
  Reads ECG data from a text file.

  Args:
      data_path (str): The path to the ECG data text file.

  Returns:
      tuple: A tuple containing the time values (in seconds) and the ECG amplitudes.
  """

  with open(file_path, "r") as f:
    data_lines = f.readlines()

  # Assuming one value per line (adjust if needed)
  timestamps = np.arange(len(data_lines))  # Create time values based on line count
  ecg_data = np.array([float(line.strip()) for line in data_lines])

  return timestamps, ecg_data

file_path = "2023-10-26-17-30-4440Secondecg.txt"

'''
ecg_data = np.loadtxt(file_path)

ecg_plot.plot_1(ecg_data, sample_rate=500, title = 'ECG')
ecg_plot.show()
'''