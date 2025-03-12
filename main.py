def greeting(name): 
    print(f'Hello {name}, what can I do for you today?')

def choice(action):
    if action.lower() == "returning":
        process_return()
    elif action.lower() == "exchanging":
        process_exchange()
    else:
        print("I'm sorry, I didn't understand that. Please type 'returning' or 'exchanging'.")

available_items = ["shirt", "pants", "jacket", "shoes", "hat", "scarf", "gloves", "sweater", "jeans", "coat"] 

def process_return():
    items = []
    while True:
        item = input("Please enter the name of the item you'd like to return (type 'done' to exit): ")
        if item.lower() == 'done':
            break
        if item in available_items:
            items.append(item)
        else:
            print("This item is not available for return.")
    print("Thank you. Your return requests have been received:")
    for item in items:
        print(f'- {item}')

def process_exchange():
    while True:
        item = input("Please enter the name of the item you'd like to exchange (type 'done' to exit): ")
        if item.lower() == 'done':
            break
        print("Available items for exchange:")
        print(', '.join(available_items))
        new_item = input(f"Enter the name of the item you'd like in exchange for {item}: ")
        if new_item.lower() in available_items:
            available_items.append(item)  # Add the exchanged item back to the available items
            available_items.remove(new_item)  # Remove the new item from available items
            print(f'{item} has been exchanged for {new_item}.')
        else:
            print("This item is not available for exchange.")
    print("Your updated available item list:")
    print(', '.join(available_items))


if __name__ == "__main__": 
    while True:
        greeting("Jay")
        action = input("Are you returning or exchanging an item? ")
        choice(action)