#curd operations
#create  / add data to list

lst = ["Thulasi",1,True]
print(lst)

#Append()

lst :lst=["Thulasi","latha","hari"]
lst.append("tendu")
print(lst)

#insert()
attendees=["Thulasi","latha","hari"]
attendees.insert(3,"tendu")
print(lst)

#count

attendees =["Thulasi","latha","hari","hari"]
print(attendees.count("hari"))
print(attendees.count("abc"))

#index()

attendees = ["Thulasi","latha","tendu","tendu"]
print(attendees.index("Thulasi"))

#count()

attendees=["Thulasi","latha","hari","latha"]
if(attendees.count("tendu")>0):
    print(attendees.index("tendu"))

#update by using index

attendees=["Thulasi","latha","hari"]
attendees[1]="Thulasi"
print(attendees)

#extend

attendees=["Thulasi","latha","hari"]
attendees1=["tendu"]
attendees.extend(attendees1)
print(attendees)

#delete

attendees=["Thulasi","latha","hari"]
attendees.remove("hari")
print(attendees)

#pop with index

attendees=["Thulasi","latha","hari","tendu"]
attendees.pop(3)
print(attendees)

#pop without index

attendees=["Thulasi","latha","hari","tendu"]
attendees.pop()
attendees.pop()
print(attendees)