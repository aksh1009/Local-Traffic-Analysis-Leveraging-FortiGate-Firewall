import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a Pandas DataFrame
csv_file_path = 'fortigate_logs.csv'
df = pd.read_csv(csv_file_path)

# Filter out logs with action "client-rst"
df = df[df['action'] != 'client-rst']

# Check if DataFrame is empty or contains NaN values
if df.empty or df.isnull().values.any():
    print("Data is empty or contains missing values. Please check your CSV file.")
else:
    # Convert 'time' to datetime format
    df['time'] = pd.to_datetime(df['time'], errors='coerce')

    # Calculate 'bandwidth' as the sum of 'sentbyte' and 'rcvdbyte'
    df['bandwidth'] = df['sentbyte'] + df['rcvdbyte']

    # Use the 'pastel' color palette
    pastel_palette = sns.color_palette('pastel')

    # Create a colorful violin plot for 'bandwidth' over time
    plt.figure(figsize=(12, 6))
    sns.violinplot(x=df['time'].dt.strftime('%H:%M'), y=df['bandwidth'], palette=pastel_palette)

    plt.xlabel('Time')
    plt.ylabel('Bandwidth')
    plt.title('Violin Plot: Bandwidth over Time')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility

    plt.tight_layout()
    plt.show()
