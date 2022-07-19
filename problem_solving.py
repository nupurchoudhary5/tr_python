# #july-18

# s = 'He is backend developer'
# print(s.split())

# s_ = 'He-is-web-developer'
# print(s_.split('-'))

# #take an int from user and perform add,mul,sub,div by taking int from user

# value = int(input('enter the number:'))
# for i in range(value):
#     operation, n1, n2 = input().split()
#     n1 = int(n1)
#     n2 = int(n2)
    
#     if operation == 'add':
#         print(n1 + n2)
#     elif operation == 'mul':
#         print(n1 * n2)
#     elif operation == 'sub':
#         print(n1 - n2)
#     elif operation == 'div':
#         print(n1 / n2)
#     else:
#         print('not found')

    #code 2 for above ques
# n = input('how many test cases:') 
# n = int(n)
# for i in range(n):
#     op = input('please enter the operation string:')
#     op_list = op.split()
#     print(op_list)
#     if op_list[0] == 'add':
#         num1 = int(op_list[1])
#         num2 = int(op_list[2])
#         print(num1 + num2)
#     elif op_list[0] == 'sub':
#         num1 = int(op_list[1])
#         num2 = int(op_list[2])
#         print(num1 - num2)
#     elif op_list[0] == 'mul':
#         num1 = int(op_list[1])
#         num2 = int(op_list[2])
#         print(num1 * num2)
#     elif op_list[0] == 'div':
#         num1 = int(op_list[1])
#         num2 = int(op_list[2])
#         print(num1 / num2)
#     else:
#         print('no found')


#         #perform add and mul for n no. of integer

# n = input('how many test cases:') 
# n = int(n)
# for i in range(n):
#     op = input('please enter the operation string:')
#     op_lst = op.split()
#     print(op_lst)

#     if op_lst[0] == 'add':
#         total = 0
#         for n in op_lst[1:]:
#             total = total + int(n)
#         print(total)

#     elif op_lst[0] == 'mul':
#         mult = 1
#         for m in op_lst[1:]:
#             mult = mult + int(m)
#         print(mult)


# #factorial
# num = int(input('enter the number:'))

# factorial = 1
# if int(num) >= 0:
#     for i in range(1, int(num)+1):
#         factorial = factorial*i
#     print("the factorial of",num,"is",factorial)

#     #palindrome
#     string = input('enter a string:')
# reverse_string = string[4::-1]
# if reverse_string == string:
#     print('yes')
# else:
#     print('no')


#problem 5  print the character with its ascii value
lst = input().split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
    print(chr(lst[i]))  
   


