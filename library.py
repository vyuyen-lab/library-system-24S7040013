library = []

def add_book():
    print("--- Add a New Book ---")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    
    
    book = {
        'title': title,
        'author': author,
        'is_available': True
    }
    
    
    library.append(book)
    print(f"Success! Book '{title}' added to library.")

def main():
    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book() 
        elif choice == '2':
            print("Feature coming soon...")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()