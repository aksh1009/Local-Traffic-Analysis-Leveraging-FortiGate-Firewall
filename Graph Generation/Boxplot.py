import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Filter out logs with action "client-rst" if needed
df = df[df['action'] != 'client-rst']

# Check if DataFrame is empty or contains NaN values
if df.empty or df.isnull().values.any():
    print("Data is empty or contains missing values. Please check your CSV file.")
else:
    # Select the relevant columns
    data_to_plot = [df['sentpkt'], df['rcvdpkt']]

    # Plotting
    fig, ax = plt.subplots()

    # Create a box plot with log scale on y-axis and adjusted box widths
    boxplot = ax.boxplot(data_to_plot, labels=['Sent Packets', 'Received Packets'], sym='o', widths=0.5, patch_artist=True)

    # Set y-axis scale to log
    ax.set_yscale('log')

    # Set y-axis ticks to 1, 10, and 100
    ax.set_yticks([1, 10, 100])

    # Customize box colors
    colors = ['blue', 'yellow']
    for box, color in zip(boxplot['boxes'], colors):
        box.set_facecolor(color)

    # Customize outlier colors
    for flier in boxplot['fliers']:
        flier.set(marker='o', color='black', alpha=1)

    plt.xlabel('Packet Type')
    plt.ylabel('Number of Packets (log scale)')
    plt.title('Box Plot: Sent and Received Packets')

    plt.show()
