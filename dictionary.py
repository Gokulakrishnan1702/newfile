user = {"name":"santhosh","age":18,"gender":"male"}
print(user)
print(type(user))
print("location : ", id(user))
print(user.keys())
print(user.values())
print(user.items())

#Access dictionary, and their keys and values
print("-------------------------")
for x in user:
    print(x, ":", user[x])
print("-------------------------")
for x in user.keys():
    print(x) 
print("-------------------------")
for x in user.values():
    print(x)

#Checking the dictionary
print("-------------------------")
if "name" in user:
    print("found")
else:
    print("not found")


#update
user.update({"Place":"coimbatore"})
print(user)
#insert
user["age"]=25
print(user)
#delete
user.pop("age")
print(user)
print("-----------------------------")

#nested dictionary
user={
    'user1':{
        "name": "gokulakrishnan",
        "age": 19,
        "gender": "male"
    },
    'user2':{
        "name": "abiesh",
        "age": 18,
        "gender": "male"

    }
}  

print(user)
print(user["user1"])
print(user["user2"])
print("---------------------------")
print(user["user1"].keys())
print(user["user2"].values())