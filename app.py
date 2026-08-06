import streamlit as st
import pickle
import re
import string

st.set_page_config(page_title="Spam Email Detector", page_icon="📧", layout="centered")


@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer


model, vectorizer = load_model()


def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


st.title("📧 Spam Email Detector")
st.write("Paste an email or message below to check whether it's spam or not.")

user_input = st.text_area(
    "Enter email/message text:",
    height=200,
    placeholder="Type or paste the email content here...",
)

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        proba = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(vectorized)[0]

        # NOTE: adjust this condition to match how your labels were encoded
        # (e.g. 1/0, "spam"/"ham", True/False)
        is_spam = prediction == 1 or str(prediction).lower() == "spam"

        if is_spam:
            st.error("🚫 This looks like SPAM.")
        else:
            st.success("✅ This looks like a legitimate (HAM) message.")

        if proba is not None:
            st.write(f"Confidence — Spam: {proba[1]*100:.2f}% | Ham: {proba[0]*100:.2f}%")

st.markdown("---")
st.caption("Built with Streamlit • Model trained on a spam/ham email dataset")
