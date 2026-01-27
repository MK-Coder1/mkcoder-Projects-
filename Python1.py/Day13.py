#strings are immutable
a = "Mohit"
print(len(a))
#all letters big size
print(a.upper())
#all letters small size
print(a.lower())

#kisi bhi traling charcture ko rmove kerta hai 
b = "Mohit!!!!!!!!"
print(b)
print(b.rstrip("!"))
#kisi bhi letter ko replace kerta hai
print(a.replace("Mohit"," Khanakiya"))

#kisi bhi words ke bhich spavce bnata hai 
print(b.split(" "))

#first letter ka word bid size ka ker deta hai.
blogHeading = "introduce to my blog."
print(blogHeading.capitalize())

#space ko users ke acording bdhata hai. 
str1 = "Welcome to my website"
print(len(str1))
print(len(str1.center(50)))

#letter ko count kerta hai ki vo kitni bar string me aaya hai.
print(b.count("Mohit"))

#true ya flase me answer deta hai.
print(str1.endswith("!!!"))


