import numpy as np
import biosppy.signals

# Load The Dataset From .txt File
data = np.loadtxt('2023-10-26-17-30-4440Secondecg.txt')

# Find ECG Signal
r_peaks_0 = biosppy.signals.ecg.ecg(signal=data, sampling_rate=200, show=True)['rpeaks'] # Define Function for ECG Signal from Biosppy Module
print("Find R-Peaks:\n", r_peaks_0) # Show The R Peaks
rr_intervals_0 = np.diff(r_peaks_0)/1000 # Calculate RR Intervals
print("Find RR-Interval:\n",rr_intervals_0) # Show The RR Intervals

# Using Engzee Segmenter
r_peaks_1 = biosppy.signals.ecg.engzee_segmenter(signal=data, sampling_rate=200, threshold=0.48) # Define Function for Engzee Segmenter from Biosppy Module
print("Find R-Peaks (Engzee Segmenter):\n", r_peaks_1) # Show The R Peaks
rr_intervals_2 = np.diff(r_peaks_1)/1000 # Calculate RR Intervals
print("Find RR-Interval (Engzee Segmenter):\n",rr_intervals_2) # Print the RR intervals

# Using Christov Segmenter
r_peaks_3 = biosppy.signals.ecg.christov_segmenter(signal=data, sampling_rate=200) # Define Function for Christov Segmenter from Biosppy Module
print("Detected R-Peaks (Christov Segmenter):\n", r_peaks_3) #Show The R Peaks
rr_intervals_3 = np.diff(r_peaks_3)/1000 # Calculate RR Intervals
print("Detected RR-Interval (Christov Segmenter):\n",rr_intervals_3) # Show The RR Intervals

# Using Hamilton Segmenter
r_peaks_4 = biosppy.signals.ecg.hamilton_segmenter(signal=data, sampling_rate=200) # Define Function for Hamilton Segmenter from Biosppy Module
print("Find R-Peaks (Hamilton Segmenter):\n", r_peaks_4) #Show The R Peaks
rr_intervals4 = np.diff(r_peaks_4)/1000 # Calculate RR Intervals
print("Find RR-Interval (Hamilton Segmenter):\n",rr_intervals4) # Show The RR Intervals

# Using SSF Segmenter
r_peaks_5 = biosppy.signals.ecg.ssf_segmenter(signal=data, sampling_rate=200, threshold=20, before=0.03, after=0.01) # Define Function for SSF Segmenter from Biosppy Module
print("Find R-Peaks (SSF Segmenter):\n", r_peaks_5) #Show The R Peaks
rr_intervals_5 = np.diff(r_peaks_5)/1000 # Calculate RR Intervals
print("Find RR-Interval (SSF Segmenter):\n",rr_intervals_5) # Show The RR Intervals