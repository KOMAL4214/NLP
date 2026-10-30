import pyarrow.parquet as pq
import pyarrow as pa
import random

INPUT_FILE = "../ASS-1/all_sentences.parquet"

OUTPUT_TRAIN = "train.parquet"
OUTPUT_DEV = "dev.parquet"
OUTPUT_TEST = "test.parquet"

TOTAL_SENTENCES = 1_000_000
TRAIN_SIZE = 998_000
DEV_SIZE = 1_000
TEST_SIZE = 1_000

SEED = 42

# 1. Open Parquet file

pf = pq.ParquetFile(INPUT_FILE)

print("Total rows:", pf.metadata.num_rows)
print("Row groups:", pf.num_row_groups)

# 2. Find enough random row groups

random.seed(SEED)

row_group_ids = list(range(pf.num_row_groups))
random.shuffle(row_group_ids)

selected_groups = []
total_rows = 0

for rg in row_group_ids:
    rows = pf.metadata.row_group(rg).num_rows

    selected_groups.append(rg)
    total_rows += rows

    if total_rows >= TOTAL_SENTENCES:
        break

print("Selected row groups:", len(selected_groups))
print("Rows available from selected groups:", total_rows)

# 3. Read selected row groups

table = pf.read_row_groups(
    selected_groups,
    columns=["text"]
)

print("Loaded rows:", table.num_rows)

# 4. Convert to Python list

sentences = table["text"].to_pylist()

# Remove null/empty sentences
sentences = [
    s.strip()
    for s in sentences
    if s is not None and s.strip()
]

print("Valid sentences:", len(sentences))

# 5. Shuffle

random.shuffle(sentences)

# Take exactly 1 million
sentences = sentences[:TOTAL_SENTENCES]

print("Using:", len(sentences), "sentences")

# 6. Split

train_sentences = sentences[:TRAIN_SIZE]

dev_sentences = sentences[
    TRAIN_SIZE:
    TRAIN_SIZE + DEV_SIZE
]

test_sentences = sentences[
    TRAIN_SIZE + DEV_SIZE:
]

print()
print("Train:", len(train_sentences))
print("Dev:", len(dev_sentences))
print("Test:", len(test_sentences))

# 7. Save as Parquet

def save_parquet(sentences, filename):
    table = pa.table({
        "text": sentences
    })

    pq.write_table(
        table,
        filename,
        compression="snappy"
    )

    print("Saved:", filename)


save_parquet(train_sentences, OUTPUT_TRAIN)
save_parquet(dev_sentences, OUTPUT_DEV)
save_parquet(test_sentences, OUTPUT_TEST)

print("\nDone!")