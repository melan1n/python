T = int(input())
i = 1

result = 'Prime'

while i <= T:
    n_str = input().strip()
        
    if int(n_str) == 1:
        result = 'Not prime'
    
    elif int(n_str) == 2:
        result = 'Prime'    
    
    elif int(n_str) % 2 == 0:
        result = 'Not prime'
    
    elif int(n_str) < 10000:
        m = 3
        while m < int(n_str):
            if int(n_str) % m == 0:
                result = 'Not prime'
                break                
            else:
                m += 2
    else:
        m = 3
        while m < (2*10**9)**0.5:
            if int(n_str) % m == 0:
                result = 'Not prime'
                break                
            else:
                m += 2                
        
    print (result)
    result = 'Prime'
    i += 1
    
  
