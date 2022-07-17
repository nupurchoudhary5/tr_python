fname = 'Nupur'
lname = 'Choudhary'

# if fname == 'Nupur':
#     print("true")
# else:
#     print("false")


# if fname == 'Nupur' and lname == 'Choudhary':  #both condition shld be true in and
#     print("true")
# else:
#     print("false")


# if fname == 'Nupur' or lname == 'Sharma':  #only 1 condition true shows true output in or
#     print("true")
# else:
#     print("false")


# if fname == 'Nupur' and not lname == 'Sharma':  #not operator
#     print("true")
# else:
#     print("false")



# if fname == 'Nupur' and not lname == 'Sharma' and company == 'regex':  #multiple operators can be used  but undefined name like company gives error
#     print("true")
# else:
#     print("false")



# if 'Nupur' in ['a', 'b', 'c']: #elif statements
#     print('Nupur is in list')
# elif 'p' in 'Nupur':
#     print('it is true')
# elif 'k' in 'aakash':
#     print('true')
# else:
#     print('false')





# #take input from user and print the value whose ascii value is even

# string = input("enter the string:")
# for i in string:
#     if(ord(i)%2 == 0):
#         print("ASCII value is even:"+i)

#input of integer type and input from user and append them in list

# value = int(input("enter the value:"))
# lst_ = [ ]
# for i in range(0,value):
#     elements = input("enter the lists:")
#     lst_.append(elements)
# print(lst_)

#take n inp from user(int) and give data type and data and create a dictionary as output

element = int(input("enter the value:"))
map_ = {
    'str' : [],
    'int' : [],
    'float' : []
 }
for i in range(element):
    dt = input('enter datatype:')
    value = input('enter value:')
    if dt == 'str':
        map_['str'].append(value)
    elif dt == 'int':
        map_['int'].append(int(value))
    elif dt == 'float':
        map_['float'].append(float(value))
    else:
        print('please initialize empty list for {dt}',format(dt))
    print(map_)














        



