#!/usrbin/python

import __future__

GDH = {"stat": [1,'type']}

print("basicConsole application\n \
    created by Grutman Alex")

def baseInput():
    dataIn = raw_input(">>> ")
#    datain = input(">>> ")
    return dataIn.split(' ')


def funcArgParser(argList):
    funcArgHash = {}
    argCounter = 0
    for item in argList:
        argCnt += 1
        item = item.split(' ')
        funcArgHash[item[0]] = [argCnt, argList[-1]]


def action(arg1, arg2, actionType):
    assert (type(arg1) == type(arg2)), '@action@=> argument types not equal'
    assert (actionType in ['+','-','*','/']), '@action@=> uncnown action'
    
    result = 0
    if actionType == '*':
        result = arg1 * arg2
    if actionType == '/':
        result = arg1 / arg2
    if actionType == '+':
        result = arg1 + arg2            
    if actionType == '-':
        result = arg1 - arg2
    return result


def operations(strList):
    tmp = strList
    while len(tmp) > 1:
        for i in ['*','/','+','-']:
            if i in tmp:
                ind = tmp.index(i)
                tmpAct =  action(tmp[ind-1], tmp[ind+1], i) #try yeld
                tmp.pop(ind-1)
                tmp.pop(ind-1)
                tmp.pop(ind-1)
                tmp.insert(ind-1, tmpAct)
                break
    return tmp[0]
            

def mainParser(strList):
    print (strList)

    if strList[-1] == "int":
        GDH[strList[0]] = int(strList[2])
        print("int", strList[0], strList[2])

    elif strList[-1] == "list":
        strList[2] = strList[2].replace('(','')
        strList[-4] = strList[-4].replace(')','')
        GDH[strList[0]] = strList[2:-3]
        print("list", strList[0],strList[2:-3])

    elif len(strList) > 1 and strList[2] == "function":
        new = []
        tmp = strList[4:]
        tmp[0] = tmp[0].replace('(','')
        tmp[-1] = tmp[-1].replace(')','')
        tmp = " ".join(tmp)
        tmp = tmp.split(";")
        for i in tmp:
            i = i.strip(' ')
            new.append(i)
        GDH[strList[0]] = new
        print "function", strList[0], new    

    elif set(strList) & set(['+','-','*','/']):
        for val in GDH.keys():
            for empt in range(strList.count(val)):
                ind = strList.index(val)
                strList.pop(ind)
                strList.insert(ind, GDH[val])
        print strList   
        print operations(strList)

    else:
        print('uncnow command ', strList)
        return True
    return False

# fill choosed cells

while True:
    if mainParser(baseInput()):
        break

for j in GDH:
    print(j, GDH[j])


