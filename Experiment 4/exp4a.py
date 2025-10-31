def factorial(n):
    fact=1
    i=2
    while(i<=n):
          fact=fact*i
          i+=1
#taking input from the user
while True:
    n=int(input("enter a number:"))
    print(f"the factorail of the number is:{fact}")
factorial(n)