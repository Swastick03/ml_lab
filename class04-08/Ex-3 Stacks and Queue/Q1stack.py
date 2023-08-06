a=[]
a.append(5)
a.append(2)
a.append(8)
a.append(3)
a.append(9)
print(a)

a.pop()
a.pop()
print(a)

if len(a)==0:
    print("Stack is empty")
else:
    print("Stack is not empty")