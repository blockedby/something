
objects = [1, 2, 1, 5, True, False, True, 'false', {}, [1,2], [1,2]]
ans = []
for obj in objects: # доступная переменная objects
    if type(obj) not in ans:
        ans.append(type(obj))
print(len(ans))

print(len({id(i) for i in objects}))