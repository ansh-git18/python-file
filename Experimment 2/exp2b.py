def separate_rupees_paise(price):
#extract rupees as the integer part
 rupees=int(price)
#extract paise by substracting rupees and multiplying by 100 , then rounding to handle floating point inprecision
 paise=round((price-rupees)*100)
 return rupees,paise

#input from the user 
price=float(input("enter the price(e.g.,12.50):"))
#call the function
rupees,paise=separate_rupees_paise(price)

print(f"rupees:{rupees}")
print(f"paise:{paise}")