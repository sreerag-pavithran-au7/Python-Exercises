#Dictionary Making
dicts = {"Brand" : "Maruti", "Model" : "Baleno", "Year" : "2019"}
print(dicts)

#Getting Value from Dict using Key
x = dicts.get("Brand")
print(x)

#Adding Values 
dicts["Year"] = 2020
print(dicts)

#Updating dict
d2 = {"Colour" : "Blue", "Drive" : "Manual", "Option" : "Full"}
print(d2)
dicts.update(d2)
print(dicts)

#Deleting
del dicts["Drive"]
print(dicts)

#Finding length
print(len(dicts))

#Print all keys
print(list(dicts.keys()))

#Print all values
print(list(dicts.values()))

#Clear Dictionary
dicts.clear()
print(dicts)
