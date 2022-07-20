# #given a string in i/p and create dictionary with information of frequency of characters in a given string
# dictionary = {}
# string = input('give a string:')
# for i in string:
#     if(dictionary.get(i)):
#         dictionary[i] = dictionary.get(i) + 1
#     else:
#         dictionary[i] = 1
# print(dictionary)



#method 2 for above prblm
# dictionary = {}
# string = input('give a string:')
# for i in string:
#     if i in dictionary:
#         dictionary[i] += 1
#     else:
#         dictionary[i] = 1
# print(dictionary)



#upper case and lower case shld be considered as same in dictionary to count
# dictionary = {}
# string = input('give a string:')
# st = string.casefold()       #can use st = string.lower()
# for i in st:
#     if i in dictionary:
#         dictionary[i] += 1
#     else:
#         dictionary[i] = 1
# print(dictionary)


# #break loop
# for i in range(5):
#     if (i == 3):
#         break
#     else:
#         print(i)


# #loop of push and pop in list until user enter stop
# lst_ = []
# inp = int(input('enter input:'))
# for i in range(inp):
#     op = input().split()
#     if op[0] =='push':
#         lst_.append(op[1])
#         print(lst_)
#     elif op[0] == 'pop':
#         lst_.remove(op[1])
#         print(lst_)
#     elif op[0] == 'stop':
#         break
# print(lst_)


# set in dictionary
n = input('string:')
dict_ = {}



