class Dataset:
    def __init__(self,name, num_rows, num_features):
        self.name = name
        self.num_rows = num_rows
        self.num_features = num_features
        self.status = "Not Loaded"

    def show_info(self):
        print(f"{self.name}, {self.num_rows}, {self.num_features}, {self.status}")

    def load(self):
        if self.status == "Loaded":
            print("Dataset is already loaded, Cannot Load again, Unload first.")
            return
        else:
            self.status = "Loaded"
            print("Change to Loaded!")

    def unload(self):
        if self.status == "Not Loaded":
            print("Its not Loaded, please Load first.")
            return
        else:
            self.status = "Not Loaded"
            print("It has been unloaded!")

    def is_loaded(self):
        if self.status == "Loaded":
            return True
        else:
            return False
