from collections import Counter

file = 'SourseFile'
a = Counter(i   for line in open(file).readlines() for i in line.rstrip().split(" "))
print(sum(a.values()))
print(a.most_common()[:-10:-1] )