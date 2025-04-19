import gradio as gr
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Загрузка модели и векторизатора
with open("logistic_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Предобработка текста
def clean_text(text):
    return text.lower()

# Предсказание
def predict_sentiment(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return "😊 Positive" if prediction == 1 else "😠 Negative"

# Интерфейс Gradio
iface = gr.Interface(fn=predict_sentiment, inputs="text", outputs="text", title="Amazon Sentiment Classifier")
iface.launch(share=True)
