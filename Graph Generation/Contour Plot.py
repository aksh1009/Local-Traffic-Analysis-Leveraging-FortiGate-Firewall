import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Replace 'fortigate_logs.csv' with the actual path to your CSV file
csv_file_path = 'fortigate_logs.csv'

# Read Fortigate data from CSV
df = pd.read_csv(csv_file_path)

# Drop rows with missing values in 'rcvdpkt'
df = df.dropna(subset=['rcvdpkt'])

# Convert 'time' to timestamp
df['time'] = pd.to_datetime(df['time'], errors='coerce')
df['time'] = df['time'].astype(np.int64) // 10**9  # Convert to seconds

# Use 'time' as the x-axis, 'sentpkt' as the y-axis, and 'rcvdpkt' as the z-axis
x = df['time'].values
y = df['sentpkt'].values
z = df['rcvdpkt'].values

# Filter out non-finite values in 'z'
mask = np.isfinite(z)
x = x[mask]
y = y[mask]
z = z[mask]

# Set levels for the contour plot
levels = np.linspace(z.min(), z.max(), 7)

# Plot the contour plot
fig, ax = plt.subplots()

ax.plot(x, y, 'o', markersize=2, color='grey')
contour = ax.tricontourf(x, y, z, levels=levels, cmap='viridis')

# Add colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Received Packets')

ax.set(xlabel='Time (s)', ylabel='Sent Packets')

plt.title('Contour Plot for Fortigate Data')
plt.show()
