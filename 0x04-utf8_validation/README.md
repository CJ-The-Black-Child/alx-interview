# Topic: UTF-8 Validation
This project contains a Python method that checks if a list of integers represents a valid UTF-8 encoding.

## Task Completed
+ [x] 0. **UTF-8 Validation**: Implements a function `validUTF8` that checks if a list of integers are valid UTF-8 codepoints.

## Function Details
The `validUTF8` function checks if a list of integers are valid UTF-8 codepoints. A character in UTF-8 can be 1 to 4 bytes long. The data set can contain multiple characters. The data will be represented by a list of integers. Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.

## Usage
```python
data = [65]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
