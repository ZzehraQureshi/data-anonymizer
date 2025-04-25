#  Data Anonymization Tool

A Python-based anonymization tool that protects user privacy in datasets using:

-  **Differential Privacy** for numerical data
-  **K-Anonymity** for string data with three strategy options:
  - Suppression
  - Generalization
  - Synthetic Replacement

---

##  Features

- User-defined privacy level (ε) for numerical columns
- Custom strategy for each string column
- Outputs anonymized CSV while preserving data structure

---

##  Installation

```bash
git clone https://github.com/YOUR_USERNAME/data-anonymizer.git
cd data-anonymizer
pip install -r requirements.txt
