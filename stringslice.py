#String slicing

name = "Thulasi"
print(name[:])
print(name[1:5])
print(name[5:])
print(name[:4])
print(name[2:6])

#negative index
a = "thulasi"
print(a[-4:-1])
print(a[:-4])
print(a[:-1])

#list data type
#implicit
attendees =["Thulasi","latha","hari"]
print(type(attendees))
#explicit
attendees = list(("Thulasi","latha","hari"))
print(type(attendees))
#data tyoe/variable annotation
attendees:list = list(("Thulasi","latha","hari"))
print(type(attendees))
attendees:list = ["Thulasi","latha","hari"]
print(type(attendees))

#accesing a string
attendees:list = ["Thulasi","latha","hari"]
print(attendees[0])
print(attendees[-2:])

#reverse a string without slicing
name = "Thulasi"
print(name[::-1])

#reverse a string without slicing
a = "Thulasi"
b = ""
for i in a:
    b = i+b
print(b)

#reverse of a list item
attendees:list = ["Thulasi","latha","hari"]
print(attendees[::-1])