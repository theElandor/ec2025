import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().split("\n\n")
    names = data[0].split(",")
    lines = data[1].splitlines()
    wrong = set()
    all_names = set(names)
    for name in names:
        print(name)
        name_valid = True
        for x,y in zip(name[:-1], name[1:]):
            sill_valid = False
            for rule in lines:
                left, right = rule.split(" > ")
                right = right.split(",")
                if x == left and y in right:
                    sill_valid = True
                    break
            if not sill_valid:
                wrong.add(name)
                break
    print(all_names - wrong)