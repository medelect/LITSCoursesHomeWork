lst = [10,2,[3,[4,5],6],79,[[9,9,9]],33]
lstOut = []
def handle(var):
    for i in var:
        if type(i) == type(int()):
            lstOut.append(i)
            print i
        else:
            handle(i)
    #return lstOut
    

handle(lst)

lst += [555]

print(lst)
print(lstOut)
def f():
    print('f')
    print(lst)
f()
