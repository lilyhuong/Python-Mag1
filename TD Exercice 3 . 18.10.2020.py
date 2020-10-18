#Exercise 1
animal = ["cow" , "mouse" , "cat" , "pig" ]
for x in animal: 
    print (x)
i = 0
while i < len(animal):
    print(animal[i])
    i += 1
#Exerise  2
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
i = 0
for i in range(5):
    print(week[i])
i = 5
while i < len(week):
    print(week[i]) 
    i += 1
#Exercise 3
for x in range(1 , 21):
    if x % 5 == 0:
        print(x)
#Exercise 4
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
even = []
for x in odd:
    x += 1
    even.append(x)
print(even)
#Exercise 5
note = [14, 9, 6, 8, 12]
sum = 0
for x in note:
    sum = sum + x
print ("The average of these notes  is {:.2f} ". format(sum/5))
#Exercise 6
for x in range(11):
    x = x * 2
    print (x)
#Exercise 7
for i in range (1 , 11):
    print( i * "*" + (11 - i) * " ")
#Exercise 8
for i in range (10 , 0 , -1):
    print( i * "*" + (10 - i) * " ")
#Exercise 9
for i in range (10 , 0 , -1):
    print( i * " " + (10 - i) * "*")
#Exercise 10
for i in range (10 , 0 , -1):
  print (i * " " + (21 - 2 * i) * "*" + i * " " )
#Exercise 12
Fibonacci = [0, 1]
for i in range (2,20):
  x = Fibonacci[i - 2] + Fibonacci[i - 1]
  Fibonacci.append(x)
print(Fibonacci)


