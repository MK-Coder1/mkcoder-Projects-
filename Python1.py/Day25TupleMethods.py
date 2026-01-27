countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")#add item
temp.pop(3)#remove item
temp[2] = "Finland"#change item
countries = tuple(temp)
print(countries)

countries = ("pakistan","Afganisthan","BanglDESH","SriLanka")
countries2 = ("Viatname","India","China")
SouthEastasia = countries + countries2
print(SouthEastasia)

tuple1 = (1,2,43,2,54,65,1,65,321,2,323,3,33,3)
res = tuple1.count(3)
print("Count of 3 in tuple1 is: ",res)


# Position of no.in tuples
tuple1 = (1,2,43,2,54,65,1,65,321,2,323,3,33,3)
# res = tuple1.index(3)
# res = tuple1.index(3,4,12)
res = len(tuple1)
print("Count of 3 in tuple1 is: ",res)