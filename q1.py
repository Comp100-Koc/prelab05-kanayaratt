def is_palindrome(s):
    if len(s) < 2:
        return False
    
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1
    return True
    


def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    longest = ""
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            current = s[i:j]
            if is_palindrome(current):
                if len(current) > len(longest):
                    longest = current
                    
                    
    return longest
        