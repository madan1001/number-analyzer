#User is asked to input the numbers they want
print ("Enter your numbers")
numbersinput = input()

#The program converts number input of user into list data type. The list is consist of numbers.
listnumbers = []
    
for i in range (0, len(numbersinput)):
    if numbersinput.find(" ") != -1:
        x = numbersinput.find(" ")
        listnumbers.append(int(numbersinput[:x]))
        numbersinput = numbersinput [x+1:]
    else :
        listnumbers.append(int(numbersinput))
        break
    
#Function for summing all numbers
def sum (a):
    y = 0
    for i in range (0, len(a)):
        y += a[i]
    return y

#Function for calculating average
def average (a):
    avg = sum(a)/len(a)
    return avg

#Function for calculating how many even numbers in the list
def even (a):
    evennumbers = 0
    for i in range (0, len(a)):
        if a[i] % 2 == 0 :
            evennumbers += 1
    return evennumbers
        
#Function for calculating how many odd numbers in the list
def odd (a):
    oddnumbers = 0
    for i in range (0, len(a)):
        if a[i] % 2 == 1:
            oddnumbers += 1
    return oddnumbers

#Discard all duplicate numbers
unique = list (set (listnumbers))

#Show all result of the analysis of user input numbers
print("\n=== NUMBER ANALYZER ===\n")
print (f"Number of elements : {len(listnumbers)}")
print (f"Sum of numbers : {sum(listnumbers)}")
print (f"Average of the numbers is {average(listnumbers)}")
print (f"Largest numbers : {max(listnumbers)}")
print (f"Smallest numbers : {min(listnumbers)}")
print (f"Number of even integers : {even(listnumbers)}")
print (f"Number of odd integers : {odd(listnumbers)}")
print (f"Unique numbers : {unique}")


