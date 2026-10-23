# replace pi with 3.14
# Given a string containing lowercase English characters, 
# replace every occurrence of the substring "pi" with "3.14".
# The replacement must be done for every occurrence of "pi" in the string.
# You may solve this problem using recursion or iteration (loop).
# 1 < = str.length() < = 10^5 str contains only lowercase English letters. 
# "pi" may occur zero or more times. Every non-overlapping occurrence of "pi" must be replaced.

def replacePi(s: str) -> str:
    return s.replace("pi","3.14")