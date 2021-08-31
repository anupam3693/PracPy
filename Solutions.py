# 1-python-lists-English.pdf
if __name__ == '__main__':
    N = int(input())
    l = []
    # print(N)
    for _ in range(N):
        s = input().split()
        if s[0] == 'insert':
            l.insert(int(s[1]), int(s[2]))
        if s[0] == 'print':
            print(l)
        if s[0] == 'remove':
            l.remove(int(s[1]))
        if s[0] == 'append':
            l.append(int(s[1]))
        if s[0] == 'sort':
            l.sort()
        if s[0] == 'pop':
            l.pop()
        if s[0] == 'reverse':
            l.sort(reverse=True)

# Better Solution 1
n = input()
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)

# Better Solution 2
L = []
for _ in range(int(input())):
    command, *args = input().split()
    try:
        getattr(L, command)(*(int(x) for x in args))
    except AttributeError:
        print(L)

# to find 2nd highest from the list of integers
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]

    z = max(arr)
    while max(arr) == z:
        arr.remove(max(arr))

    print(max(arr))

#better way and it can be nth highest or lowest
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    a = set()
    for i in arr:
        a.add(i)
    print(type(a))

    b = sorted(arr)[1]
    for i in arr:
        if i == b:
         print(i)


#2-nested-list-English
if __name__ == '__main__':
    score_set = set()
    lst = []
    names = []
    N = int(input())
    if 2 <= N <= 5:
        for _ in range(N):
            name = input()
            score = float(input())
            lst.append([name, score])
            score_set.add(score)

        second_lowest = sorted(score_set)[1]

        for i in lst:
            if second_lowest == i[1]:
                names.append(i[0])
        names.sort()

        for i in names:
            print(i)
    else:
        print("Incorrect N")

#list comprehension
print(len(set([input() for i in range(int(input()))])))

# a and b are sets
print(sum([(i in a) - (i in b) for i in range(n)]))

# Set problem
n = int(input())
s = set(map(int, input().split()))
m = int(input())
for  i in range(m):
    attr, *kw = input().split()
    if kw:
        getattr(s,attr)(*(map(int, *kw)))
    else:
        getattr(s,attr)()
print(sum(s))

#my solution
for i in range(n):
    m = list(input().split())
    if len(m) > 1:
     eval('a.'+m[0]+'('+ m[1]+')')
    else:
     eval('a.' + m[0])
print(sum(a))

# eval with .format
eval('s.{0}({1})'.format(*input().split()+['']))

# to come out of the loop when the condition is matched
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tset = set()
        x_loop_must_break = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                # print('i-{}  j-{}'.format(i,j))

                if i!=j:
                    if (nums[i]+nums[j])==target:
                        tset.update([i,j])
                        x_loop_must_break =True
                        break
            if x_loop_must_break: break
        return list(tset)

a = Solution()
a.twoSum()

#working with defaultdict()
from collections import defaultdict

m, n = list(map(int, input().split()))
dict = defaultdict(list)
for i in range(m):
    dict[input()].append(i + 1)
for i in range(n):
    print(*dict[input()] or [-1])

# dictionary with iterables
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)

# multiple word search
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    tmp = []
    tmpindex = []
    for h,i in zip(range(len(doc_list)),doc_list):
        tmp = [j.rstrip('.,').lower() for j in i.split()]
        if keyword in tmp:
           tmpindex.append(h)

    return tmpindex

def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

doc_list = [['The Learn Python Challenge Casino', 'They bought a car', 'Casinoville?'], []]
keywords = ['casino', 'they']
print(multi_word_search(doc_list, keywords))


#implementing string element case swapping
def swap_case(s):
    return  ''.join([''.join(i.lower()) if i.isupper() else i.upper() for i in s])
        #s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#split_and_join
def split_and_join(line):
    a = line.split(' ')
    return '-'.join(i for i in a)


# OrderedDict
from collections import OrderedDict

n = int(input())
lst = []
fdict = OrderedDict()
for i in range(n):
    lst = list(input().split())
    # print(lst)
    tmpstr = " ".join(lst[:-1])
    price = int(lst[-1])

    if not fdict.get(tmpstr):
        fdict[tmpstr] = price
    else:
        new_price = fdict[tmpstr] + price
        fdict[tmpstr] = new_price

# print(fdict)
for item in fdict.items():
    print(item[0], item[1])


# Word Order
from collections import OrderedDict

words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())


# Maximum % value of sum of squares of given input.
from itertools import product
'''
input
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

output
206
'''
K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
# p = product(*N)
# print(*p)
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

#to sort an array by a kth column
for row in sorted(arr, key=lambda row:row[k]):
        print(*row)

# to check numbers are positive as well any one is palandromic
n=int(input())
a = input().split()
print(any(i == i[::-1] for i in a) & all(int(j)>0 for j in a) )

# Sorting1234
# sort lower, upper, by odd number and then even numbers
s=input()
lstlower=[]
lstupper=[]
lstodd=[]
lsteven=[]

for i in s:
    if i.islower():
        lstlower.append(i)
    elif i.isupper():
        lstupper.append(i)
    elif int(i)%2 == 1:
        lstodd.append(i)
    elif int(i) % 2 == 0:
        lsteven.append(i)

a=sorted(lstlower)+sorted(lstupper)+sorted(lstodd)+sorted(lsteven)

#Alternative one liner code
print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

