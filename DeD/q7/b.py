import sys
filename = sys.argv[1]
def check_prefix(name, rules):
    for x,y in zip(name[:-1], name[1:]):
        sill_valid = False
        for rule in rules:
            left, right = rule.split(" > ")
            right = right.split(",")
            if x == left and y in right:
                sill_valid = True
                break
        if not sill_valid:
            return False
    return True

with open(filename) as f:
    data = f.read().split("\n\n")
    names = data[0].split(",")
    lines = data[1].splitlines()
    wrong = set()
    all_names = set([x+1 for x in range(len(names))])
    for i,name in enumerate(names):
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
                wrong.add(i+1)
                break
    print(sum(all_names - wrong))