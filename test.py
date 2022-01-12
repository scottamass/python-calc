

#file = open('/anotherfile.txt','w')
#i=0
#temp=1
#with open('/filename.txt') as file_:
#    for line in file_:
#        temp = temp*int(line)
#        if(i>1 && i%3==0):
#           file.write(str(temp)+'\n')
#           temp=1
#        i += 1
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')


number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))



if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')