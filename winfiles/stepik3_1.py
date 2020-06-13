nmsps = {"global":"None"} # Пространство»: «Родитель
varies = {"global":[], "None":[]}
def add(namespace, varieble): # добавить в пространство <namespace> переменную <var>
    global nmsps
    global varies
    varies[namespace].append(varieble)
def create(namespace, parent): # создать новое пространство имен с именем <namespace> внутри пространства <parent
    global nmsps
    global varies
    nmsps[namespace]=parent
    varies[namespace]=[]
def get(namespace, varieble):
    global nmsps
    global varies
    if varieble in varies[namespace]:
        print(namespace)
    else:
        if  namespace == "None":
            print("None")
        else:
            get(nmsps[namespace],varieble)
def userInterface(a = 0):
    while a>0:
        cmd, namesp, arg = input().split()
        if cmd == "create":
            create(namesp, arg)
        elif cmd == "add":
            add(namesp, arg)
        else:
            get(namesp, arg)
        a+=-1
    return a
userInterface(int(input()))

# сука работает