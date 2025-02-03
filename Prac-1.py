print("\nStrings in Python")
a = 'This is a string 1'
print (a)
b = "This is a string 2"
print (b)
c= '''This is a string 3'''
print (c)

print("\n List Operations")
L = [64, 'Chirag Nagvekar',0+7]
print(L)
L.append(" Python Lab")
print(L)
L.reverse()
print(L)
L.remove(9)
print(L)
print("Lenght of List: ",len(L))

print("\nTuples Operations")
tup1 = (15, "C", "Python", 99+1)
print(tup1)
print(tup1[2])
tup2 = (1000, 2000)
combineTuple= tup1 + tup2
print(combineTuple)
print("Length od Tuple: ",len(combineTuple))

print("\nDictionary Operations")
dict1 = {1: 'Hi', 2: 'I', 3: 'am', 4:'Chirag'}
print(dict1)
print("Accessing element: ",dict1[4])
dict2= dict ({1:'I', 2: 'am', 3: 'in', 4:'PLab'})
print(dict2)
dict1[4]="Jarvis"
print("Accessing element: ",dict2.get(4))
print("Updated dict1:", dict1,"\n")