import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Replace with actual column names
time_column = 'time'
received_packets_column = 'rcvdpkt'
sent_packets_column = 'sentpkt'

# Convert the 'time' column to datetime format
df[time_column] = pd.to_datetime(df[time_column], errors='coerce')

# Use Seaborn's color palette for a colorful scheme
colors = sns.color_palette('dark', n_colors=5)

# Calculate the differences in sent and received packets
df['delta_sent'] = df[sent_packets_column].diff()
df['delta_received'] = df[received_packets_column].diff()

# Create a quiver plot
plt.figure(figsize=(15, 8))

# Scale the quiver plot for better visibility
scale_factor = 6000

# Adjust y-axis scale for better visibility
y_scale_factor = 400

plt.quiver(
    df[time_column], 
    df[received_packets_column], 
    df['delta_sent'], 
    df['delta_received'], 
    scale=scale_factor,
    color=colors[0], 
    label='Packet Flow'
)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Received Packets')
plt.title('Quiver Plot for Packet Flow Over Time')
plt.legend()

# Add grids
plt.grid(True)

# Adjust axis limits for better visibility
plt.xlim(df[time_column].min(), df[time_column].max())
plt.ylim(0, df[received_packets_column].max() + y_scale_factor)

# Show the plot
plt.show()
