def print_table(n):
    i=1
    while(i<=10):
        print(f"{n}*{i}={n*i}")
        i+=1
for _ in range(10):
#taking input from the user
   n=int(input("enter a number:"))
   print_table(n)
print()

