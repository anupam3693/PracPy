'''
To get change with minimal currency denominnations
'''
curr_deno = [500,100, 50, 20, 10, 5, 2, 1]
change = []
x = 343
j=1

for i in curr_deno:
    print(x//i)
    print(x%i)

    #while quotient is non zero
    if  x >= i:
        print(i,x)
        change.append(str(i)*(x//i))
        x = x%i
        print(change)
