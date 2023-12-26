import pandas as pd
import matplotlib.pyplot as plt

# Replace with actual column names
time_column = 'time'
sent_byte_column = 'sentbyte'
received_byte_column = 'rcvdbyte'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('fortigate_logs.csv')

# Convert the 'time' column to datetime format
df[time_column] = pd.to_datetime(df[time_column], errors='coerce')

# Set 'time' as the index for better plotting
df.set_index(time_column, inplace=True)

# Plotting the stacked area plot
plt.figure(figsize=(15, 8))

# Stackplot for 'sentbyte' and 'rcvdbyte'
plt.stackplot(df.index, df[sent_byte_column], df[received_byte_column], labels=['Sent Bytes', 'Received Bytes'], alpha=0.7)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Bytes')
plt.title('Stacked Area Plot for Sent and Received Bytes')
plt.legend()

# Show the plot
plt.show()
