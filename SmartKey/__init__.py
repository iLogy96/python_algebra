from tkinter import Tk
from app import SmartKeyApp
from database import session

# Pokretanje aplikacije
if __name__ == "__main__":
    root = Tk()
    app = SmartKeyApp(root)
    root.mainloop()
