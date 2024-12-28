str1 = "Hello developers"
print(str1[0])
print(str1[1])
for character in str1:
  print(character)

print(len(str1))
print(str1[0:5])
print(str1[:5])
print(str1[0:-11]) #same as print(str1[0:len(str1)-11])
print(str1[:])
print(str1[5:])
print(str1.upper())
print(str1.lower())
print(str1.capitalize())

str2 = "!!!!!Jay Shree Ram!!!!!"
print(str2.rstrip("!"))
print(str2.lstrip("!"))
print(str2.strip("!"))
print(str2.replace("Ram", "Krishna"))
print(str2.split(" "))
print(str2.center(50))
print(str2.center(50, "."))
print(str2.count("!"))
print(str2.endswith("!"))
print(str2[0:18])
print(str2.endswith("Ram",0,18))
print(str2.find("a")) #returns -1 if not found
print(str2.index("a")) #returns error if not found
print(str1.isalpha())
print(str1.isnumeric())
print(str2.isalnum())
str3="HelloEveryone\n"
print(str3.isprintable())
str3="HelloEveryone"
print(str3.isprintable())
str4="  "
print(str4.isspace())
print(str2.istitle())
print(str1.istitle())
print(str1.title())
print(str1.startswith("Hello"))