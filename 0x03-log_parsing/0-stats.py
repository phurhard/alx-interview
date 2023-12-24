#!/usr/bin/python3
import sys
import re

pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$')

status_codes = {}
total_size = 0
count = 0
for line in sys.stdin.readlines():
    # check if the line matchs
    match = pattern.match(line.strip())
    count +=1
    # if it matchs
    if match:
        #seperate them out
        ip_address, date, status_code, file_size = match.groups()
        total_size += file_size
        status_codes[status_code] = status_codes.status_code + 1
        if count == 10:
            print(f"File size: {total_size}")
            pass
    else:
        # if it does not match skip it
        continue

for line in sys.stdin.readlines():
    if line not "<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>":
        continue
    if count == 10 or ctrl-C:
        print('statistics from beginning')
        total_size += file_size
        if  not status_code or not isinstance(int, status_code)
        print(f'
              File size: {total_size}
              status_code : number of times it shows
              ')