# Code to prompt the user to enter 5 numbers then output the largest number
num_list = []

num = 5

for n in range(num):
    numbers = int(input('Enter number: '))
    num_list.append(numbers)

print("The largest number is: ",max(num_list))