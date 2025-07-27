from PyPDF2  import PdfReader
import docx




def extract_text_from_pdf(file):
    text = ""
    reader = PdfReader(file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    text = ""
    doc = docx.Document(file)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_text_from_file(file):
    if file.name.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif file.name.endswith('.docx'):
        return extract_text_from_docx(file)
    else:
        return "Unsupported file format."