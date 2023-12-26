import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

    # Create a scatter plot for both sent and received packets over time
    fig, ax = plt.subplots()

    # Scatter plot for sent packets
    ax.scatter(df['time'], df['sentpkt'], color='yellow', label='Sent Packets')

    # Scatter plot for received packets
    ax.scatter(df['time'], df['rcvdpkt'], color='yellowgreen', label='Received Packets')

    # Format x-axis as HH:mm
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    plt.xlabel('Time')
    plt.ylabel('Packet Count')
    plt.title('Scatter Plot: Sent and Received Packets over Time')
    plt.legend()

    ax.grid(True)  # Add grids

    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.tight_layout()
    plt.show()
