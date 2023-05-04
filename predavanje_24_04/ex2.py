import os


class FileData:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_data(self, data):
        with open(self.file_path, "a") as file:
            file.write(data + "\n")

    def delete_data(self, data):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        with open(self.file_path, "w") as file:
            for line in lines:
                if line.strip() != data:
                    file.write(line)

    def load_data(self):
        with open(self.file_path, "r") as file:
            return file.readlines()

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            for item in data:
                file.write(item + "\n")


if __name__ == "__main__":
    file_path = "predavanje_24_04/data.txt"

    # create the file if it doesn't exist
    if not os.path.isfile(file_path):
        open(file_path, "w").close()

    # create a FileData object and add, delete, load, and save data
    file_data = FileData(file_path)
    file_data.add_data("test1")
    file_data.add_data("test2")
    file_data.add_data("test3")
    file_data.delete_data("test2")
    data = file_data.load_data()
    file_data.save_data(data)
