import re

from jinja2.utils import missing


def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text)
    keywords = [w for w in words if len > 2]
    return list(set(keywords))

def analyze_keywords(resume_text, job_description):
    keywords = extract_keywords(job_description)
    found_words = []
    missing_words = []
    for keyword in keywords:
        if keyword.lower() in resume_text.lower():
            found_words.append(keyword)
        else:
            missing_words.append(keyword)
    return found_words, missing_words
