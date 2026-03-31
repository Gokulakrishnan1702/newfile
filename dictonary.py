my_dict = {
    "name": "Akash",
    "age": 25,
    "city": "Chennai"
}

print(my_dict["name"])  

my_dict["country"] = "India"  
my_dict["age"] = 26          
del my_dict["city"]      
for key, value in my_dict.items():
    print(key, ":", value)