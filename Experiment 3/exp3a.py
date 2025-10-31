def modify_number(num):
    print(f"[Inside] Before modification: num = {num}")
    num += 10
    print(f"[Inside] After modification: num = {num}")
    
# Main program
original_number = 5
print(f"Before function call: original_number = {original_number}")

modify_number(original_number)
print(f"After function call: original_number = {original_number}")