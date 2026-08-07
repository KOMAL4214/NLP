# Assignment 1 - Telugu Sentence and Word Tokenizer

## Student Information

**Course:** Natural Language Processing (NLP)

**Assignment:** Assignment 1 – Sentence Tokenizer, Word Tokenizer and Corpus Statistics

**Language:** Telugu

---

# Objective

The objective of this assignment is to build a rule-based NLP preprocessing pipeline for the Telugu language.

The implemented pipeline performs:

- Dataset preprocessing
- Sentence tokenization
- Word tokenization
- Saving the tokenized corpus into Parquet files
- Computing corpus statistics

---

# Dataset

The Telugu corpus used in this assignment was obtained from the AI4Bharat IndicCorpV2 dataset hosted on Hugging Face.

Dataset Link:

https://huggingface.co/datasets/ai4bharat/IndicCorpV2

Language Used:

```
Telugu
```

The original extracted text corpus (`te.txt`) is approximately **15.8 GB**.

---

# Assignment Tasks

## Task 1

Downloaded the Telugu corpus from the AI4Bharat IndicCorpV2 dataset.

Extracted the Telugu text into a plain text file (`te.txt`) for further processing.

---

## Task 2

Implemented the following tokenizers.

### Sentence Tokenizer

A rule-based sentence tokenizer was implemented using Python Regular Expressions.

Sentence boundaries are detected using the following punctuation marks:

- `.`
- `!`
- `?`

Regex used:

```python
r'(?<=[.!?])\s+'
```

Each detected sentence is stored as an individual record.

---

### Word Tokenizer

A rule-based word tokenizer was implemented using Regular Expressions.

The tokenizer recognizes the following token types.

- Telugu words
- English words
- URLs
- Email IDs
- Integer numbers
- Decimal numbers
- Dates
- Ellipsis (`...`)
- Punctuation symbols

Examples

```
అమెరికా
రాష్ట్రపతి
OpenAI
https://example.com
abc@gmail.com
12.56
12/05/2024
.
,
?
!
```

Each token is stored independently.

---

## Task 3

The generated outputs are stored in Apache Parquet format.

Generated files:

```
all_sentences.parquet
```

Contains one sentence per row.

```
all_words.parquet
```

Contains one token per row.

---

## Task 4

Computed the following corpus statistics.

- Total number of sentences
- Total number of words
- Total number of characters
- Average sentence length
- Average word length
- Type Token Ratio (TTR)

---

# Text Preprocessing

Before tokenization, the corpus was preprocessed using the following operations.

- Removed empty lines
- Removed leading and trailing whitespace
- Unicode normalization
- Replaced multiple spaces with a single space
- Removed unnecessary control characters

---

# Corpus Statistics

| Statistic | Value |
|------------|---------------:|
| Total Sentences | **77,685,001** |
| Total Words | **902,393,016** |
| Total Characters | **5,085,331,598** |
| Average Sentence Length | **11.62 words/sentence** |
| Average Word Length | **5.64 characters/word** |
| Unique Tokens | **7,916,018** |
| Type Token Ratio (TTR) | **0.00877** |

---

# Formulae Used

### Average Sentence Length

Average Sentence Length is calculated as:

```
Average Sentence Length =
Total Number of Words
---------------------
Total Number of Sentences
```

Result:

```
11.62 words/sentence
```

---

### Average Word Length

Average Word Length is calculated as:

```
Average Word Length =
Total Characters
----------------
Total Words
```

Result:

```
5.64 characters/word
```

---

### Type Token Ratio (TTR)

Type Token Ratio is calculated as:

```
TTR =
Number of Unique Tokens
-----------------------
Total Number of Tokens
```

Result:

```
0.00877
```

---

# Project Workflow

```
                    te.txt
                       │
                       ▼
               Text Preprocessing
                       │
                       ▼
          Sentence Tokenization
                       │
                       ▼
         all_sentences.parquet
                       │
                       ▼
            Word Tokenization
                       │
                       ▼
           all_words.parquet
                       │
                       ▼
          Corpus Statistics
```

---

# Technologies Used

- Python
- Pandas
- Regular Expressions (`re`)
- PyArrow
- Unicode Normalization

---

# Files Included

```
ASSIGNMENT-1.ipynb
```

Complete implementation of:

- Preprocessing
- Sentence Tokenizer
- Word Tokenizer
- Corpus Statistics

```
te.txt
```

Original Telugu corpus extracted from IndicCorpV2.

```
all_sentences.parquet
```

Sentence-level corpus.

```
all_words.parquet
```

Word/token-level corpus.

---

# Memory-Efficient Processing

Since the original Telugu corpus is approximately **15.8 GB**, the implementation uses a streaming approach instead of loading the complete dataset into memory.

The processing pipeline:

- Reads the corpus line by line
- Performs sentence tokenization incrementally
- Performs word tokenization incrementally
- Writes Parquet files in batches
- Computes corpus statistics during processing

This approach enables efficient processing of very large corpora while using limited system memory.

---

# Conclusion

A complete rule-based Telugu NLP preprocessing pipeline was successfully implemented.

The project includes:

- Text preprocessing
- Sentence tokenization
- Word tokenization
- Parquet file generation
- Corpus statistics computation

The implementation successfully processed a **15.8 GB Telugu corpus** and generated sentence-level and token-level datasets along with the required corpus statistics.

---

# Dataset Reference

AI4Bharat. **IndicCorpV2** Dataset.

Hugging Face:

https://huggingface.co/datasets/ai4bharat/IndicCorpV2
