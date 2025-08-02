
<img width="1024" height="1024" alt="ChatGPT Image Jul 27, 2025, 05_36_42 PM" src="https://github.com/user-attachments/assets/0da24bcd-4a6d-42b3-88c1-fd6f6f197ed4" />

# AI Powered Resume Ranker

A simple AI tool that compares a candidate's resume to a job description and calculates a **match score**.

---

## Project Goal

Help junior candidates and students evaluate how well their resume matches a given job description and improve their chances of getting noticed.

---

##  Features

- Upload resume files in PDF or DOCX format
- Paste a job description as free text
- Get a match score (0 - 100) based on text similarity
- See which keywords are found and which are missing
- Get improvement suggestions to help optimize your resume
  
---

## Tech Stack

- Python 3
- Streamlit
- scikit - learn
- python - docx
- PyPDF2
  
---

## How It Works

1. The user uploads their resume
2. The user enters a job description
3. The app extracts text from the file
4. Both texts are vectorized using `TfidfVectorizer`
5. Cosine similarity is calculated -> final score is shown

---

## Project Structure

AI-Powered-Resume-Ranker/
├── app.py
├── utils/
│   ├── __init__.py
│   ├── parser.py
│   └── analyzer.py 
├── README.md
└── requirements.txt

---

## How to Run

1. Clone the repository  
2. Install dependencies:
      ```bash
   pip install -r requirements.txt

---
