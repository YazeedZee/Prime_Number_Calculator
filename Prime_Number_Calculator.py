import math
import time
'''
Names: 
1- Yazeed Mohammed Alzughaibi
2- Abdulrahman Sameer Aljuhani
This is EE305 project
this python written program has two differant algorithms 
that will recive a range of numbers from the lowend to 
the highend and outputs all the prime 
numbers in between them
'''

choice = 88
while (choice != 0):
    choice = int(input('Enter choice of algorithms to calculate prime numbers 1 or 2 & 0 for exiting:'))
    if choice == 1:
        print('Algorithm 1: ')
        lowend = int(input('Enter the lower end of the range: '))
        highend = int(input('Enter the higher end of the range: '))
        time1 = time.time() #save time stamp after input is done
        listofprime = [] #list to hold the prime numbers later on
        for x in range(lowend, highend + 1): #loop to go through the range of numbers
            if x > 1: #check if its greater than one
                for y in range(2, x): 
                    if x % y == 0: #if that specific number in the range can be divided by any number then it's not a prime number
                        break
                else: 
                    listofprime.append(x) #add that number to the list to display later
        calctime1 = time.time() - time1 #calculate the CPU time for the algorithm
        #final print
        print('the prime numbers between ' + str(lowend) + ' and ' + str(highend) + ' are:')
        print(listofprime)
        print(calctime1)
    elif choice == 2:
        print('Algorithm 2: ')
        lowend = int(input('Enter the lower end of the range: '))
        highend = int(input('Enter the higher end of the range: '))
        time2 = time.time() #save time stamp after input is done
        listofprime = [] #list to hold the prime numbers later on
        for x in range(lowend , highend + 1):  #loop to go through the range of numbers
            if x > 1: #check if its greater than one
                for y in range (2, int(math.sqrt(x)) + 1):
                    if x % y == 0: #if that specific number in the range can be divided by any number then it's not a prime number
                        break
                else:
                    listofprime.append(x) #add that number to the list to display later
        calctime2 = time.time() - time2 #calculate the CPU time for the algorithm
        #final print
        print('the prime numbers between ' + str(lowend) + ' and ' + str(highend) + ' are:') 
        print(listofprime)
        print(calctime2)
print('Program exiting...')
