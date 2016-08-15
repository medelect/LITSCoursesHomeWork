from collections import Counter
import mytimer


name = 'SourseFile'
#a = Counter(i   for line in open(file).readlines() for i in line.rstrip().split(" "))

def handler(_file):
    return Counter(i for line in open(_file).readlines() for i in line.rstrip().split(" "))

a = mytimer.timer(handler,name)
print(sum(a[1].values()))
print(a[1].most_common()[:-10:-1] )
print(a[0])
