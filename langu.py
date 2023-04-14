choice=input("Enter your Name :")
output=""
for letter in choice:
 if letter in ["a","e","i","o","u"]:
    letter="t"
 elif letter in ["A","E","I","O","U"]:
     letter="T"
 output=output+letter
print(output)