#Braden Leach
#Nov 26 2024
#While Loop Practice


#managing a list with a WHILE loop
number = 0
tempatures = []

while number != -9999:
 
 number = int(input(f'Enter a temerature in Fahrenheit (-9999 to quit): '))
 tempatures.append(number)


tempatures.pop()

list_length = len(tempatures)
if list_length > 0:
   print(f'Temeratures entered: {tempatures}')
   average = sum(tempatures) / len(tempatures)
   print(f'average temperature:{average:.2f}°F')   
else:
    print('No temeratures were entered')