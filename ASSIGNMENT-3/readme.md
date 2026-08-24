# Assignment 3 — DFA and FST

## Overview

This assignment implements two fundamental concepts from Natural Language Processing:

1. **DFA (Deterministic Finite Automaton)** for validating simplified English words.
2. **FST (Finite State Transducer)** for noun morphological analysis and pluralization.

The notebook is designed to run in a **local Linux/Jupyter environment** and uses the supplied `brown_nouns.txt` vocabulary. It also generates DFA and FST state diagrams using Graphviz.

---

## Objectives

* Implement a DFA for simplified English words.
* Validate words based on character-level rules.
* Implement an FST for noun singular/plural morphology.
* Apply English pluralization rules.
* Analyze the supplied Brown noun vocabulary.
* Detect invalid word forms.
* Generate state diagrams using Graphviz.
* Save the morphological analysis to a CSV file.

---

## Requirements

### Software

* Python 3.x
* Jupyter Notebook
* pandas
* matplotlib
* graphviz Python package
* Graphviz system executable

Install the required Python packages:

```bash
pip install pandas matplotlib graphviz
```

On Ubuntu/Debian, install Graphviz:

```bash
sudo apt update
sudo apt install graphviz
```

---

## Required Files

Keep the following files in the same directory:

```text
NLP_Assignment_3_DFA_FST_LOCAL.ipynb
brown_nouns.txt
```

The notebook generates:

```text
brown_nouns_fst_output.csv

diagrams/
├── dfa_simplified_english.png
└── fst_noun_pluralization.png
```

---

# Part A — DFA

## Definition

A **Deterministic Finite Automaton (DFA)** is used to determine whether a given input string belongs to a specified language.

In this assignment, a valid simplified English word must:

* Start with a lowercase letter.
* Contain only lowercase letters.
* Contain no digits.
* Contain no spaces.
* Contain no punctuation.
* Contain no special characters.
* Contain no uppercase letters.

### DFA States

| State    | Description                        |
| -------- | ---------------------------------- |
| `q0`     | Start state                        |
| `q1`     | Valid word state / accepting state |
| `q_dead` | Invalid/dead state                 |

`q1` is the accepting state.

### Transition Logic

```text
q0 + lowercase letter → q1
q0 + anything else    → q_dead

q1 + lowercase letter → q1
q1 + anything else    → q_dead

q_dead + any input    → q_dead
```

The DFA implementation processes each character and determines whether the complete word is accepted.

---

## DFA Examples

| Input       | Result       |
| ----------- | ------------ |
| `cat`       | Accepted     |
| `dog`       | Accepted     |
| `a`         | Accepted     |
| `zebra`     | Accepted     |
| `dog1`      | Not Accepted |
| `1dog`      | Not Accepted |
| `DogHouse`  | Not Accepted |
| `Dog_house` | Not Accepted |
| ` cats`     | Not Accepted |

---

## DFA Diagram

The notebook uses **Graphviz** to generate the DFA diagram automatically.

Output:

```text
diagrams/dfa_simplified_english.png
```

---

# Part B — FST

## Definition

A **Finite State Transducer (FST)** maps an input string to an output string while applying morphological rules.

The FST in this assignment performs **noun morphological analysis**.

The output format is:

```text
word+N+SG
```

for singular nouns and:

```text
root+N+PL
```

for plural nouns.

Where:

* `N` = Noun
* `SG` = Singular
* `PL` = Plural

For example:

```text
fox  → fox+N+SG
foxes → fox+N+PL
```

---

## Pluralization Rules

The notebook implements three main pluralization rules.

| Rule          | Condition                         | Example       |
| ------------- | --------------------------------- | ------------- |
| E insertion   | Ends in `s`, `z`, `x`, `ch`, `sh` | `fox → foxes` |
| Y replacement | Ends in `y`                       | `try → tries` |
| S addition    | Otherwise                         | `bag → bags`  |

### Rule 1 — E Insertion

Words ending in:

```text
s, z, x, ch, sh
```

take `es`.

Examples:

```text
fox → foxes
watch → watches
bush → bushes
```

### Rule 2 — Y Replacement

Words ending in `y` replace `y` with `ies`.

Example:

```text
try → tries
```

### Rule 3 — S Addition

Other nouns receive `s`.

Example:

```text
bag → bags
dog → dogs
```

---

# FST Generation

The notebook implements a table-driven transition system.

```text
s, z, x, ch, sh → stem + es
y               → stem_without_y + ies
other           → stem + s
```

The FST can generate both singular and plural forms.

Examples:

```text
fox + SG → fox
fox + PL → foxes

watch + PL → watches

try + PL → tries

bag + PL → bags
```

---

# Brown Noun Corpus

The supplied:

```text
brown_nouns.txt
```

file is loaded and used as the vocabulary for morphological analysis.

The notebook:

1. Reads the Brown noun file.
2. Removes empty entries.
3. Accepts alphabetic words.
4. Removes duplicates.
5. Creates a normalized vocabulary for case-insensitive matching.

The notebook reports:

```text
Total entries: 201654
Unique nouns: 18733
```

---

# FST Morphological Analysis

Each Brown noun is analyzed using the following process.

### Step 1 — DFA Validation

The input is first checked by the DFA.

If it is invalid:

```text
Invalid Word
```

is returned.

### Step 2 — Find Possible Singular Root

For a valid word, the FST checks whether it could be a plural form.

For example:

```text
foxes → fox
tries → try
dogs → dog
```

### Step 3 — Vocabulary Verification

The possible root is checked against the supplied Brown noun vocabulary.

This prevents incorrect forms from being accepted.

For example:

```text
foxs
```

is not accepted as a plural because the appropriate plural generated by the rules is:

```text
foxes
```

### Step 4 — Assign Morphological Features

The final result is represented as:

```text
root+N+PL
```

or:

```text
word+N+SG
```

---

# Example Analysis

| Input   | FST Output     |
| ------- | -------------- |
| `fox`   | `fox+N+SG`     |
| `foxes` | `fox+N+PL`     |
| `try`   | `try+N+SG`     |
| `tries` | `try+N+PL`     |
| `bag`   | `bag+N+SG`     |
| `bags`  | `bag+N+PL`     |
| `foxs`  | `Invalid Word` |
| `1dog`  | `Invalid Word` |

---

# Output CSV

The complete Brown noun analysis is saved as:

```text
brown_nouns_fst_output.csv
```

The CSV contains:

| Column                   | Description                      |
| ------------------------ | -------------------------------- |
| `Word`                   | Original input word              |
| `Morphological Analysis` | FST result                       |
| `Root`                   | Root/singular form               |
| `Category`               | Noun (`N`)                       |
| `Number`                 | Singular (`SG`) or plural (`PL`) |
| `Status`                 | Valid or Invalid                 |

The notebook analyzes **18,739 words**, including the Brown vocabulary and explicit invalid test cases.

---

# Validation

The notebook includes validation tests for:

```text
fox      → fox+N+SG
foxes    → fox+N+PL
watch    → watch+N+SG
watches  → watch+N+PL
try      → try+N+SG
tries    → try+N+PL
foxs     → Invalid Word
1dog     → Invalid Word
```

All validation tests pass:

```text
All validation tests passed: True
```

---

# State Diagrams

Two diagrams are automatically generated.

### DFA

```text
diagrams/dfa_simplified_english.png
```

### FST

```text
diagrams/fst_noun_pluralization.png
```

The diagrams visually represent the transition structures implemented in the notebook.

---

# Bonus — State Reduction

The FST uses a compact representation by grouping suffix conditions:

```text
s, z, x, ch, sh → E insertion
y               → Y replacement
other           → S addition
```

This avoids creating separate states for every possible suffix while preserving the required morphological behavior.

---

# Project Structure

After executing the notebook, the directory should look like:

```text
.
├── NLP_Assignment_3_DFA_FST_LOCAL.ipynb
├── brown_nouns.txt
├── brown_nouns_fst_output.csv
│
└── diagrams/
    ├── dfa_simplified_english.png
    └── fst_noun_pluralization.png
```

---

# How to Run

### 1. Open the project directory

```bash
cd path/to/ASS-3
```

### 2. Make sure the required files are present

```text
NLP_Assignment_3_DFA_FST_LOCAL.ipynb
brown_nouns.txt
```

### 3. Start Jupyter Notebook

```bash
jupyter notebook
```

### 4. Open the notebook

```text
NLP_Assignment_3_DFA_FST_LOCAL.ipynb
```

### 5. Run all cells

The notebook will:

* Load the Brown noun vocabulary.
* Build and test the DFA.
* Generate the DFA diagram.
* Build and test the FST.
* Generate the FST diagram.
* Analyze the Brown noun corpus.
* Run validation tests.
* Generate `brown_nouns_fst_output.csv`.

---

# Conclusion

This assignment demonstrates how **finite-state models can be applied to NLP tasks**.

The DFA performs character-level word validation, while the FST performs morphological processing by identifying noun number and applying English pluralization rules.

The combination of DFA validation, FST morphology, vocabulary verification, and Graphviz visualization provides a complete finite-state approach to basic English word and noun analysis.
