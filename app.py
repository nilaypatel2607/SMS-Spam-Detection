import streamlit as st
import pickle

# Load trained model
with open("spam_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load TF-IDF vectorizer
with open("tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# App title
st.title("SMS Spam Detection")
st.write("Enter a message to check whether it is Spam or Ham.")

# Input message
message = st.text_area("Enter your SMS message")

# Prediction button
if st.button("Predict"):
    if message.strip():
        transformed_message = vectorizer.transform([message])
        prediction = model.predict(transformed_message)

        if prediction[0] == 1:
            st.error("SPAM 🚨")
        else:
            st.success("HAM ✅")
    else:
        st.warning("Please enter a message.")