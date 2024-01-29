s = "i dont't like"
print(s)

# Given string
x = 'Welcome to Python foundation course'

# 1. find()
find_result = x.find('Python')
print("find result:- ", find_result)

# 2. count()
count_result = x.count('')
print("count result:- ",count_result)

# 3. len()
length_result = len(x)
print("length result:- ",length_result)

# 4. Concatenation
concatenation_result = x + ' - Advanced Topics'
print("concatination result:- ", concatenation_result)


x = "PanaJi@12256"
lowercase_count = x.islower()
print(lowercase_count)

uppercase_count = x.isupper()
print(uppercase_count)

numerical_count = x.isalnum()
print(numerical_count)

#store anumerical value in a variable
numerical_value = 123

#convert the numerical value to a string
string_value = str(numerical_value)
print("original numerical value: ", numerical_value)
print("Converted String Value: ", string_value)

print(type(string_value))
print(type(numerical_value))