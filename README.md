# 📩 SMS Spam Detection using Machine Learning

## 📌 Project Overview

This project is a Machine Learning-based SMS Spam Detection System that classifies text messages into two categories:

- **Spam:** Unwanted or promotional messages.
- **Ham:** Genuine and legitimate messages.

The project uses Natural Language Processing (NLP) and Machine Learning techniques to identify spam messages and provides an interactive web interface using Streamlit.

## 🎯 Project Objective

The main objective of this project is to build an intelligent system that can automatically detect spam SMS messages and help users distinguish between genuine and suspicious messages.

## 🛠️ Technologies Used

- Python
- Machine Learning
- Natural Language Processing (NLP)
- Scikit-learn
- TF-IDF Vectorization
- Streamlit
- Pickle

## ✨ Features

- User-friendly web interface.
- Real-time SMS classification.
- Spam and Ham detection.
- Machine Learning-based predictions.
- Interactive prediction system.

## 📂 Project Structure

SMS-Spam-Detection/
│
├── app.py
├── spam_model.pkl
├── tfidf_vectorizer.pkl
└── README.md

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
https://github.com/nilaypatel2607/SMS-Spam-Detection.git

Step 2: Navigate to the Project Folder
cd SMS-Spam-Detection

Step 3: Install Required Libraries
pip install streamlit pandas scikit-learn

Step 4: Run the Application
streamlit run app.py

🚀 How to Use
1. Run the Streamlit application.
2. Open the application in your browser.
3. Enter an SMS message in the text box.
4. Click on the Predict button.
5. The application will classify the message as Spam or Ham.
🧠 Machine Learning Workflow
1. Data preprocessing.
2. Text vectorization using TF-IDF.
3. Machine Learning model training.
4. Model serialization using Pickle.
5. Loading the trained model into Streamlit.
6. Predicting whether a message is Spam or Ham.
👩‍💻 Author
Nilay Patel
