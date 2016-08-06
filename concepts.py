#variables
x = 12
y = "string variable"
z = 12.03


#lists
my_list = [1, 2, 3, 4, 5]
my_list.extend([6, 7])
my_list.append(8)


# string interpolation
print("contents of my_list variable: {}".format(my_list))


# more string methods
available = "banana split;hot fudge;cherry;malted;black;white"
sundaes = available.split(";")
print(sundaes) #will print a list

mondaes = ", ".join(sundaes)
print(mondaes) #will print a string


# function declaration
def my_useless_function():
    value = "this is a string"
    print(value)

my_useless_function()
