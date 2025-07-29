
<img width="1024" height="1024" alt="ChatGPT Image Jul 27, 2025, 05_36_42 PM" src="https://github.com/user-attachments/assets/0da24bcd-4a6d-42b3-88c1-fd6f6f197ed4" />

# 🤖 AI Powered Resume Ranker

A simple AI tool that compares a candidate's resume to a job description and calculates a **match score**.

---

## 🎯 Project Goal

Help junior candidates and students evaluate how well their resume matches a given job description and improve their chances of getting noticed.

---

## 🚀 Features (So Far)

- 📄 Upload resume (PDF or DOCX)
- 📋 Paste job description
- 📊 Get a **match score** based on text similarity (TF-IDF + cosine similarity)

> ✅ Match score ranges from 0 to 100  
> ✅ Simple Streamlit UI for interaction
> ✅ Match explanation based on keywords found or missing inthe resume

---

## ⚙️ Tech Stack

- 🐍 Python 3.10+
- 📊 scikit-learn (TF-IDF & cosine similarity)
- 🧠 PyPDF2 & python-docx (file parsing)
- 🌐 Streamlit (web app)

---

## 🧪 How It Works

1. The user uploads their resume
2. The user enters a job description
3. The app extracts text from the file
4. Both texts are vectorized using `TfidfVectorizer`
5. Cosine similarity is calculated → final score is shown

---

## 📂 Project Structure

AI-Powered-Resume-Ranker/
├── app.py
├── utils/
│   ├── __init__.py
│   ├── parser.py
│   └── analyzer.py 
├── README.md
└── requirements.txt

---

## 📌 Roadmap

✅ Match Score Calculator

✅ Match Explanation

🔄 Improvement Suggestions (coming soon)

🔄 Dashboard + Visual Analytics (future)

