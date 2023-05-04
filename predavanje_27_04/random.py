import os
import datetime


class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.history = []

    def add_data(self, new_data):
        self.data.append(new_data)
        self.history.append(
            {"action": "PUSH", "data": new_data, "timestamp": datetime.datetime.now()}
        )

    def get_data(self):
        with open(self.filename, "r") as f:
            for line in f:
                print(line.strip(),end="")

    def delete_data(self, index):
        if index >= len(self.data):
            raise IndexError("Index out of range")
        deleted_data = self.data.pop(index)
        self.history.append(
            {
                "action": "POP",
                "data": deleted_data,
                "timestamp": datetime.datetime.now(),
            }
        )

    def load_data(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError("File not found")
        with open(self.filename, "r") as f:
            self.data = [line.strip() for line in f.readlines()]

    def save_data(self):
        with open(self.filename, "w") as f:
            for item in self.data:
                f.write(str(item) + "\n")

    def get_history(self):
        history = []
        for entry in self.history:
            action = entry["action"]
            data = entry["data"]
            timestamp = entry["timestamp"].strftime("%d.%m.%Y (%a) %H:%M")
            history.append(f"{action} {data} {timestamp}")
        return history


file_manager = FileManager("predavanje_27_04/my_file.txt")

file_manager.add_data("Hello")
file_manager.add_data("World")

file_manager.delete_data(1)

file_manager.load_data()

file_manager.save_data()

print(file_manager.get_history())
print(file_manager.get_data())
