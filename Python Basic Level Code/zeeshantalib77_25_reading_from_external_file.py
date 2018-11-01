#---------------------------------- Reading from external file

name_file=open("zeeshantalib77.txt","r") # r means read ,a means append,w write
print(name_file.read())  # readable(), readline(), read()[1]
for names in name_file.readline():
    print(names)
#name_file.write("\nAli - Khan")
name_file.close()

