cart = {}  

def add_item():
    item = input("Enter the item name: ")
    price = float(input("Enter the item price: ₹"))
    cart[item] = price
    print(f"{item} added to cart!")

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        for item, price in cart.items():
            print(f"- {item}: ₹{price:.2f}")

def calculate_total():
    total = sum(cart.values())
    print(f"\nTotal amount: ₹{total:.2f}")

    
    if total > 1000:
        discount = total * 0.10  # 10% discount
        total -= discount
        print(f"Discount applied: ₹{discount:.2f}")
    else:
        print("No discount applied (Spend more than ₹1000 for 10% off).")

    print(f"Final amount to pay: ₹{total:.2f}")

def main():
    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_cart()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            print("Thank you for shopping! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")
main()


