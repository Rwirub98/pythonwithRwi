x=int(input('enter the value of x : '))
match x :
  case 0 :
    print('x is zero')
  case 1 :
    print('not zero')
  case 19:
    print('x is a teenage')  
  case _ if(x!=0):
    print('not matching')
 
  
    