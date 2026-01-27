#string slicing
names = "Mohit, Naveen"
#0 se leker jitne letter print kerne hai vo no. likhne (n-1) for example [0:5]n=5 .
print(names[0:5])

#length ke liye (letter count kerne ke liye)
print(len(names))

fruit = "Mango"
len1 = len(fruit) 
print("Mango is a",len1, "letter word.")

MangoLen = len(fruit)
print(MangoLen)
print(fruit[0:4])#including 0 but not 4
print(fruit[2:5])#including 2 but not 5
print(fruit[0:-3])#including 0 but not -3
print(fruit[0:len(fruit)-3])
print(fruit[-3:-1])#2:4#including -3 but not -1

#Quick Quize
mn = "Khanakiya"
print(mn[-4:-2])