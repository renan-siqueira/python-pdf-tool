import pdfplumber


def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        text = ''.join(page.extract_text() or '' for page in pdf.pages)
    return text
