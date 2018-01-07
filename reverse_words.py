from collections import deque
from copy import deepcopy

def reverse_words(arr):
    if arr is None or len(arr) == 0:
        return []
    
    d = deque()
    temp = deepcopy(arr)
    try:
        i = temp.index(" ")
    except ValueError:
        return arr
    
    while True:
        try:
            word = temp[:i]
            d.appendleft(word)
            d.appendleft(" ")
            temp = temp[i+1:]
            i = temp.index(" ")
        except ValueError:
            break
    d.appendleft(temp)
    answer = []
    for e in list(d):
        for c in e:
            answer.append(c)
    return answer

if __name__ == '__main__':
    a = reverse_words(['p','e','r','f','e','c','t',' ',
                   'm','a','k','e','s',' ',
                   'p','r','a','c','t','i','c','e'])
    print(a)

    b = reverse_words(["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"])
    print(b)

    c = reverse_words(['h','e','l','l','o'])
    print(c)
