Character_name = "SpyingSpy" # A String is made
print(Character_name)
is_island = False #boolean value
print("2. Hi," + Character_name) # can aslo use , works same.. also , works even with int and string while + doesn't 
Character_name = "SpySpying"
print("3. Hi,\n" + Character_name) #using next line command
print("4." + Character_name.upper())
print("5." + Character_name.lower())
print(6,Character_name.isupper())
print(7,Character_name.islower())
print(8,Character_name.upper().islower())
print(9,Character_name.upper().isupper())
print(len(Character_name))
print("10." + Character_name[0])  # string me 1st letter is 0
print(11,Character_name[8])
print(12,Character_name[3])
print(13,Character_name.index("y"))
print(14,Character_name.index("S"))
print("15." + Character_name.replace("Spy", "Agent"))
print(10/3, 10 % 3)    # % For Remainder
yo_num = 7
yoo_num = -7
print(yo_num)
print(yoo_num)
print("8." + str(yoo_num))
print(abs(yoo_num))  # absolute value ke liye -5=5
print(pow(2, 4))  # 2^4 i.e. power
print(max(2, 3))
print(min(2, 3))
print(round(3.7))  # rounding off
print(round(3.4))
from math import *  # extra maths function (module)
# print(floor(4.7))
print(ceil(4.7))
print(sqrt(36))  # Square root
entry = input("Entre Something!:-")
print("Aree bhai kehna kya chahte ho? \n'" + entry + "' , kya mtlb hai iska?")
n1 = input("Ab Number likho...aur hn whole no. hi likhna")
n2 = input("one more time please...decimal bhi likh skte ho ab whole jruri nhi...")
result = int(n1) + float(n2)
print("ye lijiye result --> " + str(result))
print("Vaise jruri nhi tha decimal likhna")
cmt = input("ab kuch comment bhi krdo kaisa lga: ")
print("Maaannnn.... nhi chahiye koi comment agr bs itna hi dena h to..." + cmt)
Users = ["X", "A", "Y", "B", 2, False, "LOL"]  # known as list can store Strings, number, boolean in one array.. you can store bunch of values in [] and can modify them later
print("So, Next")
print(Users)
print("So, Actual Users:")
print(Users[0]) #only 0 index value
print(Users[-6]) 
print(Users[-2:]) #from -2 index to end
print(Users[-3:-2]) #from -3 index to -2
Users[0] = "X Y"
Users[1] = "A B"
print("So, Actual User's Full name:")
print(Users[0],",")
print(Users[-6],".")
no = [1, 2, 3, 4, 5, 6]
Users.extend(no)
print(Users)
Users.remove("LOL")
print(Users)
print(Users.index("Y"))
print(Users.count(2))  # counting no. of times the string/no./boolean(i.e. inside paranthesis) appears in the array
#Users.sort() #sorts the list but for now list contains strings so it's commented out
#print(Users)
Users.clear()
print(Users)
Users.append("You")
print(Users)
Users.insert(1, "Yes, You") #in insert you can define location but not in append
print(Users)
Users.pop() #removes one element
print(Users)
no.reverse()
print(no)
no2 = no.copy()
print(no2)
coordinates = (1, 11)  # known as tuple and cannot be modified
print(coordinates[0])
print(coordinates[1])
combo = [(1, 12), (2, 4), (6, 1)]  # tuples inside list
