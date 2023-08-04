# List containing 5 countries
country=["india","china","russia","srilanka","brazil"]
print(country)

# a) Add two more countries
c = input("Enter 1st counrty: ")
country.append(c)
c = input("Enter 2nd counrty: ")
country.append(c)
print(country)

# b)Print third country in the list

print("The third country in the list is:",country[2])


# c)Sort the list in Alphbetical order

country.sort()
print(country)


# d) Check if country India is present or not

if "india" in country:
    print("Yes India is present in the list!")
else:
    print("No India is not present in the list!")