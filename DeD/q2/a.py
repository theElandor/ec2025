import sys
def add(a,b):
    X1, Y1 = a
    X2, Y2 = b
    return [X1 + X2, Y1 + Y2]

def mul(a,b):
    X1, Y1 = a
    X2, Y2 = b
    return [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]

def div(a,b):
    X1, Y1 = a
    X2, Y2 = b    
    return [X1 // X2, Y1 // Y2]

#A=[25,9]
#A=[157,59]
result = [0,0]
for x in range(3):
    result = mul(result, result)
    result = div(result, [10,10])
    result = add(result, A)
print(result)