
# Local Traffic Analysis Leveraging FortiGate Firewall

## Table of Contents

- [Overview](#overview)
- [Features](#features)
  - [Packet Generation](#packet-generation)
  - [Observation of FortiGate Firewall Logs](#observation-of-fortigate-firewall-logs)
  - [Data Analysis and Visualization](#data-analysis-and-visualization)
  - [Note: Only TCP Traffic in FortiGate Logs](#note-only-tcp-traffic-in-fortigate-logs)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Screenshots](#screenshots)
- [Conclusion](#conclusion) 

## Overview

This project focuses on local network traffic analysis using a FortiGate firewall. It includes packet generation, FortiGate log observation, and diverse visualizations for comprehensive network analysis.
FortiGate is a robust network security appliance designed to protect and secure networks against various cyber threats. It integrates firewall, antivirus, intrusion prevention, VPN, and other security features to provide comprehensive network protection.
## Features

### Packet Generation

- Employed Scapy for crafting and sending diverse packets.
- Scapy is a powerful Python library for crafting, sending, and receiving network packets, providing a flexible interface 
  for network protocol manipulation. It allows users to build custom packets for network analysis, testing, and security 
  purposes.
- Generated TCP, UDP, ICMP, FTP, SNMP, and SMTP packets for analysis.

### Observation of FortiGate Firewall Logs

- Monitored logs for actions, timestamps, and affected IP addresses.
- Accessing Log & Report: Log in to the FortiGate web interface and navigate to the "Log & Report" section. The exact location may vary depending on the FortiGate model and firmware version.

  ![WhatsApp Image 2023-12-27 at 09 05 32_8275d2dc](https://github.com/aksh1009/Local-Traffic-Analysis-Leveraging-FortiGate-Firewall/assets/143216212/98ed974f-d0db-440a-9569-5a37ec021960)

- Enabled logging of local traffic for analysis.
- Converting to Comma-Seperated Values(CSV) file.

### Data Analysis and Visualization

- Loaded FortiGate logs into Pandas DataFrame, applied filters, and checked for missing values or contains NaN values. Filter out logs with action "client-rst".
- Utilized various visualizations for network analysis using Matplotlib, Seaborn.
- In the visualizations, patterns, spikes, and anomalies in the network traffic data were analyzed to enhance anomaly 
  detection capabilities.

### Note: Only TCP Traffic in FortiGate Logs

**Issue:** Despite generating various protocols, FortiGate logs may exclusively capture TCP traffic.

**Possible Reasons:**
- Firewall configuration settings may prioritize TCP logging.
- Logging level or verbosity settings might filter out non-TCP traffic.
- Firewall policy rules could favor TCP over other protocols.
- Traffic filtering or dropping for non-TCP packets may occur.
- Limitations in recognizing certain packet formats or content.

**Resolution:** Review and adjust firewall settings, policies, and packet crafting to ensure proper logging of desired protocols. Consult FortiGate documentation for any specific limitations or considerations related to logging various protocols.

## Project Structure

- **`packet generation/`:** Contains Scapy code snippets for packet generation.
- **`fortigate_logs/`:** Includes downloaded FortiGate textfile logs, Code for conversion to CSV and the converted CSV 
                         Log file for further analysis.
- **`Visualizations/`:** Stores generated plots and graphs.
- **`graph_generation_codes/`:** Houses code snippets for visualization generation.

Feel free to explore specific folders for detailed code implementations and data files.

## Dependencies

Ensure the following Python packages are installed:

```bash
pip install scapy matplotlib seaborn pandas
```

## Screenshots





## Conclusion

*I was aware of the potential impact on the network and systems, and I ensured to have the necessary permissions for conducting such tests.*

This project provides a holistic approach to local traffic analysis, incorporating packet generation, firewall log observation, and diverse visualizations for effective network optimization and anomaly detection.

For further exploration or customization, refer to the specific folders in the project structure. Your contributions and feedback are welcome to enhance the functionality and effectiveness of this local traffic analysis project. Happy analyzing!
