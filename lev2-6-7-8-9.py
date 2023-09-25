"""
Unpack the list
"""
#7. a,b , a= the first index , b = rest of the list
a ,*b = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha','tito']
print(a)
print(b)
print("=====================================================================")

#8. a = the first index , b = the last index
a ,*c ,b= ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha','tito']
print(a)
print(b)
print("=====================================================================")

#9. a = the first index , b = the second index
a ,b ,*_= ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha','tito']
print(a)
print(b)