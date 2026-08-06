import streamlit as st
import pickle

st.set_page_config(page_title="Spam Email Detector", page_icon="📧", layout="centered")


@st.cache_resource
def load_model():
    with open("spam_model.pkl", "rb") as f:
        clf = pickle.load(f)
    return clf


clf = load_model()

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
        # Feed raw text directly — the pipeline's CountVectorizer step
        # handles tokenizing/lowercasing, matching how it was trained
        prediction = clf.predict([user_input])[0]

        if prediction == 1:
            st.error("🚫 This looks like SPAM.")
        else:
            st.success("✅ This looks like a legitimate (HAM) message.")

        if hasattr(clf, "predict_proba"):
            proba = clf.predict_proba([user_input])[0]
            st.write(f"Confidence — Spam: {proba[1]*100:.2f}% | Ham: {proba[0]*100:.2f}%")

st.markdown("---")
st.caption("Built with Streamlit • Naive Bayes model trained on SMS/email spam dataset")
