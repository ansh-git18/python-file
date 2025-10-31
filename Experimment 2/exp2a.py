#programme to calculate simple interest and compund interest
#taking input from the user
principal=float(input("enter the princiapl amounnt(in rs.)"))
rate=float(input("enter the rate of interest(in %)"))
time=float(input("enter the time (in years)"))

#calculating simple interest
simple_interest=(principal*rate*time)/100

#calculating compound interest
compound_amount=principal*(1+rate/100)**time
compound_interest=compound_amount-principal

#displayinng the results
print(f"the simple interest is:{simple_interest:.2f}")
print(f"the compound interest is:{compound_interest:.2f}")


