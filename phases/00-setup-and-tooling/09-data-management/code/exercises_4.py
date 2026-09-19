from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")
split = dataset.train_test_split(0.30)
test_val_split = split["test"].train_test_split(0.5)

train_split = split["train"]
test_split = test_val_split["train"]
val_split = test_val_split["test"]


print(len(train_split) / len(dataset))
print(len(test_split) / len(dataset))
print(len(val_split) / len(dataset))
