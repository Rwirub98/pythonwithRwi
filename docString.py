# python docString are the string literals that appear right after the definition of a function ,class , modules.
# example:
  
def square(n):
  '''takes in a number n, returns the square of n'''
  return n**2


print(square(5))  
print(square.__doc__)