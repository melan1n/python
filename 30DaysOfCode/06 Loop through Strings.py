N = int(input())

for n in range(1,(N+1)):
    line = input().strip()

    line_even = ''
    line_odd = ''

    i = 0
    for char in line:

        while i < len(line):
            if (i % 2) == 0:
                line_even = line_even + line[i]
            else:
                line_odd = line_odd + line[i]
            i = i + 1
        
    print(line_even+' '+line_odd)
