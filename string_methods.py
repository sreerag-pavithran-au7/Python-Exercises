# SLICING
a = "RSEERAG"
print(a[0:4:1])

# REVERSE STRING
print(a[::-1])

# STRING CONCATENATE
strAdd = "Sreerag" + " Pavithran"
print(strAdd)

#STRING LENGTH
strlen = "Sandra"
print(len(strlen))

# UPPER AND LOWER CASE
loves = "Sreerag Sandra"
print(loves.upper())
print(loves.lower())

# BOOLEAN METHOD
number = "30"
bee = "Sandra"

print(number.isnumeric()) # String consists of only numeric characters
print(bee.isalpha()) # String consists of only alphabetic characters (no symbols)
print(number.isalnum()) # String consists of only alphanumeric characters (no symbols)

# str.islower()	--- String’s alphabetic characters are all lower case
# str.isspace() ---	String consists of only whitespace characters
# str.istitle() ---	String is in title case
# str.isupper()	--- String’s alphabetic characters are all upper case

print(loves.find("Sandra")) # find() returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.


# Python String | strip()
lett = "@@@iamsreerag@@@"
print(lett.strip("@"))

# Type() Function
leta = "Saa"
letb = 30
print(type(leta))
print(type(letb))




