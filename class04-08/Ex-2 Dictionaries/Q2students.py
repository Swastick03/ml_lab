students={"abhi":45,"saras":87,"barsa":76,"megha":98}

# a)
a={"candan":66}
students.update(a)
print(students)


# b)
print("Average marks:",sum(students.values())/5)


# c)

b=list(students.keys())
c=list(students.values())
print("The Student with highest marks is: ",b[c.index(max(c))] )

# d)

d=dict(sorted(students.items()))
print(d)