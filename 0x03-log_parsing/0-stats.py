#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys
import re


def print_status(code_dict, total_size):
    """
    Prints the total file size and status code occurrences.
    """
    print(f"File size: {total_size}")
    for code in sorted(code_dict.keys()):
        if code_dict[code]:
            print(f"{code}: {code_dict[code]}")


status_codes = {
    str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]
}
total_size = 0

try:
    for count, line in enumerate(sys.stdin, start=1):
        match = re.search(r'\"GET /projects/260 HTTP/1.1\" (\d+) (\d+)', line)
        if match:
            status_code, file_size = match.groups()
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += int(file_size)
        if count % 10 == 0:
            print_status(status_codes, total_size)
except KeyboardInterrupt:
    print_status(status_codes, total_size)
    raise
finally:
    print_status(status_codes, total_size)
