import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Filter out logs with action "client-rst"
df = df[df['action'] != 'client-rst']

# Check if DataFrame is empty or contains NaN values
if df.empty or df.isnull().values.any():
    print("Data is empty or contains missing values. Please check your CSV file.")
else:
    # Create a histogram for sent and received packets with logarithmic scale
    plt.hist([df['sentpkt'], df['rcvdpkt']], bins=20, color=['mediumorchid', 'plum'], label=['Sent Packets', 'Received Packets'], log=True)

    plt.xlabel('Packet Count')
    plt.ylabel('Frequency (Log Scale)')
    plt.title('Distribution of Sent and Received Packets')
    plt.legend()

    plt.show()
