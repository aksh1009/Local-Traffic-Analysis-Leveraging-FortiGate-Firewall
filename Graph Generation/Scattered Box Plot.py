import pandas as pd
import seaborn as sns
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
    # Set the style of seaborn
    sns.set(style="whitegrid")

    # Create a scattered boxplot for sent and received packets with wider boxes
    plt.figure(figsize=(12, 8))

    # Using the 'viridis' palette and different colors
    sns.boxplot(x="variable", y="value", data=pd.melt(df[['sentpkt', 'rcvdpkt']]), hue="variable", palette="viridis", showfliers=False, width=0.6)
    sns.stripplot(x="variable", y="value", data=pd.melt(df[['sentpkt', 'rcvdpkt']]), hue="variable", palette="Set2", dodge=True, alpha=0.7, marker='o', size=6)

    # Add labels and title
    plt.xlabel('Packet Type')
    plt.ylabel('Number of Packets')
    plt.title('Scattered Boxplot: Sent and Received Packets')

    # Set y-axis scale for better visibility
    plt.yscale('log')  # You can adjust this based on your preference

    plt.legend(title=None)  # Remove legend title

    plt.show()
