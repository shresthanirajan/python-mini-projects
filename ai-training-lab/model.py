class Model:
    def __init__(self, name, model_type,version):
        self.name = name
        self.model_type = model_type
        self.version = version
        self.status = "Not Trained"
        self.trained_on = None

    def train(self, other_dataset):

        if other_dataset.is_loaded():
            print("Is Loaded")
        else:
            print("Not Loaded")
            return

        if self.status == "Trained":
            print(f"{self.name} is already Trained!")
            return
        else:
            self.status = "Trained"
            print(f"{self.name} has been successfully Trained!")
            self.trained_on = other_dataset
