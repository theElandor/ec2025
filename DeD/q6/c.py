import sys
from collections import defaultdict
filename = sys.argv[1]
def mentor(letter, list):
    prefix = []
    current = 0
    for l in letters:
        if l == letter:
            current += 1
        prefix.append(current)
    ans = 0
    for i,x in enumerate(letters):
        if x == letter.lower():
            ans += prefix[i]
    return ans

with open(filename) as f:
    letters = f.read().strip()
    wlen = 2000
    repeat = 1000
    sequence = letters*repeat
    window = defaultdict(int)
    ans = 0
    current_wlen = wlen // 2
    for i in range(wlen//2):
        window[sequence[i]] += 1
    for i in range(len(sequence)):
        current = sequence[i]
        if i <= wlen//2:
            current_wlen += 1
        else:
            if current_wlen < wlen:
                current_wlen +=1
            else:
                # remove backwards element
                old = sequence[i-1-wlen//2]
                window[old] -= 1
        try:
            window[sequence[i+wlen//2]] += 1
        except:
            pass
        if current.islower():
            ans += window[current.upper()] 
    print(ans)