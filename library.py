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

# Hàm mới: Hiển thị danh sách sách
def view_books():
    print("\n--- List of Books ---")
    if not library:
        print("No books in the library yet.")
    else:
        for book in library:
            # In ra thông tin sách như yêu cầu đề bài
            print(f"Title: {book['title']} | Author: {book['author']} | Available: {book['is_available']}")

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
            view_books() # Gọi hàm hiển thị sách
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()