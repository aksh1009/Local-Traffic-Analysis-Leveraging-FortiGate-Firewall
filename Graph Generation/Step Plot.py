import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Filter out logs with action "client-rst"
df = df[df['action'] != 'client-rst']

# Check for NaN values and drop them
df = df.dropna(subset=['time', 'sentpkt', 'rcvdpkt'])

# Check for duplicate values and drop them
df = df.drop_duplicates(subset=['time', 'sentpkt', 'rcvdpkt'])

# Sort DataFrame by 'time'
df['time'] = pd.to_datetime(df['time'])
df = df.sort_values(by='time')

# Plotting
fig, ax = plt.subplots()

# Step plot for sent packets
ax.step(df['time'], df['sentpkt'], where='post', label='Sent Packets', color='darkcyan')

# Step plot for received packets
ax.step(df['time'], df['rcvdpkt'], where='post', label='Received Packets', color='peru')

plt.xlabel('Time')
plt.ylabel('Packet Count')
plt.title('Step Plot: Sent and Received Packets over Time')
plt.legend()
plt.show()
