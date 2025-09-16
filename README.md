This Repo includes:
- Paragraph tokenization using **spaCy Tokenizer**
- **BPE (Byte Pair Encoding)** for subword tokenization
- **Word_pair** of two words
---
**Veera Ganga Godina
700769576**
---

# Tokenization Example
### 1️⃣ Install & Download Model

pip install spacy
python -m spacy download xx_ent_wiki_sm

input : “Students often struggle with managing their time effectively. Sometimes, they procrastinate, which leads to stress. However, with practice, they can develop better habits.”

### 🧮 Example Run

```python

# input text
text = “Students often struggle with managing their time effectively. Sometimes, they procrastinate, which leads to stress. However, with practice, they can develop better habits.”

# Manual tokenization (splitting by spaces)
manual_tokens = text.split()

# spaCy tokenization
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
spacy_tokens = [token.text for token in doc]

# Compare results
print("Original Text:\n", text, "\n")
print("Naïve space-based tokens:\n", naive_tokens, "\n")
print("Manual corrected tokens:\n", manual_tokens, "\n")
print("spaCy tokens:\n", spacy_tokens, "\n")
```

# BPE Learner
### 🧮 Example Run
```python
input : low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new

Enter number of merges to learn (default 10): 3
```

input : తెలుగు ఒక ప్రాచీన భాష. ఇది దక్షిణ భారతదేశంలో విస్తరించి ఉంది. తెలుగు సాహిత్యం గొప్ప సంపదను కలిగి ఉంది. ఈ భాషలో అనేక కవులు, రచయితలు ఉన్నారు. వారి రచనలు ప్రపంచవ్యాప్తంగా గుర్తింపు పొందాయి.

Enter number of merges to learn (default 30): 20

Enter : 
తెలుగు
భాష
సాహిత్యం
రచయితలు
ప్రపంచ


# Word pair

### 🧮 Example Run
```python
source = "Sunday"
target = "Saturday"

# Model A Equal cost for all operations
dist_a, dp_a = edit_distance(source, target, sub_cost=1, ins_cost=1, del_cost=1)
path_a = reconstruct_path(dp_a, source, target, sub_cost=1, ins_cost=1, del_cost=1)

# Model B Higher Cost for Substitution
dist_b, dp_b = edit_distance(source, target, sub_cost=2, ins_cost=1, del_cost=1)
path_b = reconstruct_path(dp_b, source, target, sub_cost=2, ins_cost=1, del_cost=1)
```
