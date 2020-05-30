employee=['mark','julia','philix','lambert']
print('enter your name here to insert your name to the employee list: ')
here=input()
x=here
employee.insert(0,x)
print(employee)
print('type your name to know your rank: ')
rank=input()
y=rank
print(employee.index(y))
print('whos the last in rank:',employee.pop())

