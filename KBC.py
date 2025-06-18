# 1. create a program capable of displaying questions to the user like KBC.
# 2. use list data type of store the questions and their correct answer.
# 3. display the final amount of the person is taking home after playing the game.

q='who is the prime minister'

A='narendra modi'
B='karan singh'
C='monomohan singh'
D='rajput rajit'

print(q)
print('A:', A)
print('B:', B)
print('C:', C)
print('D:', D)

answer= input('enter the correct answer')
if (answer == 'A'):
  print("correct answer , you have won 1 cr...!!!!")
elif(answer=='B'):
  print ('oops you lost 7cr!!!')
else:
  print('oops you lost 7cr!!! ')