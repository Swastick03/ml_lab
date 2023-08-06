queue=[]

queue.append('d')
queue.append('s')
queue.append('v')
queue.append('k')
queue.append('c')

print(queue)

queue.pop()
queue.pop()

print(queue)

if len(queue)==0:
    print("Queue is Empty")
else:
    print("Queue is not empty")