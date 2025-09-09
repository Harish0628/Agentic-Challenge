#----------------Importing modules----------------
from pypdf import PdfReader

#----------------Reading a PDF----------------
reader = PdfReader(r"C:\Computer Science\PYTHON\agentic-challenge\level1\test_pdf.pdf")   # put your PDF file name here
text = ""

# Extract text from all pages
for page in reader.pages:
    text += page.extract_text() + "\n"

print("Extracted Text from PDF:\n")
print(text[:500])   # print only first 500 chars for preview
