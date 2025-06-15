####################################################################################################################
#Variables/DataType
from operator import truediv

age = 25 #integer
height = 1.75 #float
name =  "Slavi" #String
is_student = True #boolean
fruits = ["apple", "banana","orange"] #List
coordinates = {10,20} #Tuple
person = {"name":"Slavi", "age":25, "is_student":True}#Dictionary {dict}
unique_number = {1,2,3,4,5,6}#Set (set)
#NonType {None} #absence of value


####################################################################################################################
#Math operators

a=10
b=8
add=a+b
sub=a-b
multiply=a*b
division = a/b
floor_division=a//b
mod= a%b
exponentiation = a**b
print("Addition: ",add)
print("Subtraction: ",sub)
print("Multiplication: ",multiply)
print("Division: ",division)
print("Floor division: ",floor_division)
print("Modulus: ",mod)
print("Exponentiation: ",exponentiation)


####################################################################################################################
#Comparison operators
x = 10
y = 5

equal_to = x==y
not_equal_to = x != y
greater_than = x > y
less_than = x < y
greater_than_or_equal_to = x >= y
less_than_or_equal_to = x <= y

print("Equal to: ",equal_to)
print("Not equal to: ",not_equal_to)
print("Greater than: ",greater_than)
print("Less than: ",less_than)
print("Greater than or equal to: ",greater_than_or_equal_to)
print("Less than or equal to: ",less_than_or_equal_to)


####################################################################################################################
#Logical operators

p = True
q = False
logical_AND = p and q
logical_OR = p or q
logical_NOT = not p

print("Logical AND: ",logical_AND)
print("Logical OR: ",logical_OR)
print("Logical NOT: ",logical_NOT)

#Control Structures (if statements,loops)
####################################################################################################################

z = int(input())
if z > 10:
    print("Hello, Chichaci")
elif x==0:
    print("Nula e")
else:
    print("Less than 52")


####################################################################################################################
#Loops
    #a.For loops
    fruits = ["apple","banana","lemon"]
    for i in fruits:
        print (i)

    #b.While loops
    count =0
    while count < 8:
        print("Count : ", count)
        count +=1

    ####################################################################################################################
    #3. Control Statements
    for i in range(8):
        if i==3:
            break
        elif i==1:
            continue   #пропуска останалия код вповтарянето
        else:
            pass
        print (i)


####################################################################################################################

    #4. Nested Control Structures
    for aa in range(5):
        print("Outer loop:", aa)
        for bb in range(4):
            print("Inner loop:", bb)
            if bb==1:
                break



####################################################################################################################

    #4. Data structures
    #List
    #Creating List
    numbers = [1,2,3,4,5,6,7]
    fruits = ["apple","banana","lemon", "mango","melon"]
    mixed = [1,"banana",2, True, 3.14, "петка",False, 234]

    #Accessing elements
    print(numbers[0])
    print(fruits[1])
    print(mixed[-1])

    #Slicing a list
    print(numbers[2:6]) #показва елементите между индексите 2 и 6
    print (fruits[:3])
    print((mixed[2:0:-1])) #reversed



    #Modifying
    fruits[1]="avocado"
    print(fruits)
    fruits.append("banana")
    print(fruits)
    fruits.insert(2,"bambuk")
    print(fruits)
    fruits.remove("lemon")
    print(fruits)
    del fruits[3]
    print (fruits)

    #List operations
    combined = numbers+fruits #combination
    repeat = fruits*2
    print("apple" in fruits)#membership output:boolean
    print(combined)
    print(repeat)

    #Common list methods append(), pop(), extend(),sort(),reverse()
    print(numbers)
    numbers.append(9)#add element to the end
    print(numbers)
    numbers.pop()#remove the last element #number.pop(3) -  remove element by index
    print(numbers)
    fruits.extend(["kiwi","cactus"])
    print(fruits)
    fruits.sort()
    print(fruits)
    fruits.reverse()
    print(fruits)


#TUPLES
#Creating tuples
number_tuple = (1,2,3,4,5)
fruit_tuple =("apple","lemon","banana")
mixed_tuple = ("apple",27,True,1.34)

#Accessing tuples
print(number_tuple[0])
print (fruit_tuple[2])
print(mixed_tuple[-1])

#Tuple packing and unpacking
#Tuple packing
person=("Slavi",17,"Sofiq")
#Tuple unpacking
name,age,city=person
print("Name: ",name)
print("Age: ",age)
print("City: ",city)

