import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.parser import extract_text_from_file
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    return cosine_similarity([vectors[0]], [vectors[1]])[0][0]

st.title("AI - Powered Resume Ranker - Basic Demo")

uploaded_file = st.file_uploader("upload your resume (PDF or DOCX)", type = ['pdf', 'docx'])
job_description = st.text_area("Enter the job description")

if st.button("Calculate Match Score"):
    if uploaded_file is not None and job_description.strip() != "":
        resume_text = extract_text_from_file(uploaded_file)
        similarity = compute_similarity(resume_text, job_description)
        score = round(similarity * 100, 2)
        st.success(f"Match Score: {score} / 100")
    else:
        st.error("Please upload a resume file and enter the job description.")