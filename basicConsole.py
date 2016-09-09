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


def funcActionAnaliser(commandsList):
    pass

def funcActionReader():
    funcList = []
    while True:
        funcList.append(raw_input(''))
        if funcList[0] == 'return':
            break
    return funcList


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
# ---------- type parsers start
def prcInt(lst, dct):
    dct[lst[0]] = int(lst[2])
    return dct

def prcList(lst, dct):
    name = lst[0]                                                              
    for i in [0, 0, -1, -1, -1]: lst.pop(i)                                
    lst = list(map(lambda x: x.replace('[', '').replace(']', ''), ist)) 
    lst = list(map(lambda x: int(x.replace(',', '')),lst))            
    dct[name] = lst                                                        

def prcFunc(lst, dct):
    new = []                               
    tmp = lst[4:]                
    tmp[0] = tmp[0].replace('(','')  
    tmp[-1] = tmp[-1].replace(')','') 
    tmp = " ".join(tmp)                
    tmp = tmp.split(";")                
    for i in tmp:                      
        i = i.strip(' ')                
        new.append(i)                  
    actLst = funcActionReader()
    dct[strList[0]] = [new, actLst]               
    return dct
# --------- typeparsers end
            

def mainParser(strList):
    print (strList)

    if strList[-1] == "int":
        GDH = prcInt(strList, GDH)

    elif strList[-1] == "list":
        GDH = prcList(strList, GDH)

    elif strList[2] == "function":
        GDH = prcFunc(strList, GDH)              

    elif set(strList) & set(['+','-','*','/']):
        for val in GDH.keys():
            for empt in range(strList.count(val)):
                ind = strList.index(val)
                strList.pop(ind)
                strList.insert(ind, GDH[val])
        print strList   
        print operations(strList)
    
    elif strList[0] == 'head':
        if strList[2] in GDH.keys():
            if type(GDH[strList[2]]) == type([]):
                print (GDH[strList[2]][0])
            else: print ('{} not is list'.format(GDH[strList[2]]))
        else: print('uncnown variable') 
        
    elif strList[0] == 'tail':
        if strList[2] in GDH.keys():
            if type(GDH[strList[2]]) == type([]): 
                print (GDH[strList[2]][1:])
            else: print ('{} {} not is list'.format(type(GDH[strList[2]]), GDH[strList[2]]))
        else: print('uncnown variable') 

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


