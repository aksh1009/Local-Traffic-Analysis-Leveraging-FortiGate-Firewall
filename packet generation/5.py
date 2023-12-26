from scapy.all import IP, TCP, send

    # Craft FTP TCP packet
    ftp_packet = IP(dst="172.16.0.5") / TCP(dport=21)

    # Send the packet 1000 times
    send(ftp_packet, count=1000, verbose=False)
