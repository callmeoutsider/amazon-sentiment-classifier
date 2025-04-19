---
title: Amazon Sentiment Classifier
emoji: 🧠
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
---

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
📥 [Download dataset from Kaggle](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)
> ⚠️ Due to file size limits, `amazon_train.txt` and `amazon_test.txt` are not included in this repository.  
> Please download them separately and place in the project root directory if you want to re-train the model.

---

## 🧰 Tools & Stack
- Python 3.12
- Jupyter Notebook (VS Code)
- Pandas, Scikit-learn, Matplotlib, Seaborn

---

## 🧪 Workflow Overview

| Step | Description |
|------|-------------|
| 1️⃣  | Load FastText-style dataset (`.txt`) |
| 2️⃣  | Clean and normalize text |
| 3️⃣  | Vectorize text using TF-IDF |
| 4️⃣  | Train a Logistic Regression classifier |
| 5️⃣  | Evaluate using classification report and confusion matrix |

---

## 📈 Results

- **Accuracy**: ~90%
- **F1-Score**: 0.90
- **Model**: Logistic Regression
- **Features**: Top 5000 TF-IDF terms

### 📊 Confusion Matrix

<p align="center">
  <img src="confusion_matrix.png" width="500"/>
</p>

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/outeast98/amazon-sentiment-classifier.git
   cd amazon-sentiment-classifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the Jupyter notebook:
   ```bash
   sentiment_analysis.ipynb
   ```
   and run each cell step by step.

---

## 🌐 Live Interface (Gradio)

This project includes a simple web interface built with [Gradio](https://gradio.app/), allowing users to test sentiment classification in real time.

### 🖥 How to launch the app locally:

1. Make sure you have the model and vectorizer saved as:
   - `logistic_model.pkl`
   - `tfidf_vectorizer.pkl`

2. Install Gradio:
   ```bash
   pip install gradio
   ```

3. Run the app:
   ```bash
   python app.py
   ```

The app will launch in your browser, where you can enter any product review and get an instant sentiment prediction:

```
😊 Positive  
😠 Negative
```

<p align="center">
  <img src="preview.png" width="600"/>
</p>

---

## 👨‍💻 Author

**Yevhenii Aloshyn**  
Machine Learning & Cybersecurity Enthusiast  
📍 Toronto, Canada  
[GitHub](https://github.com/callmeoutsider)