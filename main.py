import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect("ebook_manager.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ebooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            year INTEGER
        )
    """)
    conn.commit()
    conn.close()

# Add a new e-book
def add_ebook(title, author, genre, year):
    conn = sqlite3.connect("ebook_manager.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ebooks (title, author, genre, year)
        VALUES (?, ?, ?, ?)
    """, (title, author, genre, year))
    conn.commit()
    conn.close()
    print("E-book added successfully!")

# View all e-books
def view_ebooks():
    conn = sqlite3.connect("ebook_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ebooks")
    ebooks = cursor.fetchall()
    conn.close()
    print("\nE-book Collection:")
    for ebook in ebooks:
        print(f"ID: {ebook[0]}, Title: {ebook[1]}, Author: {ebook[2]}, Genre: {ebook[3]}, Year: {ebook[4]}")
    print()

# Search for an e-book
def search_ebooks(query):
    conn = sqlite3.connect("ebook_manager.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM ebooks WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?
    """, (f"%{query}%", f"%{query}%", f"%{query}%"))
    results = cursor.fetchall()
    conn.close()
    if results:
        print("\nSearch Results:")
        for ebook in results:
            print(f"ID: {ebook[0]}, Title: {ebook[1]}, Author: {ebook[2]}, Genre: {ebook[3]}, Year: {ebook[4]}")
    else:
        print("No matching e-books found.")
    print()

# Update an e-book
def update_ebook(ebook_id, title, author, genre, year):
    conn = sqlite3.connect("ebook_manager.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ebooks
        SET title = ?, author = ?, genre = ?, year = ?
        WHERE id = ?
    """, (title, author, genre, year, ebook_id))
    conn.commit()
    conn.close()
    print("E-book updated successfully!")

# Delete an e-book
def delete_ebook(ebook_id):
    conn = sqlite3.connect("ebook_manager.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ebooks WHERE id = ?", (ebook_id,))
    conn.commit()
    conn.close()
    print("E-book deleted successfully!")

# Main menu
def main():
    init_db()
    while True:
        print("\nE-book Management System")
        print("1. Add E-book")
        print("2. View All E-books")
        print("3. Search E-books")
        print("4. Update E-book")
        print("5. Delete E-book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            year = input("Enter year: ")
            add_ebook(title, author, genre, year)
        elif choice == "2":
            view_ebooks()
        elif choice == "3":
            query = input("Enter search query (title/author/genre): ")
            search_ebooks(query)
        elif choice == "4":
            ebook_id = int(input("Enter e-book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            genre = input("Enter new genre: ")
            year = input("Enter new year: ")
            update_ebook(ebook_id, title, author, genre, year)
        elif choice == "5":
            ebook_id = int(input("Enter e-book ID to delete: "))
            delete_ebook(ebook_id)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
