# #string lines

# fruit='apple'
# print(fruit)

# argu='he said, "i want to play kabaddi"' #single line string
# print (argu)

# para= '''hfkjw vs jhefi  
# ksdnfkjhsf 
# jkldsnc 
# djfosidhjf 
# jlsdhjdfoiwjef
# hvolsh 
# p9w3uqwiopdj 
# anfb whfiow hoifhowign ''' #multiline string
# print (para)


# #forlooping in string


# name='swargiary'
# print(name[0])
# # for character in name:
# #  print(character)
 
 
 
#  # string slicing & operation on string
 
# print(len(name))

# print(name[0:5]) # [start:end]
# print(name[:7])# start from 0 index and end is start from 1 indexing.
# print(name[:])

# nm='harry'
# print(nm[-4:-1])# here negative slicing , we substrat from the len of the variable, if both side has negative then we will perform same operation in both side

# ###########################################################################
# #  string methods

# #lower and upper case method

var = "Rwi"
print(var.upper())
print(var.lower())

#rstrip (removes any unwanted character)
fruit="apple!"
print(fruit.rstrip("!"))

fruits="!!!!!apple!"
print(fruits.rstrip("!"))# deosnt remove the leading unwanted character


#split ( if there is gap between strings or instance then it will convert the string into list element in a string form)
a="manw bidi jakhw jeneba  ang baywlwi bdba "
print(a.split(" "))

#capitalize( make the first letter upper, and remaining smaller. if the first character is already upper then there will be no change) )
b="gfiwecubikavcboquhdoqnc"
print(b.capitalize())

c="GfiwecubikavcboquHdoqnc"
print(c.capitalize())

# replace(replace the existed string with diff string)
print(fruit.replace('apple!', 'banana'))

#center( align the string)
print(len(fruit))
print(len(fruit.center(20)))

#count( here we do count the existing of the string or  repeating )
print(b.count('c'))

#endswith(it checks it ends with the given value with it or not and gives the result in true false)
print(b.endswith('g'))
print(b.endswith('ub', 6,8))

#find(used to find the string but it search only for first occurance and remaining even if exits and if coudnt find it will print -1)
i= "we know he has gone mad but still we can try and give him chance, if he will "
print(i.find('know'))

#index(similar to find but throws an error while gap shows -1)
print(i.index('x'))



 