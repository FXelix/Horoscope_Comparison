
def add():
    print("ello")

def sub():
    return "helo"

x = 9

lis = {"test": [add, sub],
       "res": [add(), sub()]}

for i in lis.values():
    print(i)
def hi():
    for i in lis["test"]:
        return i

hi()
