import sys
memo = {}
def add(a,b):
    X1, Y1 = a
    X2, Y2 = b
    return [X1 + X2, Y1 + Y2]

def mul(a,b):
    X1, Y1 = a
    X2, Y2 = b
    return [(X1 * X2 - Y1 * Y2), (X1 * Y2 + Y1 * X2)]

def div(a,b):
    X1, Y1 = a
    X2, Y2 = b    
    return [int(X1 / X2), int(Y1 / Y2)]

def is_engraved(point):
    result = [0,0]
    for x in range(100):
        result = mul(result, result)
        result = div(result, [100000,100000])
        result = add(result, point)
        for coord in result:
            if coord > 1000000 or coord < -1000000:
                return False
    return True

A=[-21673,67997]
points = []
mask = []
for oy in range(0, 1001):
    for ox in range(0, 1001):
        p = (A[0]+ox, A[1]+oy)
        if is_engraved(p):
            mask.append(True)
        else:
            mask.append(False)
        points.append(p)

for i in range(1001):
    for j in range(1001):
        if(mask[i*1001 + j]):
            print("x", end = "")
        else:
            print(".", end="")
    print("\n")

print(len([x for x in mask if x == True]))