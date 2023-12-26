import csv
import os

# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Specify the absolute path for the CSV file
csv_file_path = os.path.join(current_directory, 'fortigate_logs.csv')

# Open the input and output files
with open('testlogs.txt', 'r') as log_file, open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header to CSV file
    csv_writer.writerow(['date', 'time', 'id', 'itime', 'euid', 'epid', 'dsteuid', 'dstepid', 'logver', 'type',
                         'subtype', 'level', 'action', 'policyid', 'sessionid', 'srcip', 'dstip', 'srcport',
                         'dstport', 'trandisp', 'duration', 'proto', 'sentbyte', 'rcvdbyte', 'sentpkt', 'rcvdpkt',
                         'logid', 'service', 'app', 'appcat', 'srcintfrole', 'dstintfrole', 'dstserver', 'eventtime',
                         'dstmac', 'masterdstmac', 'srcintf', 'dstintf', 'tz', 'devid', 'vd', 'dtime', 'itime_t', 'devname'])

    # Process each log entry
    for log_entry in log_file:
        # Split the log entry into fields
        fields = log_entry.strip().split()

        # Check if there are at least 44 fields (adjust the number accordingly)
        if len(fields) >= 44:
            # Extract values from fields
            date = next((field.split('=')[1] for field in fields if field.startswith('date=')), '')
            time = next((field.split('=')[1] for field in fields if field.startswith('time=')), '')
            id = next((field.split('=')[1] for field in fields if field.startswith('id=')), '')
            itime = next((field.split('=')[1][1:-1] for field in fields if field.startswith('itime=')), '')
            euid = next((field.split('=')[1] for field in fields if field.startswith('euid=')), '')
            epid = next((field.split('=')[1] for field in fields if field.startswith('epid=')), '')
            dsteuid = next((field.split('=')[1] for field in fields if field.startswith('dsteuid=')), '')
            dstepid = next((field.split('=')[1] for field in fields if field.startswith('dstepid=')), '')
            logver = next((field.split('=')[1] for field in fields if field.startswith('logver=')), '')
            type = next((field.split('=')[1][1:-1] for field in fields if field.startswith('type=')), '')
            subtype = next((field.split('=')[1][1:-1] for field in fields if field.startswith('subtype=')), '')
            level = next((field.split('=')[1][1:-1] for field in fields if field.startswith('level=')), '')
            action = next((field.split('=')[1][1:-1] for field in fields if field.startswith('action=')), '')
            policyid = next((field.split('=')[1] for field in fields if field.startswith('policyid=')), '')
            sessionid = next((field.split('=')[1] for field in fields if field.startswith('sessionid=')), '')
            srcip = next((field.split('=')[1] for field in fields if field.startswith('srcip=')), '')
            dstip = next((field.split('=')[1] for field in fields if field.startswith('dstip=')), '')
            srcport = next((field.split('=')[1] for field in fields if field.startswith('srcport=')), '')
            dstport = next((field.split('=')[1] for field in fields if field.startswith('dstport=')), '')
            trandisp = next((field.split('=')[1][1:-1] for field in fields if field.startswith('trandisp=')), '')
            duration = next((field.split('=')[1] for field in fields if field.startswith('duration=')), '')
            proto = next((field.split('=')[1] for field in fields if field.startswith('proto=')), '')
            sentbyte = next((field.split('=')[1] for field in fields if field.startswith('sentbyte=')), '')
            rcvdbyte = next((field.split('=')[1] for field in fields if field.startswith('rcvdbyte=')), '')
            sentpkt = next((field.split('=')[1] for field in fields if field.startswith('sentpkt=')), '')
            rcvdpkt = next((field.split('=')[1] for field in fields if field.startswith('rcvdpkt=')), '')
            logid = next((field.split('=')[1] for field in fields if field.startswith('logid=')), '')
            service = next((field.split('=')[1][1:-1] for field in fields if field.startswith('service=')), '')
            app = next((field.split('=')[1][1:-1] for field in fields if field.startswith('app=')), '')
            appcat = next((field.split('=')[1][1:-1] for field in fields if field.startswith('appcat=')), '')
            srcintfrole = next((field.split('=')[1][1:-1] for field in fields if field.startswith('srcintfrole=')), '')
            dstintfrole = next((field.split('=')[1][1:-1] for field in fields if field.startswith('dstintfrole=')), '')
            dstserver = next((field.split('=')[1] for field in fields if field.startswith('dstserver=')), '')
            eventtime = next((field.split('=')[1] for field in fields if field.startswith('eventtime=')), '')
            dstmac = next((field.split('=')[1][1:-1] for field in fields if field.startswith('dstmac=')), '')
            masterdstmac = next((field.split('=')[1][1:-1] for field in fields if field.startswith('masterdstmac=')), '')
            srcintf = next((field.split('=')[1][1:-1] for field in fields if field.startswith('srcintf=')), '')
            dstintf = next((field.split('=')[1][1:-1] for field in fields if field.startswith('dstintf=')), '')
            tz = next((field.split('=')[1][1:-1] for field in fields if field.startswith('tz=')), '')
            devid = next((field.split('=')[1][1:-1] for field in fields if field.startswith('devid=')), '')
            vd = next((field.split('=')[1][1:-1] for field in fields if field.startswith('vd=')), '')
            dtime = next((field.split('=')[1][1:-1] for field in fields if field.startswith('dtime=')), '')
            itime_t = next((field.split('=')[1] for field in fields if field.startswith('itime_t=')), '')
            devname = next((field.split('=')[1][1:-1] for field in fields if field.startswith('devname=')), '')

            # Write the values to the CSV file
            csv_writer.writerow([date, time, id, itime, euid, epid, dsteuid, dstepid, logver, type, subtype, level, action,
                                policyid, sessionid, srcip, dstip, srcport, dstport, trandisp, duration, proto, sentbyte,
                                rcvdbyte, sentpkt, rcvdpkt, logid, service, app, appcat, srcintfrole, dstintfrole, dstserver,
                                eventtime, dstmac, masterdstmac, srcintf, dstintf, tz, devid, vd, dtime, itime_t, devname])

# Notify the user about the location of the CSV file
print(f"CSV file created at: {csv_file_path}")




