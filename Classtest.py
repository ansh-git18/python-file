def shopping_cart():
    prices = []

    print("Enter item prices (type 'done' to finish):")
    while True:
        user_input = input("Price: ")
        if user_input.lower() == "done":
            break

        # Validate numeric input
        try:
            price = float(user_input)
            if price < 0:
                print("❌ Price cannot be negative. Try again.")
                continue
            prices.append(price)
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")
            continue

    if not prices:
        print("No items added to cart.")
        return

    total = sum(prices)

    # Apply discount condition
    if total > 2000:
        discount = 0.10 * total
    else:
        discount = 0.0

    payable = total - discount

    print("\n🛒 Shopping Cart Summary")
    print("-------------------------")
    print(f"Items: {prices}")
    print(f"Total: ₹{total:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Final Payable: ₹{payable:.2f}")


# Run the program
shopping_cart()