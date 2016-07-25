

def funcFactory(param):
    tmp = 0
    if param == "int":
        tmp = lambda x: len(param)
    elif param == "string":
        tmp = lambda x: param[::-1]
    else:
        tmp = lambda x: "please enter correct value"
    return tmp
a = funcFactory("stringd")
print (a("string"))