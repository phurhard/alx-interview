#!/usr/bin/python3
"""This is a sample of the interview question,
where we log the output of a server"""

import sys
import re

pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - '
                     r'\[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" '
                     r'(\d+) (\d+)$')

status_codes: dict = {}
total_size = 0
count = 0
for line in sys.stdin:
    # check if the line matchs
    match = pattern.match(line.strip())
    count += 1
    # if it matchs
    if match:
        # seperate them out
        ip_address, date, status_code, file_size = match.groups()
        total_size += int(file_size)
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
        try:
            if count == 10:
                print(f"File size: {total_size}")
                for k, v in dict(sorted(status_codes.items())).items():
                    print(f'{k}: {v}')
                count = 0
        except KeyboardInterrupt:
            print(f"File size: {total_size}")
            for k, v in dict(sorted(status_codes.items())).items():
                print(f'{k}: {v}')
    else:
        # if it does not match skip it
        continue
