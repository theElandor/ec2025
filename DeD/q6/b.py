import sys
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
    print(sum([mentor('A',letters), mentor('B',letters), mentor('C', letters)]))