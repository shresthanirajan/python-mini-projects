from dataset import Dataset
from model import Model
dataset1 = Dataset("Jack", 10, 15)
dataset2 = Dataset("Ram", 20, 30)

model1 = Model("cryptech", "classification","1")

dataset1.load()
model1.train(dataset1)


