#set is a non repetitive 
a={1,2,1,3,4,1}
print(a)
#important :this syntax will create an empty dictionary and not an empty set
a={}
print(type(a))
#an empty set can be created using below syntax:
a=set()
print(type(a))
#methods*************
a.add(11)#add
a.add(1111)
a.add(111)
a.add(11111)
print(a)
print(len(a))#length
a.remove(11)#remove
print(a)
a.pop()#remove one 
print(a)
a.clear()
print(a)
#find union 
A = {1, 3, 5, 7}
B = {'a', 'b', 'c', 'd'}
print(A.union(B))
print(B.union(A))
print(A.union(B) == B.union(A))
q={1,2,3,4}
w={2,1,4,4,5,6}
print(q.intersection(w))
print(w.intersection(q))


