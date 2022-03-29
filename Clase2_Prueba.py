n = 100
a = "Fizz"
b = "Buzz"
c = "FizzBuzz"

for i in range(1 , n+1):
    if (i%5 == 0 and i%3 == 0):
        print(str(i)+ " " + c)
    elif i % 3 == 0:
        print(str(i)+ " " + a)
    elif i % 5 == 0:
        print(str(i)+ " " + b)

    
