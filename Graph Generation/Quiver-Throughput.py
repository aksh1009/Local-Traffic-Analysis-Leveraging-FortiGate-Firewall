import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Replace with actual column names
time_column = 'time'
received_bytes_column = 'rcvdbyte'
sent_bytes_column = 'sentbyte'

# Convert the 'time' column to datetime format
df[time_column] = pd.to_datetime(df[time_column], errors='coerce')

# Use Seaborn's color palette for a colorful scheme
colors = sns.color_palette('dark', n_colors=5)

# Calculate the differences in sent and received bytes
df['delta_sent_bytes'] = df[sent_bytes_column].diff()
df['delta_received_bytes'] = df[received_bytes_column].diff()

# Calculate throughput (bytes per second)
df['throughput'] = (df['delta_sent_bytes'] + df['delta_received_bytes']) / df[time_column].diff().dt.total_seconds()

# Create a quiver plot for throughput
plt.figure(figsize=(15, 8))

# Scale the quiver plot for better visibility
scale_factor = 4000  
y_scale_factor = 100 

plt.quiver(
    df[time_column], 
    df[received_bytes_column], 
    df['delta_sent_bytes'], 
    df['delta_received_bytes'], 
    scale=scale_factor,
    color=colors[0], 
    label='Throughput Flow'
)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Received Bytes')
plt.title('Quiver Plot for Throughput Over Time')
plt.legend()

# Add grids
plt.grid(True)

# Adjust axis limits for better visibility
plt.xlim(df[time_column].min(), df[time_column].max() + pd.Timedelta('1 hour'))  # Extend the x-axis limit
plt.ylim(0, df[received_bytes_column].max() + y_scale_factor)

# Show the plot
plt.show()
