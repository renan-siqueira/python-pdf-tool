import fitz as PyMuPDF


def extract_text(file_path):
    text = ""
    with PyMuPDF.open(file_path) as doc:
        text = ''.join(page.get_text() for page in doc)
    return text
