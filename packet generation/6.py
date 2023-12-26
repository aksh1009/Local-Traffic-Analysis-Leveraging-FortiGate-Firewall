from scapy.all import IP, UDP, SNMP, send

    # Craft SNMP UDP packet
snmp_packet = IP(dst="172.16.0.5") / UDP(dport=161) / SNMP()

    # Send the packet 1000 times
send(snmp_packet, count=1000, verbose=False)
