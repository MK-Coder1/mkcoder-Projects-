marks = [3,5,7,"Mohit","Naveen",12,232,23,45,435,43,54,90]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# nagative statement
# print(marks[-3])#Nagatie index
# print(marks[len(marks)-3])#Positive index
# print(marks[5-3])#Positive index
# print(marks[2])#Positive index

# if 6 in marks:
#     print("Yes")
# else:
#     print("No")

# if "Mohit" in marks:
#     print("Yes")
# else:
#     print("No")
    
# print(marks)
# print(marks[1:])
# print(marks[1:-1])
# print(marks[1:-3])
# print(marks[1:8])
# print(marks[1:8:2])

# lst = [i for i in range(4)]
# print(lst)

lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)