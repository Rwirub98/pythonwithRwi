#break if we use the break condition , if stops or skip the loop immediatly and print the output 
for i in range (13):
  if (i==10):
   break
  print("2 x", i+1 ,'=', 2*(i+1))
  
  ##continue, if we use that it skips the mention value and contiue looping
  
  
for i in range(10):
  if(i==4):
    continue
  print(i)