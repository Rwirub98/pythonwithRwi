#converts one data to another data type
#it has tho different typcasting
# 1) implicit conversion
# 2) explicit conversion

# 1) implicit conversion: the conversion is done by the python interpreter itself depending on the value level. it converts lower value datatype into high value datatype
# 2) explicit conversion: done by the developer or the programmer and can convert according to our desired.

a=2
b=5.6
print (a+b)
print (type(a+b)) #implicit

a="21"
b="20"
print(int(a)+int(b))#we did addtion by changing the data while additioning
print(type(a+b))#but the still main data type will remain same (str)