from scapy.all import IP, UDP, send

# Craft UDP packet to port 53 (DNS)
udp_packet = IP(dst="172.16.0.5") / UDP(dport=53)

# Send the UDP packet 1000 times
send(udp_packet, count=1000, verbose=False)
