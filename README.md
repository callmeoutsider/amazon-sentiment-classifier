# 🧠 Amazon Sentiment Classifier

A fast and effective sentiment classification project using 3.6 million Amazon product reviews.  
Built with Logistic Regression, TF-IDF, and classic preprocessing — this project demonstrates scalable NLP on real-world data.

---

## 📦 Dataset
- **Source**: Amazon Reviews from Kaggle (`train.ft.txt`)
- **Size**: 3,600,000 reviews
- **Labels**:  
  - `__label__1` = Negative  
  - `__label__2` = Positive  
- **Format**: FastText-style plain text

---

## 🧰 Tools & Stack
- Python 3.12
- Jupyter Notebook (in VS Code)
- Pandas, Scikit-learn, Matplotlib, Seaborn

---

## 🧪 Workflow Overview

| Step | Description |
|------|-------------|
| 1️⃣  | Load `.txt` FastText-style dataset |
| 2️⃣  | Clean and normalize text |
| 3️⃣  | Vectorize using TF-IDF |
| 4️⃣  | Train a Logistic Regression classifier |
| 5️⃣  | Evaluate with classification report and confusion matrix |

---

## 📈 Results

- **Accuracy**: ~90%
- **F1-Score**: 0.90
- **Model**: Logistic Regression
- **Features**: 5000 top TF-IDF terms

Confusion Matrix:

*(add screenshot here or use `plt.savefig()` to export)*

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
