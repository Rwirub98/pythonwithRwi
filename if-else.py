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
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
# print(timestamp)
if(hour>=0 and hour<12):
  print('goodMoring sir')
elif(hour<=12 and hour<16):
  print('goodAfternoon sir')
elif(hour>=17 and hour<23):
  print('goodEvening sir')
else:
  print('good night sir')
   

