#--------------------------------- List

names=["Ali","Zeeshan","Ahamd","Abbas"]
print(names.index("Ali"))
print(names.count("Ali"))
names.sort()
names.pop() # remove the last element
names.append("Khan") # add another element
names.insert(1,"Hamza") # add with respect to index
names.remove("Ali")
print(names)

names.clear() # Clear all data in a list
print(names)