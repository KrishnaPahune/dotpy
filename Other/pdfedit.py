from pdf2image import convert_from_path
import pytesseract

# Full path to your scanned PDF file
pdf_path = r"C:\Users\krish\OneDrive\Desktop\Python\Other\SANDIP_SCOLAR.pdf"

# Convert PDF pages to images
pages = convert_from_path(pdf_path)

# Run OCR on each page
for i, image in enumerate(pages):
    print(f"\n--- Page {i + 1} ---")
    text = pytesseract.image_to_string(image)
    print(text)
