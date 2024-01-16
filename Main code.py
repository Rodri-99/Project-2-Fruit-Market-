# Dictionary containing fruits and their prices
fruits_prices = {
    "Apple": 2,
    "Grape": 1,
    "Orange": 3
}

# Welcome message
print("Welcome to the GC Fruit Market!")
user_name = input("What is your name?\n> ")

# Initialize total cost and fruit quantities
total_cost = 0
fruit_quantities = {fruit: 0 for fruit in fruits_prices}

# Loop for fruit selection
while True:
    # Displaying the list with numbers
    print(f"\nWelcome {user_name}. Which fruit would you like to buy?")
    for index, (fruit, price) in enumerate(fruits_prices.items(), start=1):
        print(f"{index}. {fruit} ${price}")

    # Get user input for the selected fruit
    selected_index = int(input("> "))

    # Validate user input
    if 1 <= selected_index <= len(fruits_prices):
        selected_fruit = list(fruits_prices.keys())[selected_index - 1]
        selected_price = fruits_prices[selected_fruit]
        total_cost += selected_price  # Accumulate total cost
        fruit_quantities[selected_fruit] += 1
        print(f"You bought 1 {selected_fruit.lower()} at ${selected_price}")

        # Ask if the user wants to buy another piece of fruit
        another_fruit = input("Would you like to buy another piece of fruit? (y/n)\n> ").lower()
        if another_fruit != 'y':
            break  # Exit the loop if the user does not want to buy another fruit
    else:
        print("Invalid selection. Please choose a valid number.")

# Display the order summary
print(f"\nOrder for {user_name}")
for fruit, quantity in fruit_quantities.items():
    if quantity > 0:
        print(f"{quantity} {fruit.lower()}(s) at ${fruits_prices[fruit]} apiece")

# Calculate subtotal, tax, and total
subtotal = sum(fruits_prices[fruit] * quantity for fruit, quantity in fruit_quantities.items())
tax = subtotal * 0.05
total = subtotal + tax

# Display the final amounts
print(f"Sub Total: ${subtotal:.2f}")
print(f"5% Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")





