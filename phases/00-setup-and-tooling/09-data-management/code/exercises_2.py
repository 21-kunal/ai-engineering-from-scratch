from datasets import load_dataset
import time

dataset = load_dataset("zaaabik/c4-parquet", split="train", streaming=True)

count = 0
start = time.time()

for example in dataset:
    count += 1
    if time.time() - start >= 10:
        break

elapsed = time.time() - start

print(f"Processed {count:,} examples in {elapsed:.2f} seconds")
print(f"Throughput: {count / elapsed:,.2f} examples/sec")
