import sys
filename = sys.argv[1]


with open(filename) as f:
    moves = [int(x) for x in f.read().split(",")]
    nails = 256
    x1 = moves[0]
    lines = []
    knots = 0
    for i in range(1, len(moves)):
        x2 = moves[i]
        for y1, y2 in lines:
            # check previous lines
            if x1 == y1 or x1 == y2 or x2 == y1 or x2 == y2:
                continue
            prev_found = None
            for index in range(1,nails+1):
                # x1,x2, y1, y2 are for sure different.
                if index in [x1,x2]:
                    if prev_found == "x":
                        break
                    prev_found = "x"
                elif index in [y1,y2]:
                    if prev_found == "y": 
                        break
                    prev_found = "y"
            else:
                knots += 1
        lines.append((x1,x2))
        x1 = x2
    print(knots)
            
        

       

