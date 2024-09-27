import pdfplumber

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Path to your PDF file
pdf_path = "F:\My Document/Lab Report - R513518.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Print the extracted text (optional, for verification)
print("Extracted Text from PDF:")
print(pdf_text)