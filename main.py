import json
import os
import logging
from extractors import pypdf2_extractor, pdfminer_extractor, pymupdf_extractor, pdfplumber_extractor
from helpers import utils


def get_extractor(library_name):
    return {
        'pypdf2': pypdf2_extractor.extract_text,
        'pdfminer': pdfminer_extractor.extract_text,
        'pymupdf': pymupdf_extractor.extract_text,
        'pdfplumber': pdfplumber_extractor.extract_text
    }.get(library_name, None)


def process_file(file_path, libraries, output_dir):
    for library in libraries:
        extractor = get_extractor(library)
        if extractor:
            try:
                extracted_text = extractor(file_path)
                output_file = os.path.join(output_dir, f"{os.path.basename(file_path).split('.')[0]}_{library}.txt")
                utils.save_text_to_file(extracted_text, output_file)
            except Exception as e:
                logging.error(f"Error processing {file_path} with {library}: {e}")


def create_output_dir(base_dir, input_path, is_single_file):
    if is_single_file:
        output_dir = os.path.join(base_dir, os.path.basename(input_path).split('.')[0])
    else:
        output_dir = os.path.join(base_dir, os.path.basename(input_path))
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def main():
    with open('json/config.json') as config_file:
        config = json.load(config_file)

    logging.basicConfig(level=config.get("log_level", "INFO"))

    input_path = config["input_path"]
    libraries = config["libraries"]
    base_output_dir = config.get("output_path", "./output")

    is_single_file = os.path.isfile(input_path) and input_path.endswith('.pdf')
    output_dir = create_output_dir(base_output_dir, input_path, is_single_file)

    if is_single_file:
        process_file(input_path, libraries, output_dir)
    elif os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            if filename.endswith('.pdf'):
                process_file(os.path.join(input_path, filename), libraries, output_dir)
    else:
        logging.error("Invalid input path")


if __name__ == '__main__':
    main()
