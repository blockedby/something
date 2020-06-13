nemes = dict.fromkeys(["None"])
nemes["None"] = [{"global":[]}]
# {'None': ['global': "" ]}
nemes["None"][0]["global"].append('s:[]')
def userInterface(a = 0):
    while a>0:
        cmd, namesp, arg = input().split()
        myNameSp(cmd,namesp,arg)
        a-=1
    return a
def myNameSp(cmd,namesp,arg):
    global nemes
    if cmd == "create":
        create()
    elif cmd == "add":
        add()
    else:
        get()
    def create(parent, child):
        global nemes
        nms = nemes
        def searchParent(parent, child):
            for key in nms.keys:
                if key == parent:
                    return parent #returns list of
                else:
                    for values in key:
                        searchParent(parent,child)

    def add():
        pass
    def get():
        pass
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, 
# или None, если такого пространства не существует
userInterface(int(input()))