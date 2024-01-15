#!/usr/bin/env python3
"""This is a sample of the interview question,
where we log the output of a server

import sys
import re

status_codes: dict = {}
total_size = 0
count = 0
# line = sys.stdin.readline()
# print(line)
for line in sys.stdin.readlines():
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

        print(line)

        continue
"""
import sys


cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
