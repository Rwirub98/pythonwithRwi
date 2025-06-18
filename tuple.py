a=(1,)
print(type(a))

n=(912,34,'hdjsf',21,44,2)
# n[1]=2 throws error cos its immutable 
print(n)

print(n[1:4])


n2=n[2:3]
print(n2)



# operation in tuple

state=('assam', 'magaland',' manipur','tripura')
change=list(state)
print(type(change))

change.append('odissa')#add new item
print(change)

change.pop(1)#remove item
print(change)

change[2]='nagaland'#pushing item in mention index
print(change)

state=tuple(change)
print(type(state))

