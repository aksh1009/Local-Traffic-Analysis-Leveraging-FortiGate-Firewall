import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Filter out logs with action "client-rst"
df = df[df['action'] != 'client-rst']

# Check if DataFrame is empty or contains NaN values
if df.empty or df.isnull().values.any():
    print("Data is empty or contains missing values. Please check your CSV file.")
else:
    # Convert 'time' to datetime format
    df['time'] = pd.to_datetime(df['time'], errors='coerce')

    # Sort DataFrame by 'time'
    df = df.sort_values(by='time')

    # Convert 'time' to string for categorical plotting
    df['time_str'] = df['time'].dt.strftime('%H:%M')

    # Define custom color bins with smaller ranges
    bins = [0, 10, 20, 50, 100, 150, 200, 300, 400, np.inf]
    labels = ['0-10', '10-20', '20-50', '50-100', '100-150', '150-200', '200-300', '300-400', '400+']

    # Add a new column for color bin labels for sent packets
    df['sentpkt_bin'] = pd.cut(df['sentpkt'], bins=bins, labels=labels, include_lowest=True)

    # Add a new column for color bin labels for received packets
    df['rcvdpkt_bin'] = pd.cut(df['rcvdpkt'], bins=bins, labels=labels, include_lowest=True)

    # Calculate the sum of sent packets for each bin
    sentpkt_sum = df.groupby('sentpkt_bin')['sentpkt'].sum()
    # Filter out categories with 0 sum
    sentpkt_sum = sentpkt_sum[sentpkt_sum != 0]

    # Calculate the sum of received packets for each bin
    rcvdpkt_sum = df.groupby('rcvdpkt_bin')['rcvdpkt'].sum()
    # Filter out categories with 0 sum
    rcvdpkt_sum = rcvdpkt_sum[rcvdpkt_sum != 0]

    # Define custom colors for both pie charts
    custom_colors_sent = ['#ffcc99', '#c2c2f0', '#ffb3e6', 'plum', 'lightgreen', '#ff9999', 'skyblue', 'lightgray', 'wheat']
    custom_colors_rcvdpkt = ['#ffcc99', '#c2c2f0', '#ffb3e6', 'plum', 'lightgreen', '#ff9999', 'skyblue', 'lightgray', 'wheat']

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plotting a colorful pie chart with custom colors for sent packets
    axes[0].pie(sentpkt_sum, labels=sentpkt_sum.index, autopct='%1.1f%%', colors=custom_colors_sent, startangle=140)
    axes[0].set_title('Distribution of Sent Packets')

    # Plotting a colorful pie chart with custom colors for received packets
    axes[1].pie(rcvdpkt_sum, labels=rcvdpkt_sum.index, autopct='%1.1f%%', colors=custom_colors_rcvdpkt, startangle=140)
    axes[1].set_title('Distribution of Received Packets')

    # Equal aspect ratio ensures that pies are drawn as circles
    axes[0].axis('equal')
    axes[1].axis('equal')

    plt.show()
