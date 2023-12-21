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
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_status(status_codes, total_size)

        data = line.split()
        count += 1

        try:
            total_size += int(data[-1])
        except Exception:
            pass
        try:
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
        except Exception:
            pass
    print_status(status_codes, total_size)

except KeyboardInterrupt:
    print_status(status_codes, total_size)
    raise
