
from colorama import init, Fore, Back, Style
init(autoreset=True)

import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    print(Fore.YELLOW + "\n📚 Let's add a new book!")
    title = input("📖 Enter book title: ")
    author = input("✍️ Enter book author: ")
    year = input("📅 Enter publication year: ")
    genre = input("🎭 Enter book genre: ")
    read = input("✅ Have you read this book? (yes/no): ").lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(new_book)
    save_library(library)
    print(Fore.GREEN + f"🎉 Book '{title}' added to the library!")

def remove_book(library):
    print(Fore.RED + "\n🗑️ Remove a Book")
    title = input("Enter the title of the book to remove: ").lower()
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:
        save_library(library)
        print(Fore.GREEN + f"✅ Book '{title}' removed from the library.")
    else:
        print(Fore.RED + f"❌ Book '{title}' not found.")

def search_book(library):
    print(Fore.CYAN + "\n🔍 Search for a Book")
    search_by = input("Search by (title/author): ").lower()
    if search_by not in ['title', 'author']:
        print(Fore.RED + "⚠️ Invalid search type. Choose 'title' or 'author'.")
        return
    search_term = input(f"Enter the {search_by}: ").lower()
    found_books = [book for book in library if search_term in book[search_by].lower()]
    if found_books:
        print(Fore.YELLOW + f"\n🔎 Found {len(found_books)} matching book(s):")
        for book in found_books:
            status = "✅ Read" if book['read'] else "❌ Not Read"
            print(Fore.GREEN + f"\n📖 Title: {book['title']}")
            print(Fore.BLUE + f"✍️  Author: {book['author']}")
            print(Fore.MAGENTA + f"📅 Year: {book['year']}")
            print(Fore.YELLOW + f"🎭 Genre: {book['genre']}")
            print(Fore.CYAN + f"📘 Status: {status}")
    else:
        print(Fore.RED + "❌ No matching books found.")

def display_books(library):
    print(Fore.YELLOW + "\n📚 All Books in Your Library")
    if library:
        for book in library:
            status = "✅ Read" if book['read'] else "❌ Not Read"
            print(Fore.GREEN + f"\n📖 Title: {book['title']}")
            print(Fore.BLUE + f"✍️  Author: {book['author']}")
            print(Fore.MAGENTA + f"📅 Year: {book['year']}")
            print(Fore.YELLOW + f"🎭 Genre: {book['genre']}")
            print(Fore.CYAN + f"📘 Status: {status}")
    else:
        print(Fore.RED + "📭 No books in the library yet.")

def display_statistics(library):
    print(Fore.YELLOW + "\n📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    unread_books = total_books - read_books
    percent_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(Fore.CYAN + f"📚 Total books: {total_books}")
    print(Fore.GREEN + f"✅ Books read: {read_books}")
    print(Fore.RED + f"❌ Books not read: {unread_books}")
    print(Fore.MAGENTA + f"📈 Percentage read: {percent_read:.1f}%")

def main():
    library = load_library()
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n📘 Library Management System")
        print("1️⃣  Add Book")
        print("2️⃣  Remove Book")
        print("3️⃣  Search Book")
        print("4️⃣  Display All Books")
        print("5️⃣  Display Statistics")
        print("6️⃣  Exit")

        choice = input(Fore.WHITE + "\n➡️  Enter your choice(in numbers): ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print(Fore.GREEN + "\n💾 Library saved. Goodbye! 👋")
            break
        else:
            print(Fore.RED + "⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
