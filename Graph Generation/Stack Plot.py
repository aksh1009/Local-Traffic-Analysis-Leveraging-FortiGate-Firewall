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
    df['time'] = pd.to_datetime(df['time'], errors='coerce')

    # Group by time and sum the values
    grouped_df = df.groupby('time').sum()

    # Plotting
    fig, ax = plt.subplots()

    # Stack plot for sent and received packets
    labels = ['Sent Packets', 'Received Packets']
    colors = ['green', 'lightgreen']
    ax.stackplot(grouped_df.index, grouped_df['sentpkt'], grouped_df['rcvdpkt'], labels=labels, colors=colors)

    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Number of Packets')
    plt.title('Stack Plot: Sent Packets and Received Packets')

    # Add legend
    ax.legend(loc='upper left')

    # Set the x-axis locator and formatter
    locator = mdates.MinuteLocator(interval=10)
    formatter = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    

    plt.show()
