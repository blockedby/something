mySpcs = {"global":[] } #global, child namespaces
myVars = {"global":set()}
print()
# https://stepik.org/lesson/24460/step/10?unit=6766
def get(namespace, var):
    pass
def add(namespace, var):
    pass
def create(namespace, parent) :
    pass
def finditem(obj, key):
    if key in obj:
        return obj[key]
def ui():
    i = int(input())
    global myVars
    while i>0:
        cmd, namesp, arg = input().split()
        if cmd == "create": #create <namespace> <parent> 
            pass
        elif cmd == "add":  #add <namespace> <var>
            pass
        else:       #get    #get <namespace> <var>
            pass
        myNamesp(cmd, namesp, arg)
        i-=1


# @ outister
# 2 года назад
# Ссылка
# Задачка прикольная!

# 1. Я решил все делать в 1 словаре namesp. Я сделал его вида, 
# как таблицы в mongo_db или json запросы. Во пример вложенных пространств
#  имено global, foo, bar:


# namesp = {
#     'global': {
#         'parent': None,
#         'vars': set('a'),
#         'foo': {
#             'parent': 'global',
#             'vars': set('b'),
#             'bar': {
#                 'parent': 'foo', 
#                 'vars': set('a')}
#         }
#     }
# }

# 2. Количество команд считывал через n = int(input()). 
# Затем в цикле while n != 0 считывал команды, сразу деля
#  их на 3 переменные cmd, nmsp, var = input().split() и в 
# зависимости от if cmd == я выполнял ту или иную функцию и передавал
#  в нее остальные 2 переменные nmsp и var.

# 3. У меня было 3 основные функции 
# - def get(namespace, var),
# - def add(namespace,var),
#     a['vars'].add(var)
# - def create(namespace, parent)
#     a[namespace] = {'parent':parent, 'vars':set()}

# 4. Для создания окружения я использовал рекурсивную функцию, 
# которая ищет ключ словаря который будет родительским пространством для нового.
# def finditem(obj, key):
#     if key in obj:
#         return obj[key]
# etc
# 5. Для поиска переменных я создал рекурсивную функцию 
# def findvar(obj, namespace, var):
#     if namespace in obj:
#         if var in obj[namespace]['vars']:
#             return namespace
# etc

# 6. Можно было объединить 2 рекурсивные функции, но мне было лень. Итого 61 строчка понятного и читаемого кода в соответствии с pep8.

# Удачи.