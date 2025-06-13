#else-if condition

# age=int(input('enter the age: '))
# print(age)
# if(age<=15):
#   print('teenager')
# elif(age>=16):
#   print('adult')
# else:
#   print('you are kid5')  
  
 ##nested if statements
 
 #we can use if else elif statement inside other if statement as well
num=-23
if(num==0):
  print('natural number') 
elif(num>=10):
  print('positive')
  if(num>10):
    print('11-20')
  else:('nothing')
elif(num<=10):
  print('1-10')
else:('just nested number')    