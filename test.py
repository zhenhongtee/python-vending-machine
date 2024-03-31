'''You are tasked to code the vending machine logic out using Python Programming Language. 
In your code, you can have a few drinks as your items with any price (no coin). The customer should be able to insert any notes to buy his preferred drinks. 
The outcome is to release the least amount of notes back to the customer. '''

# Define available drink names and their prices in a dictionary
drinks = {
    "A": {"name": "Coke", "price": 1.50},
    "B": {"name": "Water", "price": 0.80},
}

# Define available notes to be returned
notes = [0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50, 100]

# Track inserted notes and total amount inserted
inserted_notes = {}
total = 0

while True:
    # Display available drinks and prices
    print("Drinks:")
    for drink_id, drink in drinks.items():
        print(f"{drink_id}: {drink["name"]}(MYR {drink["price"]:.2f})")

    while True:
        note_val = input("\nEnter note (MYR): ")
        try:
            note_val = float(note_val)
            if note_val <= 0:
                print("Please enter a positive number.")
            else:
                # Append note in inserted_notes dictionary
                inserted_notes[note_val] = inserted_notes.get(note_val, 0) + 1
                total += note_val
                break
        except ValueError:
            print("Please enter a number.")

    # Display inserted notes
    print("\nInserted notes:")
    for note, quantity in inserted_notes.items():
        if quantity > 0:
            print(f"{quantity} x MYR {note:.2f}")

    # Prompts user to select drink from available drinks
    drink_selected = input("\nEnter drink id:")

    if drink_selected not in drinks:
        print("Invalid drink id.")
        continue
    
    drink_price = drinks[drink_selected]["price"]

    if total < drink_price:
        print(f"Your payment is insufficient. The price of {drinks[drink_selected]["name"]} is MYR {drink_price:.2f}")
        continue
    
    change = total - drink_price
    change_given = {}

    for note in notes[::-1]:
        if change >= note:
            count = change // note
            change_given[note] = count
            change -= count * note
    
    for note, quantity in change_given.items():
        if quantity > 0:
            print(f"Returning: {quantity} x MYR {note:.2f}")

    break

