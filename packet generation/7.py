from scapy.all import IP, TCP, send

    # Craft SMTP TCP packet
smtp_packet = IP(dst="172.16.0.5") / TCP(dport=25)

    # Send the packet 1000 times
send(smtp_packet, count=1000, verbose=False)
