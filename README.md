# PracPy
1. How we can mutate string? We can mutate string object by using list as well as :
string[:position]+character+string[position+1:]

2. Testing String for different types:
    s = input().strip()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))
        
        OR
    
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print (any(method(c) for c in s))

3. def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    
4. 

