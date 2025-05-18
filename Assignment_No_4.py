"""# Q1
name = input("What is your name?")
movie = input("What is your favorite movie?")

print(name+' \'s favorite movie is '+ movie+'.')

#Q2 
string = input("Enter a string:")
print("The string you entered is: "+string)
print("The upper of the string is: "+string.upper())
print("The lower of the string is: "+string.lower())
print("The title case of the string is: "+string.title())
print("The length of the string is: "+str(len(string)))

#Q3
list = []
for i in range(2):
    list.append(int(input("Enter a number:")))

sum = int(0)
diff = int(0) 
multiply = int(1)  
quotient = int(0)
for j in range(len(list)):
    sum=sum+list[j]
    multiply=multiply*list[j]
    if j==0:
        diff=list[j]
        quotient=list[j]
    else:
        diff=diff-list[j]
        quotient=quotient/list[j]

print("The sum of the numbers is: "+str(sum))
print("The difference of the numbers is: "+str(diff))
print("The product of the numbers is: "+str(multiply))
print("The quotient of the numbers is: "+str(quotient))

#Q4

list = ['Haris', 'Nadeem', 'Ali', 'Butt']
for x in list:
    print(x,end=' ')

#Q5

list = ['Apple','Orange','Mango']
print(str(list))
list[1]='Banana'
print(str(list))
list.append('Grapes')
print(str(list))
list.insert(0,'Pineapple')
print(str(list))

#Q6

list = ['','','','','']   

for i in range(5):
    print(i)
    list[i] = input("Enter animal name: ")

print("The list of animals has : "+str(len(list))+ " animals in it")
print("The first animal is " + list[0] + " and the last animal is " + list[len(list)-1])

#Q7

for i in range(11):
    print(str(i),end =',')
print("")
for i in range(2,21,2):
    print(str(i),end=',')
print("")
for i in range(5,51,5):
    print(str(i),end=',')
print("")


#Q8

for i in range(1,11):
    print(str(i) + " squared is "+ str(i*i))

#Q9

list = [x*x*x for x in range(1,6) ]
print(list)

# Q10

print("Enter 5 movies name")
list = ['A','B','C','D','E']
for i in range(5):
    list.append(input())
print(list[0:3])
print(list[:-3:-1])

# Q11
list =[]
for i in range(5):
    list.append(input("Enter "+str(i)+ " Student Name: "))
print("Top three students are:"+str(list[0:3]))
newList=list[:]
newList.append("Jahanzaib")
newList.append("tayyab")

print("Original List: "+str(list))
print("New List: "+str(newList))

# Q12
list = ["Saudia", "Turkey", "Swizerland", "germany", "France"]
print("The list of countries is: "+str(list))
list.sort()
print("The temporary sorted list of countries is: "+str(list))
list.sort(reverse=True)
print("The Reversed sorted list of countries is: "+str(list))
list.reverse()
print("The reversed version of the list is: "+str(list))
list.reverse()
print("The origdouble reversed version of list of countries is: "+str(list))


# Q13
input_string = input("Enter your name: ")
list = input_string[0:]
for i in list:
    print(str(i))

firstList = []
for i in range(3):
    firstList.append(list[i])

print("The first three letters are:"+ str(firstList))

lastList = []
for i in range(len(list)-2,len(list)):
    lastList.append(list[i])

print("The last three letters are:"+ str(lastList))
print("The length of my name is: "+ str(len(list)))
"""