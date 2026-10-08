#dic syntax collection of key and values
dic={
    "mahak":"code",
    "age":"24",
    "m":[100,22],
    "dict":{ "name":"mahak",
            "age":"25" }
  
    
}
dic["m"] =[24,33,22]
print(dic["m"]) 

 #unodered,mutable,indexed,cant contaion duplicate keys
dic["age"]=25
print(dic["dict"]["age"])
#dictonary method*********************************
#print the keys of dic. and values.
print(dic.keys())#only keys
print(dic.items())#key and value both
print(dic.values())#only values
#typecasting
print(list(dic.keys()))#dic change into list
print(tuple(dic.keys()))#dic change into tuple
#update dictionary***********
print(dic)
dicupdate={
    "lavish":"koko",
    #add value and rewritte or overlaping 
    "age":22
}
dic.update(dicupdate)
print(dic)
#get value returns key
print(dic.get("lavish"))
#this method if key isnt present so gave none value thats why we use get instead
print(dic["lavish"])