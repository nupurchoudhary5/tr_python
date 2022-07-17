first_name = 'Nupur'
last_name = 'Choudhary'
print(first_name.upper())
print(first_name.isdigit())
print(first_name.isdecimal())
print(first_name.capitalize())
print(first_name.casefold())
print(first_name.endswith('p'))
print(first_name.find('u'))
print(first_name.count('u'))

#15july
sentence = f'{first_name} {last_name} is a coder'
print(sentence)

#length_function
s = 'nupur'
len(s)

#lists
lst = [1, 2, 3, 4, 5, 'hello', ['a', 'b', 'c']]
print(lst[0])
print(lst[-1])
print(lst[-2][0])
print(lst[6][1])

#it will run after commenting the code from 22 to 25
lst[0] = 7
print(lst)

random_number_list = [10,32,12,45,67,89,12,34,56,78,90]
random_number_list.sort()
print(random_number_list)

#comment the code from 31 to 33 
print(random_number_list, 'before appending:')
random_number_list.append('hello world')
print(random_number_list, 'after appending:')

#print according to ascii value
name = 'nupur'
ls = list(name)
print(ls)
ls.sort()
print(ls)


a =[1, 2, 4]
b = [3, 5, 6]
a + b
print(a+b)
a.extend(b)
print(a)
b.extend(a)
print(b)
a.append(b)
print(a)
a.reverse()
print(a)


#list slicing
a = [1, 2, 3, 4, 'hello world', 5, 6, 7]
a[0:len(a):1]
print(a)
a[-1:4:-1]
print(a)

