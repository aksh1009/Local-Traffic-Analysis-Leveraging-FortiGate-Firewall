from scapy.all import IP, TCP, send

# Craft TCP packet to port 80 (HTTP)
tcp_packet = IP(dst="172.16.0.5") / TCP(dport=80)

# Send the TCP packet 1000 times
send(tcp_packet, count=1000, verbose=False)
