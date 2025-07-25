**AI-Powered Resume Ranker — Phase 1: Requirements Definition (Mini PRD)**

---

### Project Objective

Develop an AI-powered system that ranks resumes based on their relevance to a junior-level job description in the tech industry. The system will provide a match score, explain the score, and suggest possible resume improvements.

---

### Input

1. **Candidate's Resume File**:
   - Supported formats: PDF, DOCX, TXT
2. **Job Description**:
   - Free text input
   - Option to enter a URL (future feature)

---

### Output

1. **Match Score**:
   - Range: 0 to 100
   - Calculated based on similarity between the resume and job description
2. **Score Explanation**:
   - Highlights which requirements are present or missing
   - Categories: Technologies, Experience, Education, Programming Languages
3. **Improvement Suggestions**:
   - Recommended phrasing or additions
   - Missing keywords that could improve the match score

---

### Target Audience

- Candidates applying for junior positions in software development, data, and QA
- Students and recent graduates looking to improve their chances of entering the tech industry

---

### Limitations and Future Plans

- The initial version will focus on basic text comparison
- Future versions will include:
  - Semantic analysis using embeddings
  - Support for job post URLs (e.g., LinkedIn)
  - File history for registered users
  - Graphs and dashboards