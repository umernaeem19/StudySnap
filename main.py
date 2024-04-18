from PyPDF2 import PdfReader 
import string

def filter_text(text):
    printable = set(string.printable)
    filtered_text = ''.join(filter(lambda x: x in printable, text))
    return filtered_text

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

text = get_pdf_text(["constituition.pdf"])

# Filter out non-printable and non-ASCII characters
filtered_text = filter_text(text)

# Print the filtered text
print(filtered_text)
