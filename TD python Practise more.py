#Exercice 1
Name = "google.com"
Frequence = {}
for char in Name:
    if char in Frequence:
        Frequence[char]  += 1
    else: 
        Frequence[char] = 1
print(str(Frequence))

#exercice 2
Chain = input("Donnez- moi un mot, s'il vous plait: ")
if len(Chain) < 3:
    print(Chain)
else:
        if  Chain[-1] == "g" and Chain[-2] == "n" and Chain[-3] == "i":
            Chain += "ly"
            print(Chain)
        else:
            Chain += "ing"
            print(Chain)

#Exercice 3
list = []
for x in range(1500, 2071):
    if x % 7 == 0 and x % 5 == 0: 
        list.append(x)
print(list)

#Exercice 4
for x in range(0,51):
    if x % 3 == 0 and x % 5 == 0:
        print ("BuzzFizze")
    elif x % 5 == 0:
        print ("buzz")
    else:
        print(x)

#Exercice 5
Reverse = ""
string = input("Donnez - moi un mot, s'il vous plait: ") 
print(string [::-1]) 

#Exercice 6
List = [1, 6, 9, 0, 9, 0, 9, 6]
List2 = []
for x in List:
    if x not in List2:
        List2.append(x)
print (List2)  

#Exercice 7
palin = input("Donnez - moi un mot, s'il vous plait ")
if palin == palin[::-1]: 
    print (palin + " is a palindrome")
else:  
    print (palin + " isn't a palindrome")

#Exercice 9
a = int(input("Donnez - moi un nombre entre 1 et 9, s'il vous plait ! "))
x = a
for i in range (1, 10):
    a *= i
    print ( x , " x ", i , " = " , a )
    a = a // i

#Exercice 10
alphabet = input ("Input a letter of the alphabet: ")
if alphabet == "a" or alphabet == "u" or alphabet == "e" or alphabet == "i" or alphabet == "o":
    print (alphabet + " is a vowel")
else:
    print (alphabet + " is a consonant")



