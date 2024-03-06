# S-to-Five takes a word or pdf document and converts every "s" character to a 5.
# This file was authored by: Kyle Shanahan

# These libraries need to be installed for the script to work:
# pip install python-docx
# pip install PyPDF2

# Steps to run the script:
# 1) Save the Script: Save the provided Python script to a file with a .py extension. You can name it whatever you like, such as text_replace.py.
# 2) Navigate to Script Directory: Open a terminal or command prompt and navigate to the directory where you saved the Python script using the cd command:cd path/to/directory
# 3) Execute the script:
# For Word Documents --> python text_replace.py your_document.docx <-- Make sure to replace "your_document" with the document name of your file
# For PDF Documents --> python text_replace.py your_document.pdf <-- Make sure to replace "your_document" with the document name of your file
# After running the script, it will create a modified version of your input document with 's' replaced by '5'. If it's a PDF file, the modified file will have a name starting with 'modified_', followed by the original file name.


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
