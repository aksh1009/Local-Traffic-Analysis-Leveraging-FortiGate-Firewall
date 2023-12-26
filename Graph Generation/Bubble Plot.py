import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns  # For color palette

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Replace with actual column names
time_column = 'time'
received_packets_column = 'rcvdpkt'
sent_packets_column = 'sentpkt'

# Convert the 'time' column to datetime format
df[time_column] = pd.to_datetime(df[time_column], errors='coerce')

# Use Seaborn's color palette for purple colors
colors = sns.color_palette('PuRd', n_colors=2)

# Bubble plot with time on the x-axis, bubble size represents the count of packets
plt.scatter(df[time_column], df[sent_packets_column], s=df[sent_packets_column], color=colors[0], label='Sent Packets', alpha=0.5)
plt.scatter(df[time_column], df[received_packets_column], s=df[received_packets_column], color=colors[1], label='Received Packets', alpha=0.5)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Packet Count')
plt.title('Bubble Plot of Sent and Received Packets Over Time')
plt.legend()

# Format the x-axis as HH:mm
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Show the plot
plt.show()
