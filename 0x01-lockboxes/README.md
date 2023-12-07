# Title: Lockboxes

## Description
This project contains a Python method `canUnlockAll(boxes)` that determines if all the boes can be opened. The boxes are numbered sequentially from 0 to n-1 and each box may contain keys to the other boxes. A key with the same number as a box opens that box. The first box `boxes[0]` is unlocked.

## Requirements
* Python 3.7+
* Ubuntu 20.04 LTS

## Files
The repository's directory contains the following file:
1. `0-lockboxes.py`: This is the main Python script that contains the `canUnlockAll(boxes)`, method.

## Usage
You can import the `canUnlockAll(boxes)` method from the `0-lockboxes.py` file into your Python script and use it as follows:

``` python
canUnlockAll = __import__('0-lockboxes').canUnlockAll
boxes = [[1], [2], [3]. [4], []]
print(canUnlockAll(boxes))

<!-- Explanation-->
## Solution
The solution uses a depth-first search approach. It starts from the first box and gets as deep as possible by following the keys found in each box. When it can't go any further, it backtracks and continunes with the next key. This approach is more efficient because it doesn't need to keep track of visited boxes separately and it doesn't need to check if all boxes  are unlocked at each step. Instead, it checks if all boxes are unlocked at the end, which is faster.

## Output
The `canUnlockAll(boxes)` method returns `True` if all boxes can be opened, else it returns `False`.

## Author
Congo J Migue