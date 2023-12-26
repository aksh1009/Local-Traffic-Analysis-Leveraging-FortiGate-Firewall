import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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
    df['time'] = pd.to_datetime(df['time'])

    # Sort DataFrame by 'time'
    df = df.sort_values(by='time')

    # Plotting
    fig, ax = plt.subplots()

    # Plot line for 'sentpkt'
    ax.plot(df['time'], df['sentpkt'], marker='o', linestyle='-', color='black', label='Sent Packets')  # Orange color

    # Plot line for 'rcvdpkt'
    ax.plot(df['time'], df['rcvdpkt'], marker='o', linestyle='-', color='skyblue', label='Received Packets')  # Green color

    # Format the x-axis as HH:mm
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    plt.xlabel('Time')
    plt.ylabel('Packets')
    plt.title('Line Plot: Sent and Received Packets over Time')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.legend()
    plt.tight_layout()
    plt.show()
