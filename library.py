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

def view_books():
    print("\n--- List of Books ---")
    if not library:
        print("No books in the library yet.")
    else:
        for book in library:
            print(f"Title: {book['title']} | Author: {book['author']} | Available: {book['is_available']}")

# Hàm mới: Tìm kiếm sách
def search_book():
    print("\n--- Search for a Book ---")
    query = input("Enter search keyword: ").lower() # Chuyển về chữ thường để tìm cho dễ
    
    found = False
    for book in library:
        # Kiểm tra xem từ khóa có nằm trong tên sách không
        if query in book['title'].lower():
            print(f"FOUND: Title: {book['title']} | Author: {book['author']}")
            found = True
            
    if not found:
        print("No matching books found.")

def main():
    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Search book") # Thêm mục này
        print("4. Exit")       # Đẩy Exit xuống số 4
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book() # Gọi hàm tìm kiếm
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()