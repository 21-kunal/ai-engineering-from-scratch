from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

csv_size = dataset.to_csv("imdb_train.csv")
parquet_size = dataset.to_parquet("imdb_train.parquet")

csv_mb = csv_size / (1024**2)
parquet_mb = parquet_size / (1024**2)
size_diff_mb = parquet_mb - csv_mb

print(f"CSV size: {csv_mb:.2f} MB")
print(f"Parquet size: {parquet_mb:.2f} MB")
print(f"Size difference: {size_diff_mb:.2f} MB")
