# count vowels
# Given a string s, count and return the total number of vowels in it. 
# Vowels are the characters 'a', 'e', 'i', 'o', 'u' in both uppercase and lowercase.

def countVowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count