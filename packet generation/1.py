from scapy.all import IP, ICMP, send

# Craft ICMP echo request packet
packet = IP(dst="172.16.0.5") / ICMP()

# Send the packet 1000 times, suppressing Scapy's output
send(packet, count=1000, verbose=False) 
