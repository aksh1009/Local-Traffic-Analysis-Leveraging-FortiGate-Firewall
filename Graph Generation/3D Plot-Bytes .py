import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.dates as mdates
import numpy as np

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Filter out logs with action "client-rst" if needed
df = df[df['action'] != 'client-rst']

# Check if DataFrame is empty or contains NaN values
if df.empty or df.isnull().values.any():
    print("Data is empty or contains missing values. Please check your CSV file.")
else:
    # Convert 'time' to datetime format
    df['time'] = pd.to_datetime(df['time'], errors='coerce')

    # Convert datetime to numerical representation
    df['time_num'] = mdates.date2num(df['time'])

    # Define a size factor for the dots
    size_factor = 50

    # Create a 3D plot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot for sent and received bytes with color gradient using 'viridis' colormap
    sc = ax.scatter(df['time_num'], df['sentbyte'], df['rcvdbyte'], c=df['sentbyte'] + df['rcvdbyte'], cmap='viridis', s=size_factor)

    ax.set_xlabel('Time')
    ax.set_ylabel('Sent Bytes')
    ax.set_zlabel('Received Bytes')
    ax.set_title('3D Plot: Sent and Received Bytes over Time')

    # Add colorbar
    cbar = fig.colorbar(sc, ax=ax, label='Byte Count')

    plt.show()
