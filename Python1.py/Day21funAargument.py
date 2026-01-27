# def average(a=9, b=1):
#     print("The average is", (a+b)/2)
    
    
#     # average(4, 6)
# average(5, 1)


# def average(a, b, c=8):
#     print("The average is", (a+b+c)/2)
    
    
def average(*numbers):
       print(type(numbers))
       sum = 0
       for i in numbers:
           sum = sum+i
    #    print("Average is:",sum/len(numbers))
    # return 7 
    # hmesa retrun first wala hi use/work kere ga
       return sum/len(numbers)
  
    
#     # average(4, 6)
c = average(5, 5,4,8)
print(c)
# average(b=9)
# average(b=9, a=21)

# def name(fname, mname = "Mohit", lname = "Khanakiya"):
#     print("Hello,",fname,mname,lname)
    
# name("Mohit","ji")


# dictionary value
# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name ["lname"])
# name(mname = "Buchanan", lname = "Barnes", fname = "James")