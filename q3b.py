def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    n1 = a[2:]
    n2 = b[2:]
    res = ""
    carry = 0
    
    
    i = len(n1) - 1 
    j = len(n2) - 1

    while i >= 0 or j>= 0 or carry:
        if (i >=0 and n1[i] == '1'):
            b1 = 1
        else:
            b1 = 0
        
        if (j >=0 and n2[j] == '1'):
            b2 = 1
        else:
            b2 = 0
        
        current = b1 + b2 + carry
        digit = current % 2 
        carry = current // 2
        
        res = str(digit) + res
        i -= 1 
        j -= 1 
        
    if res != "0" and res[0] == "0":
        while len(res) > 1 and res[0] == '0':
            res = res[1:]

    return "0b" + res        