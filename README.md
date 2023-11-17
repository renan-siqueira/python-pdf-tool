# PDF Text Extraction Tool

## Description

This project facilitates the extraction of text from PDF files using various Python libraries. It is designed to be flexible, allowing the choice among different text extraction libraries and supporting both single PDF file and directory containing multiple PDF files.

---

## Project Structure

```markdown
- main.py
- extractors/
  - __init__.py
  - pypdf2_extractor.py
  - pdfminer_extractor.py
  - pymupdf_extractor.py
  - pdfplumber_extractor.py
- helpers/
  - __init__.py
  - utils.py
- json/
  - params.json
```

---

## Configuration

- **Python:** This project is developed in Python. Ensure you have the latest version of Python installed.
- **Dependencies:** The required libraries are listed in each extraction file within the `extractors` folder. Install them using `pip install <library>`.

_Use the `requirements.txt` file to install all libraries at once_

---

## Usage

1. **Initial Setup:** Edit the `json/params.json` file to set the input path (`input_path`), output path (`output_path`), desired libraries (`libraries`), and log level (`log_level`).

Example `params.json`:

```json
{
    "input_path": "/path/to/pdf/or/directory",
    "output_path": "/path/to/output/directory",
    "libraries": ["pypdf2", "pdfminer"],
    "log_level": "INFO"
}
```

2. **Execution:** Run the `main.py` script to start the text extraction process.

```bash
python main.py
```

---

## Features

- Text extraction from PDF files using various libraries.
- Supports processing either a single file or multiple files in a directory.
- Automatic output folder generation based on input.
- Flexible configuration via the json/params.json file.
