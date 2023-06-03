from tkinter import (
    Frame,
    Label,
    Button,
    Entry,
    Listbox,
    BooleanVar,
    Scrollbar,
    Checkbutton,
    END,
)
from tkinter.messagebox import showinfo
from database import User, session


class SmartKeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Key App")
        self.root.geometry("800x400")

        self.status_label = Label(self.root, text="Dobro došli!", pady=10)
        self.status_label.pack()

        self.button_frame = Frame(self.root)
        self.button_frame.pack()

        self.ring_button = Button(
            self.button_frame, text="Pozvoniti", command=self.ring
        )
        self.ring_button.pack(side="left")

        self.unlock_button = Button(
            self.button_frame, text="Otključati", command=self.unlock
        )
        self.unlock_button.pack(side="left")

    def ring(self):
        self.status_label.config(text="Zvono aktivirano!")

    def unlock(self):
        self.button_frame.destroy()
        self.status_label.config(text="Unesite PIN:")
        self.pin_entry = Entry(self.root, show="*")
        self.pin_entry.pack()
        self.confirm_button = Button(self.root, text="Potvrdi", command=self.check_pin)
        self.confirm_button.pack()
        self.cancel_pin = Button(self.root, text="Reset", command=self.reset_pin)
        self.cancel_pin.pack()
        self.pin_buttons_frame = Frame(self.root)
        self.pin_buttons_frame.pack()

        self.pin_buttons = []
        for i in range(1, 10):
            button = Button(
                self.pin_buttons_frame,
                text=str(i),
                command=lambda i=i: self.add_pin_digit(i),
                width=4,
                height=2,
            )
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3)
            self.pin_buttons.append(button)

        # Add "0" button separately because of the layout
        button_zero = Button(
            self.pin_buttons_frame,
            text="0",
            command=lambda: self.add_pin_digit(0),
            width=4,
            height=2,
        )
        button_zero.grid(
            row=3, column=1, columnspan=1
        )  
        self.pin_buttons.append(button_zero)

    def reset_pin(self):
        self.pin_entry.delete(0, END)

    def add_pin_digit(self, digit):
        current_pin = self.pin_entry.get()
        current_pin += str(digit)
        self.pin_entry.delete(0, END)
        self.pin_entry.insert(END, current_pin)

    def check_pin(self):
        pin = self.pin_entry.get()
        user = session.query(User).filter_by(pin=pin).first()
        if user:
            self.status_label.config(
                text=f"Uspješno unesen PIN!\nDobro došli, {user.name} {user.surname}!"
            )
            if pin == "0000":
                self.open_admin_panel()
        else:
            showinfo("Pogrešan PIN", "Unijeli ste pogrešan PIN!")

    def open_admin_panel(self):
        self.pin_entry.destroy()
        self.cancel_pin.destroy()
        self.confirm_button.destroy()
        self.pin_buttons_frame.destroy()
        self.status_label.config(text="Administracija sustava")

        self.users_frame = Frame(self.root)
        self.users_frame.pack(side="left", fill="y")

        self.users_listbox = Listbox(self.users_frame, selectmode="single")
        self.users_listbox.pack(side="left", fill="y")

        self.users_scrollbar = Scrollbar(self.users_frame)
        self.users_scrollbar.pack(side="right", fill="y")

        self.users_listbox.config(yscrollcommand=self.users_scrollbar.set)
        self.users_scrollbar.config(command=self.users_listbox.yview)

        self.update_users_list()

        form_frame = Frame(self.root)
        form_frame.pack(side="right", padx=10, pady=10)

        self.name_label = Label(form_frame, text="Ime:")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = Entry(form_frame)
        self.name_entry.grid(row=0, column=1)

        self.surname_label = Label(form_frame, text="Prezime:")
        self.surname_label.grid(row=1, column=0, sticky="e")
        self.surname_entry = Entry(form_frame)
        self.surname_entry.grid(row=1, column=1)

        self.id_label = Label(form_frame, text="ID:")
        self.id_label.grid(row=2, column=0, sticky="e")
        self.id_entry = Entry(form_frame)
        self.id_entry.grid(row=2, column=1)

        self.pin_label = Label(form_frame, text="PIN:")
        self.pin_label.grid(row=3, column=0, sticky="e")
        self.pin_entry = Entry(form_frame, show="*")
        self.pin_entry.grid(row=3, column=1)

        self.active_var = BooleanVar()
        self.active_checkbox = Checkbutton(
            form_frame, text="Aktivan", variable=self.active_var
        )
        self.active_checkbox.grid(row=4, columnspan=2, sticky="w")

        self.edit_button = Button(form_frame, text="Uredi", command=self.edit_user)
        self.edit_button.grid(row=5, column=0, sticky="e")
        self.save_button = Button(form_frame, text="Spremi", command=self.save_user)
        self.save_button.grid(row=5, column=1, sticky="w")
        self.delete_button = Button(
            form_frame, text="Izbriši", command=self.delete_user
        )
        self.delete_button.grid(row=6, column=0, sticky="e")

        self.cancel_button = Button(
            form_frame, text="Odustani", command=self.clear_fields
        )
        self.cancel_button.grid(row=6, column=1, sticky="w")

    def update_users_list(self):
        self.users_listbox.delete(0, END)  
        users = session.query(User).all()
        for user in users:
            self.users_listbox.insert(END, f"{user.name} {user.surname}")

    def edit_user(self):
        selected_user = self.users_listbox.get(self.users_listbox.curselection())
        name, surname = selected_user.split(" ", 1)
        user = session.query(User).filter_by(name=name, surname=surname).first()
        self.active_checkbox.select() if user.active else self.active_checkbox.deselect()
        self.name_entry.delete(0, END)
        self.name_entry.insert(END, user.name)
        self.surname_entry.delete(0, END)
        self.surname_entry.insert(END, user.surname)
        self.id_entry.delete(0, END)
        self.id_entry.insert(END, user.id)
        self.pin_entry.delete(0, END)
        self.pin_entry.insert(END, user.pin)

    def save_user(self):
        user_id = self.id_entry.get()
        pin = self.pin_entry.get()

        if not user_id or not pin:
            showinfo("Greška", "ID i PIN moraju biti uneseni.")
            return

        name = self.name_entry.get()
        surname = self.surname_entry.get()
        active = True if self.active_var.get() else False

        try:
            user_id = int(user_id)
        except ValueError:
            showinfo("Greška", "ID mora biti cijeli broj.")
            return

        existing_user = session.query(User).filter_by(id=user_id).first()
        if existing_user:
            existing_user.name = name
            existing_user.surname = surname
            existing_user.pin = pin
            existing_user.active = active
        else:
            user = User(id=user_id, pin=pin, name=name, surname=surname, active=active)
            session.add(user)

        session.commit()
        showinfo("Spremljeno", "Promjene su spremljene!")
        self.update_users_list()
        self.clear_fields()

    def delete_user(self):
        selected_user = self.users_listbox.get(self.users_listbox.curselection())
        name, surname = selected_user.split(" ", 1)
        user = session.query(User).filter_by(name=name, surname=surname).first()
        session.delete(user)
        session.commit()
        self.users_listbox.delete(self.users_listbox.curselection())
        showinfo("Izbrisano", "Korisnik je izbrisan!")
        self.clear_fields()  

    def clear_fields(self):
        self.name_entry.delete(0, END)
        self.surname_entry.delete(0, END)
        self.pin_entry.delete(0, END),
        self.id_entry.delete(0, END)
        self.active_checkbox.deselect()
