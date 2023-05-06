from itertools import takewhile

s = "S->iEtS|iEtSeS|a"

def groupby(ls):
    d = {y: [i for i in ls if i.startswith(y)] for y in set(l[0] for l in ls)}
    return d

def prefix(x):
    return len(set(x)) == 1

starting, rules, common, alphabetset = "", [], [], list("ABCDEFGHIJKLMNOPQRSTUVWXYZ'")

s = s.replace(" ", "").replace("	", "").replace("\n", "")
starting, rules = s.split("->")
rules = rules.split("|")

common = [''.join([l[0] for l in takewhile(prefix, zip(*group))]) for _, group in groupby(rules).items()]

for i in common:
    newalphabet = alphabetset.pop()
    print(f"{starting}->{i}{newalphabet}")
    index = [k.replace(i, "", 1) or "\u03B5" for k in rules if k.startswith(i)]
    print(f"{newalphabet}->" + "|".join(index))
