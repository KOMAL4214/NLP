# Text Segmentation using Greedy Matching and Dynamic Programming

## Overview

This project implements and compares two approaches for **text segmentation**:

1. **Greedy Longest Matching**
2. **Dynamic Programming**

The objective is to split a continuous string of characters into meaningful words using a vocabulary and word-frequency information from a dataset.

The notebook also evaluates both methods using:

- Exact Sentence Accuracy
- Word Accuracy
- Average Levenshtein Edit Distance

---

## Dataset

The program loads the dataset from:

```text
text_segmentation_dataset.json
```

The dataset contains:

- `word_counts` – frequency of words in the corpus
- `test_cases` – input strings and their ground-truth segmentation
- `metadata` – information such as the total number of corpus words

The vocabulary is constructed from the available words, and the maximum vocabulary word length is calculated for efficient segmentation.

---

## Algorithms

### 1. Greedy Longest Matching

The greedy approach starts from the beginning of the input string and searches for the **longest possible word** present in the vocabulary.

For every position:

1. Check the longest possible substring.
2. If it exists in the vocabulary, select it.
3. Move forward by the selected word's length.
4. Continue until the complete string is segmented.

If no matching word is found, the current character is used as a fallback.

### Advantages

- Simple to implement
- Fast and straightforward
- Requires no probability calculations

### Limitation

The algorithm makes a locally optimal decision without considering future words. Therefore, choosing the longest word at the current position can lead to an incorrect overall segmentation.

---

### 2. Dynamic Programming

The dynamic programming approach finds the segmentation with the **highest probability** based on word frequencies.

For each possible word:

```text
P(word) = word frequency / total corpus words
```

Log probabilities are used instead of direct probabilities:

```text
log_probability = log(P(word))
```

The DP table stores the maximum log probability for every prefix of the input string.

The algorithm then reconstructs the best segmentation by storing the previous position and selected word.

If a complete segmentation cannot be found, the implementation falls back to the greedy approach.

---

## Evaluation

The following metrics are used.

### Exact Sentence Accuracy

Measures how many complete test cases were segmented exactly correctly.

```text
Exact Accuracy =
Number of completely correct segmentations / Total test cases
```

### Word Accuracy

Measures the proportion of correctly predicted words.

```text
Word Accuracy =
Correctly predicted words / Total ground-truth words
```

### Average Edit Distance

The notebook calculates the **Levenshtein edit distance** between the predicted and actual segmented sentences.

It measures the minimum number of:

- Insertions
- Deletions
- Substitutions

required to transform the predicted text into the correct text.

---

## Results

| Method | Exact Sentence Accuracy | Word Accuracy | Average Edit Distance |
|---|---:|---:|---:|
| Greedy | 69.10% | 82.21% | 1.290 |
| Dynamic Programming | **98.20%** | **99.14%** | **0.028** |

The Dynamic Programming approach performs substantially better than the greedy approach across all three evaluation metrics.

---

## Sample Results

### Example 1

Input:

```text
itthatthecitytakestepstothisproblem
```

Greedy:

```text
it that the city takes t e p s to this problem
```

Dynamic Programming:

```text
it that the city take steps to this problem
```

The dynamic programming approach produces a much more accurate segmentation.

### Example 2

Input:

```text
oftitlelawwasalsobythe
```

Both approaches produce:

```text
of title law was also by the
```

---

## Technologies Used

- **Python 3.14**
- JSON
- Dynamic Programming
- Greedy Algorithms
- Levenshtein Edit Distance
- Jupyter Notebook

The notebook was executed using a Python 3.14 environment.

---

## Project Structure

```text
.
├── ASSIGNMENT-2(3).ipynb
├── text_segmentation_dataset.json
└── README.md
```

---

## How to Run

### 1. Install Python

Make sure Python 3.x is installed.

### 2. Install Jupyter Notebook

```bash
pip install notebook
```

### 3. Place the Dataset

Keep the following file in the same directory as the notebook:

```text
text_segmentation_dataset.json
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
ASSIGNMENT-2(3).ipynb
```

and run the cells sequentially.

---

## Conclusion

The experiment demonstrates that **Dynamic Programming is significantly more effective than simple greedy matching for text segmentation**.

The greedy algorithm achieves **69.10% exact sentence accuracy**, while the dynamic programming approach achieves **98.20%**. Similarly, word accuracy improves from **82.21% to 99.14%**, and average edit distance decreases from **1.290 to 0.028**.

This shows the advantage of considering the **global probability of an entire segmentation** rather than making independent local decisions.