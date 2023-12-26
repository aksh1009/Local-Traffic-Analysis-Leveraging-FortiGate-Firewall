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
    # Calculate total sent and received packets
    total_sent = df['sentpkt'].sum()
    total_received = df['rcvdpkt'].sum()

    # Create a pie chart
    labels = ['Sent Packets', 'Received Packets']
    sizes = [total_sent, total_received]
    colors = ['lightskyblue', 'lightcoral']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Distribution of Sent and Received Packets')
    plt.show()
