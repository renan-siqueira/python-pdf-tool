import PyPDF2


def extract_text(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''.join(page.extract_text() or '' for page in reader.pages)
    return text
