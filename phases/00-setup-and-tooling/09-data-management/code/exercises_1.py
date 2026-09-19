from datasets import load_dataset

dataset = load_dataset("nyu-mll/glue","mrpc")

print(dataset)

for i in range(5):
    
    print(i)
    print(dataset["train"][i])
    print(dataset["validation"][i])
    print(dataset["test"][i])
    print("-"*10)