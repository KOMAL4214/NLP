import re
import pandas as pd

data=pd.read_parquet("new.parquet")
data.head()

all_sentences=[]
for k in data["text"]:
    pattern=r'(?<=[.!?])\s+'
    sentences=re.split(pattern,k)
    all_sentences.extend([s.strip() for s in sentences if s.strip()])

print("total sentences:", len(all_sentences))

leng=0
for k in all_sentences:
    leng+=len(k)

print("average length of sentences:", leng/len(all_sentences))

df=pd.DataFrame(all_sentences,columns=["text"])
df.to_parquet("all_sentences.parquet",index=False)

import re

TOKEN_PATTERN = re.compile(r"""
    https?://[^\s]+|                       # URLs
    \b[\w.+-]+@[\w.-]+\.\w+\b|             # Email IDs
    \d{1,2}[/-]\d{1,2}[/-]\d{2,4}|         # Dates (12/05/2024, 12-05-2024)
    \d+\.\d+|                              # Decimal numbers
    \d+|                                   # Integers
    [\u0C00-\u0C7F]+|                      # Telugu words
    [A-Za-z]+|                             # English words
    \.{3}|                                 # Ellipsis (...)
    [.,!?;:()"'\-]                         # Punctuation
""", re.VERBOSE)

words = []
for sentence in all_sentences:
    words.extend(TOKEN_PATTERN.findall(sentence))

print("Total words:", len(words))

le=0
for k in words:
    le+=len(k)

print("total_characters:", le)

print("average length of words:", le/len(words))

dw=pd.DataFrame(words,columns=["text"])
dw.to_parquet("all_words.parquet",index=False)

unique_words = len(set(words))

print("ttr : ", unique_words/len(words))
