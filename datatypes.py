#Data types
#STRINGS
print("Hello"[4])
#INTEGER
a= 123 + 345
print(a)
#Float
b= 431.21
c= 21_31.31
#Boolean
True
False
#Type casting/conversion
num_char= len(input("What is your name? "))
# print("The length is" + num_char+ "characters") ERROR: TypeError: can only concatenate str (not "int") to str
new_num_char= str(num_char)
print("The length is " + new_num_char+ " characters") #Yay no error!
print(type(b)) #type() is used to get the datatype of a variable
print(123+ float("100.2"))
print(str(70)+ str(100))