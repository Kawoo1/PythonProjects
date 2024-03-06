# S-to-Five takes a word or pdf document and converts every "s" character to a 5.

# These libraries need to be installed for the script to work:
# pip install python-docx
# pip install PyPDF2

# 
#

import os
import sys
import docx
from PyPDF2 import PdfReader, PdfWriter

def replace_text_in_docx(file_path):
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        paragraph.text = paragraph.text.replace('s', '5')
    doc.save(file_path)

def replace_text_in_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            page_text = page.extract_text()
            modified_text = page_text.replace('s', '5')
            writer.add_page(page)
            writer.update_page(len(writer.pages) - 1, {'/Contents': modified_text})

        with open(f"modified_{os.path.basename(file_path)}", 'wb') as output_file:
            writer.write(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if file_path.endswith('.docx'):
        replace_text_in_docx(file_path)
    elif file_path.endswith('.pdf'):
        replace_text_in_pdf(file_path)
    else:
        print("Unsupported file format. Only .docx and .pdf files are supported.")
