import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
from PIL import ImageTk, Image


# Database functions
def create_table():
    conn = sqlite3.connect('floral.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS plants
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  image BLOB,
                  soil_moisture TEXT,
                  light_requirement TEXT,
                  substrate_recommendation TEXT)''')
    conn.commit()
    conn.close()


def insert_plant(name, image_path, soil_moisture, light_requirement, substrate_recommendation):
    conn = sqlite3.connect('floral.db')
    c = conn.cursor()

    with open(image_path, 'rb') as f:
        image_data = f.read()

    c.execute('''INSERT INTO plants (name, image, soil_moisture, light_requirement, substrate_recommendation)
                 VALUES (?, ?, ?, ?, ?)''', (name, image_data, soil_moisture, light_requirement, substrate_recommendation))

    conn.commit()
    conn.close()


def update_plant(plant_id, name, image_path, soil_moisture, light_requirement, substrate_recommendation):
    conn = sqlite3.connect('floral.db')
    c = conn.cursor()

    if image_path:
        with open(image_path, 'rb') as f:
            image_data = f.read()

        c.execute('''UPDATE plants SET name=?, image=?, soil_moisture=?, light_requirement=?, substrate_recommendation=?
                     WHERE id=?''', (name, image_data, soil_moisture, light_requirement, substrate_recommendation, plant_id))
    else:
        c.execute('''UPDATE plants SET name=?, soil_moisture=?, light_requirement=?, substrate_recommendation=?
                     WHERE id=?''', (name, soil_moisture, light_requirement, substrate_recommendation, plant_id))

    conn.commit()
    conn.close()


def delete_plant(plant_id):
    conn = sqlite3.connect('floral.db')
    c = conn.cursor()
    c.execute('DELETE FROM plants WHERE id=?', (plant_id,))
    conn.commit()
    conn.close()


def get_all_plants():
    conn = sqlite3.connect('floral.db')
    c = conn.cursor()
    c.execute('SELECT * FROM plants')
    plants = c.fetchall()
    conn.close()
    return plants


# GUI functions
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_image.delete(0, tk.END)
    entry_soil_moisture.delete(0, tk.END)
    entry_light_requirement.delete(0, tk.END)
    entry_substrate_recommendation.delete(0, tk.END)


def browse_image():
    filetypes = (("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
    filepath = filedialog.askopenfilename(title="Select Image", filetypes=filetypes)
    entry_image.delete(0, tk.END)
    entry_image.insert(0, filepath)


def show_plants():
    plants_listbox.delete(0, tk.END)
    plants = get_all_plants()
    for plant in plants:
        plants_listbox.insert(tk.END, plant[1])


def show_selected_plant(event):
    index = plants_listbox.curselection()
    if index:
        plant = get_all_plants()[index[0]]
        display_plant_details(plant)


def display_plant_details(plant):
    clear_entries()

    plant_id, name, image_data, soil_moisture, light_requirement, substrate_recommendation = plant

    entry_name.insert(0, name)
    entry_soil_moisture.insert(0, soil_moisture)
    entry_light_requirement.insert(0, light_requirement)
    entry_substrate_recommendation.insert(0, substrate_recommendation)

    if image_data:
        image = Image.open(image_data)
        image.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(image)
        label_image.configure(image=photo)
        label_image.image = photo


def add_plant():
    name = entry_name.get()
    image_path = entry_image.get()
    soil_moisture = entry_soil_moisture.get()
    light_requirement = entry_light_requirement.get()
    substrate_recommendation = entry_substrate_recommendation.get()

    if not name or not soil_moisture or not light_requirement or not substrate_recommendation:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        insert_plant(name, image_path, soil_moisture, light_requirement, substrate_recommendation)
        clear_entries()
        show_plants()
        messagebox.showinfo("Success", "Plant added successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_selected_plant():
    index = plants_listbox.curselection()
    if index:
        plant = get_all_plants()[index[0]]
        plant_id = plant[0]

        name = entry_name.get()
        image_path = entry_image.get()
        soil_moisture = entry_soil_moisture.get()
        light_requirement = entry_light_requirement.get()
        substrate_recommendation = entry_substrate_recommendation.get()

        if not name or not soil_moisture or not light_requirement or not substrate_recommendation:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            update_plant(plant_id, name, image_path, soil_moisture, light_requirement, substrate_recommendation)
            clear_entries()
            show_plants()
            messagebox.showinfo("Success", "Plant updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def delete_selected_plant():
    index = plants_listbox.curselection()
    if index:
        plant = get_all_plants()[index[0]]
        plant_id = plant[0]
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this plant?")
        if confirm:
            try:
                delete_plant(plant_id)
                clear_entries()
                show_plants()
                messagebox.showinfo("Success", "Plant deleted successfully.")
            except Exception as e:
                messagebox.showerror("Error", str(e))


# Initialize the GUI
root = tk.Tk()
root.title("Floral Management System")
root.geometry("800x600")

# Database setup
create_table()

# Plants list
plants_frame = tk.Frame(root)
plants_frame.pack(side=tk.LEFT, fill=tk.Y)

plants_label = tk.Label(plants_frame, text="Plants")
plants_label.pack()

plants_listbox = tk.Listbox(plants_frame)
plants_listbox.pack(fill=tk.Y)
plants_listbox.bind('<<ListboxSelect>>', show_selected_plant)

scrollbar = tk.Scrollbar(plants_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
plants_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=plants_listbox.yview)

show_plants()

# Plant details
details_frame = tk.Frame(root)
details_frame.pack(side=tk.RIGHT)

label_name = tk.Label(details_frame, text="Name")
label_name.pack()
entry_name = tk.Entry(details_frame)
entry_name.pack()

label_image = tk.Label(details_frame)
label_image.pack()

label_image_path = tk.Label(details_frame, text="Image Path")
label_image_path.pack()
entry_image = tk.Entry(details_frame)
entry_image.pack()

button_browse = tk.Button(details_frame, text="Browse", command=browse_image)
button_browse.pack()

label_soil_moisture = tk.Label(details_frame, text="Soil Moisture")
label_soil_moisture.pack()
entry_soil_moisture = tk.Entry(details_frame)
entry_soil_moisture.pack()

label_light_requirement = tk.Label(details_frame, text="Light Requirement")
label_light_requirement.pack()
entry_light_requirement = tk.Entry(details_frame)
entry_light_requirement.pack()

label_substrate_recommendation = tk.Label(details_frame, text="Substrate Recommendation")
label_substrate_recommendation.pack()
entry_substrate_recommendation = tk.Entry(details_frame)
entry_substrate_recommendation.pack()

button_add = tk.Button(details_frame, text="Add Plant", command=add_plant)
button_add.pack()

button_update = tk.Button(details_frame, text="Update Plant", command=update_selected_plant)
button_update.pack()

button_delete = tk.Button(details_frame, text="Delete Plant", command=delete_selected_plant)
button_delete.pack()

root.mainloop()
