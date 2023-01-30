import json

with open("data.json","r") as j_f :
  a=json.load(j_f)
  
# print(a[0].faculty)
# print(a)
# print(a[["students"]["name"]])
print(a['students'][0]['faculty'])
