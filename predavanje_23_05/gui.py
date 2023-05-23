import tkinter as tk
from tkinter import messagebox
from bookshop import Book, Author, session


# LibraryApp
class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        self.search_label = tk.Label(self, text="Search:")
        self.search_label.pack()

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(self, text="Search", command=self.search_book)
        self.search_button.pack()

        self.search_result_label = tk.Label(self, text="")
        self.search_result_label.pack()

        # Input
        self.title_label = tk.Label(self, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(self)
        self.title_entry.pack()

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.surname_label = tk.Label(self, text="Surname:")
        self.surname_label.pack()

        self.surname_entry = tk.Entry(self)
        self.surname_entry.pack()

        self.save_button = tk.Button(self, text="Save", command=self.save_book)
        self.save_button.pack()

    def search_book(self):
        search_value = self.search_entry.get()
        self.search_result_label.config(text="")  # Clear the label

        if search_value:
            books = (
                session.query(Book)
                .join(Author)
                .filter(
                    Author.name.ilike(f"%{search_value}%")
                    | Author.surname.ilike(f"%{search_value}%")
                    | Book.title.ilike(f"%{search_value}%")
                )
                .all()
            )
            if books:
                book_info = "\n".join(
                    [f"Title: {book.title}, Author: {book.author}" for book in books]
                )
                self.search_result_label.config(text=book_info)
            else:
                self.search_result_label.config(text="No matching books found.")
        else:
            self.search_result_label.config(text="")

    def save_book(self):
        title = self.title_entry.get()
        name = self.name_entry.get()
        surname = self.surname_entry.get()

        if not title or not name or not surname:
            messagebox.showerror("Error", "Please enter title, name, and surname.")
            return

        author = session.query(Author).filter_by(name=name, surname=surname).first()
        if not author:
            new_author = Author(name=name, surname=surname)
            session.add(new_author)
            session.commit()
            author_id = new_author.id
        else:
            author_id = author.id

        new_book = Book(title=title, author_id=author_id)
        session.add(new_book)
        session.commit()

        messagebox.showinfo("Success", "Book added successfully.")

        self.title_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)


app = LibraryApp()
app.mainloop()
