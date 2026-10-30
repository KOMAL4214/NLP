import re
import pyarrow.parquet as pq
import pyarrow as pa


# Assignment-1 tokenizer

TOKEN_PATTERN = re.compile(r"""
    https?://[^\s]+|                       # URLs
    \b[\w.+-]+@[\w.-]+\.\w+\b|             # Email IDs
    \d{1,2}[/-]\d{1,2}[/-]\d{2,4}|         # Dates
    \d+\.\d+|                              # Decimal numbers
    [\u0C66-\u0C6F]+|                      # Telugu digits
    \d+|                                   # Integers
    [\u0C00-\u0C7F]+|                      # Telugu words
    [A-Za-z]+|                             # English words
    \.{3}|                                 # Ellipsis (...)
    [.,!?;:()"'\-]                         # Punctuation
""", re.VERBOSE)


def tokenize(sentence):
    return TOKEN_PATTERN.findall(sentence)


# Tokenize one parquet file

def process_file(input_file, output_file):

    pf = pq.ParquetFile(input_file)

    writer = None

    total = 0

    for batch in pf.iter_batches(
        batch_size=10_000,
        columns=["text"]
    ):

        sentences = batch["text"].to_pylist()

        tokenized = []

        for sentence in sentences:

            if sentence is None:
                continue

            tokens = tokenize(sentence)

            if not tokens:
                continue

            # Add sentence boundaries
            tokens = ["<START>"] + tokens + ["<END>"]

            # Store as space-separated tokens
            tokenized.append(" ".join(tokens))

        if not tokenized:
            continue

        table = pa.table({
            "tokens": tokenized
        })

        if writer is None:
            writer = pq.ParquetWriter(
                output_file,
                table.schema,
                compression="snappy"
            )

        writer.write_table(table)

        total += len(tokenized)

        print(
            f"{input_file}: processed {total} sentences"
        )

    if writer:
        writer.close()

    print(f"\nSaved: {output_file}")
    print(f"Total sentences: {total}")


# Process all three datasets

process_file(
    "train.parquet",
    "tokenized_train.parquet"
)

process_file(
    "dev.parquet",
    "tokenized_dev.parquet"
)

process_file(
    "test.parquet",
    "tokenized_test.parquet"
)