import gradio as gr
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Загрузка модели и векторизатора
model = joblib.load("logistic_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

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
iface = gr.Interface(
    fn=predict_sentiment,
    inputs="text",
    outputs="text",
    title="Amazon Sentiment Classifier",
    description="Enter an Amazon product review to detect its sentiment",
    theme="soft",
)

# Запуск с публичной ссылкой
iface.launch(share=True)
