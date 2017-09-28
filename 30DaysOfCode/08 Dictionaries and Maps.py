n = int(input())
dictionary = {}  

for i in range(1, (n + 1)):
    dict = input().strip().split(' ')   #creates a list of strings from each line of input 
    dictionary[dict[0]] = int(dict[1])  #adds a Key: value pair to the dictionary
    
j = n + 1
query = input().strip()
while query != '':
    if query in dictionary:
        print(query + '=' + str(dictionary[query]))
    else:
        print('Not found')
    j = j + 1
    query = input().strip()
