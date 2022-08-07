operand_1 = int(input('Enter your first name: '))
operand_2 = float(input('Enter your second name: '))
operation = input(''''
Please type in the match operation you would like to complete: 
+
-
*
**
/
''''')
if operation == '+':
    print('{} + {} = '.format(operand_1, operand_2))
    print(operand_1 + operand_2)

elif operation == '-':
    print('{} - {} = '.format(operand_1, operand_2))
    print(operand_1 - operand_2)

elif operation == '*':
    print('{} * {} = '.format(operand_1, operand_2))
    print(operand_1 * operand_2)

elif operation == '**':
    print('{} ** {} = '.format(operand_1, operand_2))
    print(operand_1 ** operand_2)

elif operation == '/':
    print('{} / {} = '.format(operand_1, operand_2))
    print(operand_1 / operand_2)



if operation == "(":
    print("wrong symbol")

if operation == "$":
    print("wrong symbol")

if operation == "@":
    print("wrong symbol")














