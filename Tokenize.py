# main.py

import spacy

# Step 1: Define text
text = "Students often struggle with managing their time effectively. Sometimes, they procrastinate, which leads to stress. However, with practice, they can develop better habits."

# Step 2: Naïve space-based tokenization
naive_tokens = text.split(" ")

# Step 3: Manual correction (separate punctuation manually)
manual_tokens = [
    "Students", "often", "struggle", "with", "managing", "their", "time", "effectively", ".",
    "Sometimes", ",", "they", "procrastinate", ",", "which", "leads", "to", "stress", ".",
    "However", ",", "with", "practice", ",", "they", "can", "develop", "better", "habits", "."
]

# Step 4: spaCy tokenization
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
spacy_tokens = [token.text for token in doc]

# Step 5: Print results
print("Original Text:\n", text, "\n")
print("Naïve space-based tokens:\n", naive_tokens, "\n")
print("Manual corrected tokens:\n", manual_tokens, "\n")
print("spaCy tokens:\n", spacy_tokens, "\n")
