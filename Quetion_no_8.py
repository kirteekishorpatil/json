# import json
# keys={"name","designation","age","salary"}
# value1={"neelam","programer","24","2400"}
# i=0
# my_dic1={}
# lenght=len(keys)
# while i<lenght:
#     new_dic={keys[i]:value1[i]}
#     my_dic1.update(new_dic)
#     i=i+1
# print(my_dic1)
# value2={"komal","trainer","24","20000"}
# k=0
# my_dic2={}
# lenght=len(keys)
# while k<lenght:
#     new_dic={keys[k]:value2[k]}
#     my_dic2.update(new_dic)
#     k=k+1
# print(my_dic2)
# value3={"anirudha","HR","25","40000"}
# s=0
# my_dic3={}
# lenght=len(keys)
# while s<lenght:
#     new_dic={keys[s]:value3[s]}
#     my_dic3.update(new_dic)
#     s=s+1
# print(my_dic3)
# value4={"Abhishek","manager","29","63000"}
# h=0
# my_dic4={}
# lenght=len(keys)
# while h<lenght:
#     new_dic={keys[h]:value4[h]}
#     my_dic4.update(new_dic)
#     h+h+1
# print(my_dic4)

import json
list1=["neelam","programer","24","2400",]
list2=["komal","trainer","24","20000",]
list3=["anuradha","HR","25","40000",]
list4=["Abhishek","manager","29","63000",]  
keys=["name","designation","age","salary",]
emp1={}
emp2={}
emp3={}
emp4={}
dict={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
for i in range(len(list1)):
    emp1.update({keys[i]:list1[i]})    
for j in range(len(list3)):
    emp2.update({keys[j]:list2[j]})
for k in range(len(list3)):
    emp3.update({keys[k]:list3[k]})
for l in range(len(list4)):
    emp4.update({keys[l]:list4[l]})
with open("kirteepatil.json","w")as k:
    json.dump(dict,k,indent=4)














