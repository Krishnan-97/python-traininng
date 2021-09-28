n1 = int(input('Enter num1:'))
n2 = int(input('Enter num2:'))
n3 = int(input('Enter num3:'))

if(n1 >= n2):
    gr = n1
else:
    gr = n2

if(n3 > gr):
    print('Biggest num is',n3)
else:
    print('Biggest num is',gr)