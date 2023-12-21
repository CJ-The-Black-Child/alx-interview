#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys


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
        data = line.split()
        if len(data) < 2:
            continue
        if data[-2] in status_codes:
            status_codes[data[-2]] += 1
        total_size += int(data[-1])
        if count % 10 == 0:
            print_status(status_codes, total_size)
except KeyboardInterrupt:
    print_status(status_codes, total_size)
    raise
finally:
    print_status(status_codes, total_size)
