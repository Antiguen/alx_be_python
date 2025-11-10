def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print("-" * 20) # Separator for cleaner output

        if choice == '1':
            # 1. Add Item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: # Ensure the user didn't enter an empty string
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # 2. Remove Item
            if not shopping_list:
                print("The list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")

        elif choice == '3':
            # 3. View List
            if shopping_list:
                print("Current Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            # 4. Exit
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
