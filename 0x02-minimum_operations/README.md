# Title: Minimum Operation

## Description
This Python script calculates the fewest number of operations needed to result in exactly `n` 'H' characters in a text file. The text editor can execute only 2 operations in this file: Copy All and Paste.

## Method
The function `minOperations(n)` computes the minimum number of operations. It works by dividing `n` by its smallest factors one at a time. This is equivalent to "copying" the current number of 'H' characters and "pasting" them as many times as possible (which is the factor). The number of operations is then the sum of these factors.

## Usage
```python
from min_operations import minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

Requirements
Python 3.x

Author
[Congo J Migue]