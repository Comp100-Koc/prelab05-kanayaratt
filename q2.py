def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    change = True
    while change:
        change = False
        
        for i in range(len(s) -1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                change = True
                break
    return s