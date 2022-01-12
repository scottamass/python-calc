

def calc(operation,number_1,number_2):
    


    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        total=number_1 + number_2
        return total

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        total=number_1 + number_2
        return total
    elif operation == 'x':
        print('{} * {} = '.format(number_1, number_2))
        total=number_1 + number_2
        return total
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        total=number_1 + number_2
        return total
    else:
        print('You have not typed a valid operator, please run the program again.')


with open('test.txt','r') as file:
    

    filelines= file.read().splitlines()
    for line in filelines:
        comp=line.split()

        operator=comp[1]
        number_1=int(comp[2])
        number_2=int(comp[3])
        
        awn=calc(operator,number_1,number_2)
        
        
    
        awn+=awn

    print(awn)    



    # calc 2%5
        

        

    
     
