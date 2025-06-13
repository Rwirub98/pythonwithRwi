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
# num=2
# if(num==0):
#   print('natural number') 
# elif(num>=10):
#   print('positive')
#   if(num>10):
#     print('11-20')
#   else:('nothing')
# elif(num<=10):
#   print('1-10')
# else:('just nested number')    


## exercise
import time
timestamp=int(time.strftime('%H'))
print(timestamp)
if(timestamp>=11):
  print('goodMoring sir')
elif(timestamp>=15):
  print('goodAfternoon sir')
elif(timestamp>=19):
  print('goodEvening sir')
else:'goodNight sir'    

