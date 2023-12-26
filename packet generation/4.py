from scapy.all import IP, ICMP, UDP, TCP, send

# Craft ICMP, UDP, and TCP packets
icmp_packet = IP(dst="172.16.0.5") / ICMP()
udp_packet = IP(dst="172.16.0.5") / UDP(dport=53)
tcp_packet = IP(dst="172.16.0.5") / TCP(dport=80)

# Send each packet type 500 times
send([icmp_packet, udp_packet, tcp_packet], count=500, verbose=False)
