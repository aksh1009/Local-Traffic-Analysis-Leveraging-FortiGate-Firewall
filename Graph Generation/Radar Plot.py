import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Replace with actual column names
received_packets_column = 'rcvdpkt'
sent_packets_column = 'sentpkt'
received_bytes_column = 'rcvdbyte'
sent_bytes_column = 'sentbyte'

# Calculate the sum of received and sent packets and bytes
received_packets_sum = df[received_packets_column].sum()
sent_packets_sum = df[sent_packets_column].sum()
received_bytes_sum = df[received_bytes_column].sum()
sent_bytes_sum = df[sent_bytes_column].sum()

# Define categories and values for radar plot
categories = ['Received Packets', 'Sent Packets', 'Received Bytes', 'Sent Bytes']
values = [received_packets_sum, sent_packets_sum, received_bytes_sum, sent_bytes_sum]

# Scale the values for better representation (log scale in this case)
values = np.log1p(values)  # Adding 1 to avoid log(0)

def radar_plot(categories, values, title='Radar Plot'):
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)

    # Repeat the first value to close the circle
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    # Plot the data
    plt.polar(angles, values, marker='o', linestyle='-', color='steelblue', label='Parameter Counts')
    plt.fill(angles, values, alpha=0.35)

    # Add labels to each point
    plt.thetagrids(np.degrees(angles[:-1]), labels=categories)

    plt.title(title)
    plt.legend()
    plt.show()

# Create a radar plot for received and sent packets and bytes
radar_plot(categories, values, title='Packet and Byte Radar Plot')
