# 📚 **Personal Library Manager**

> *"Manage your world of books right from the terminal."*

---

## 🎯 **Objective**
Create a command-line **Personal Library Manager** 🖥️ that lets users manage their book collection with ease. The program allows users to:

- ➕ Add books
- ❌ Remove books
- 🔍 Search for books
- 📋 Display all books
- 📊 View reading statistics
- 💾 Save/load books using file handling

---

## 💼 **Core Features**

### 📖 **Book Details**
Each book is stored as a **dictionary** with these fields:
- `Title` (string)
- `Author` (string)
- `Publication Year` (integer)
- `Genre` (string)
- `Read Status` (boolean: ✅ if read, ❌ if unread)

### 📜 **Menu System**
- `1️⃣ Add a book`
- `2️⃣ Remove a book`
- `3️⃣ Search for a book`
- `4️⃣ Display all books`
- `5️⃣ Display statistics`
- `6️⃣ Exit`

---

## 🔧 **Functional Breakdown**

### ➕ **Add a Book**
Prompts user for details and adds book to library.
✅ Saved successfully.

### ❌ **Remove a Book**
Takes book title as input and removes it from the library.
🗑️ Success message on deletion.

### 🔍 **Search for a Book**
- User can search by `Title` or `Author`
- Displays all matching results

### 📋 **Display All Books**
Formatted output of all books in the library:
```
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - ✅ Read
2. 1984 by George Orwell (1949) - Dystopian - ❌ Unread
```

### 📊 **Display Statistics**
- 📚 Total number of books
- ✅ Number and percentage of read books
- ❌ Number and percentage of unread books

### 🔚 **Exit**
- Saves library to a file before exiting.
- 💾 File used: `library.txt`
- 👋 Displays farewell message

---

## 💡 **Implementation Notes**
- Data is stored in a **list of dictionaries** 🗂️
- Menu uses `loops` and `conditionals` to keep interaction going
- `String formatting` for clean output
- `Type casting` is used for input values
- Uses `json` module for file I/O

---

## 💾 **Optional Challenge Completed**
- ✅ *Save library to file (`library.txt`) on exit*
- ✅ *Load library from file on startup*
- Uses `json.dump()` and `json.load()` for easy data serialization

---

## 🖼️ **Sample Output**
```bash
Welcome to your Personal Library Manager!

1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
Enter your choice: 1

Enter the book title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the publication year: 1925
Enter the genre: Fiction
Have you read this book? (yes/no): yes
Book added successfully!
```

---

## 📦 **Technologies Used**
- `Python 3` 🐍
- `Colorama` 🎨 (for colored terminal output)
- `JSON` 📄 (for saving/loading library)

---

## 🧠 **Skills Demonstrated**
- File handling
- Loop control
- Conditionals
- User input validation
- String formatting
- Clean code structure

---

## 🤝 **Contribution & Usage**
Feel free to fork or clone this repo and enhance it with more features like:
- Sorting by author/year 📅
- GUI integration with Tkinter or PyQt 🎨
- Export to PDF/CSV 📄

PRs are welcome. 🙌

---

## 📜 **License**
MIT License

> Made with ❤️ by Ashna Ghazanfar 
> *Because every book deserves a place on your shelf.*

