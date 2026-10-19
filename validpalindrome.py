# valid palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Given a string s, return True if it is a palindrome, or False otherwise.

def isPalindrome(S: str) -> bool:
    S = ''.join(ch.lower()for ch in S if ch.isalnum())
    return S == S[::-1]