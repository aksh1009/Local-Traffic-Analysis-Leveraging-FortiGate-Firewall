import pandas as pd
import seaborn as sns
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

    # Create an area plot with custom colors
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='time', y='sentpkt', data=df, label='Sent Packets', color='green')
    sns.lineplot(x='time', y='rcvdpkt', data=df, label='Received Packets', color='purple')

    plt.fill_between(df['time'], df['sentpkt'], color='green', alpha=0.2)
    plt.fill_between(df['time'], df['rcvdpkt'], color='purple', alpha=0.2)

    plt.xlabel('Time')
    plt.ylabel('Packet Count')
    plt.title('Area Plot of Time vs Sent and Received Packets')
    plt.legend()

    # Format x-axis labels as HH:mm
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
