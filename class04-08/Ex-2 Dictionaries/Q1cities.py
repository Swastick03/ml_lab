city={"balasore":65675,"jaipur":76557,"bhopal":76869,"cuttack":75738,"patna":56735}


# a)
a={"surat":87363,"ranchi":93732}
city.update(a)
print(city)


# b)
b=list(city.keys())
c=list(city.values())
print("The City with maximum population: ",b[c.index(max(c))],", population = ",max(c))



# c)

if "london" in city.keys():
    print("Yes , London is in the list.")
else:
    print("No london is not there")
    
    
# d)

city.pop("patna")
print(city)